import time
import os
import logging
from collections import deque
from watchdog.events import FileSystemEventHandler
from src.actions.network import isolate_network
from src.actions.alerts import send_alert

class RansomwareHandler(FileSystemEventHandler):
    def __init__(self, config):
        self.config = config
        self.max_events = config['detection']['max_events']
        self.time_window = config['detection']['time_window_seconds']
        self.suspicious_extensions = set(config['detection']['suspicious_extensions'])
        self.webhook_url = config['mitigation'].get('webhook_url')
        
        # Diccionario para almacenar marcas de tiempo de eventos por directorio
        # Clave: ruta_directorio, Valor: deque de marcas de tiempo
        self.event_history = {}

    def on_created(self, event):
        if not event.is_directory:
            self.process_event(event.src_path, "CREADO")

    def on_modified(self, event):
        if not event.is_directory:
            self.process_event(event.src_path, "MODIFICADO")

    def on_moved(self, event):
        if not event.is_directory:
            # Verificar el nuevo nombre de archivo por extensiones sospechosas
            self.check_extension(event.dest_path)
            self.process_event(event.dest_path, "MOVIDO")

    def process_event(self, file_path, event_type):
        directory = os.path.dirname(file_path)
        self.check_burst(directory)
        self.check_extension(file_path)

    def check_extension(self, file_path):
        _, ext = os.path.splitext(file_path)
        if ext.lower() in self.suspicious_extensions:
            message = f"ALERTA: Extensión sospechosa detectada: {file_path} ({ext})"
            self.trigger_mitigation(message)

    def check_burst(self, directory):
        current_time = time.time()
        
        if directory not in self.event_history:
            self.event_history[directory] = deque()
        
        timestamps = self.event_history[directory]
        timestamps.append(current_time)

        # Eliminar eventos fuera de la ventana de tiempo
        while timestamps and timestamps[0] < current_time - self.time_window:
            timestamps.popleft()

        # Verificar si se superó el umbral
        if len(timestamps) > self.max_events:
            message = f"ALERTA: Actividad masiva sospechosa en {directory}. {len(timestamps)} eventos en {self.time_window}s."
            self.trigger_mitigation(message)
            # Limpiar historial para evitar disparos repetidos por la misma ráfaga
            timestamps.clear()

    def trigger_mitigation(self, message):
        logging.critical(message)
        print(f"\n[!!!] {message}")
        
        if self.config['mitigation'].get('enable_network_isolation'):
            isolate_network()
        
        send_alert(self.webhook_url, message)
