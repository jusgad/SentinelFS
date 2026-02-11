import sys
import time
import logging
import yaml
import os
from watchdog.observers import Observer
from src.core.monitor import RansomwareHandler

def load_config(config_path="config/settings.yaml"):
    try:
        with open(config_path, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error cargando configuración: {e}")
        sys.exit(1)

def setup_logging(log_file="logs/sentinel.log"):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )

def main():
    setup_logging()
    logging.info("Iniciando SentinelFS Monitor Anti-Ransomware...")

    config = load_config()
    paths_to_watch = config.get("directories_to_watch", [])
    
    if not paths_to_watch:
        logging.error("No se configuraron directorios para vigilar en settings.yaml.")
        sys.exit(1)

    event_handler = RansomwareHandler(config)
    observer = Observer()

    for path in paths_to_watch:
        if os.path.exists(path):
            logging.info(f"Monitoreando directorio: {path}")
            observer.schedule(event_handler, path, recursive=True)
        else:
            logging.warning(f"Directorio no encontrado: {path}")

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()

if __name__ == "__main__":
    main()
