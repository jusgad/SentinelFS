# SentinelFS: Monitor de Integridad Anti-Ransomware

SentinelFS es una herramienta modular diseñada para proteger a pequeñas empresas detectando patrones de comportamiento típicos de ransomware, como el cifrado masivo de archivos o el cambio repentino de extensiones.

## Características

*   **Monitoreo en Tiempo Real**: Utiliza `watchdog` para vigilar cambios en el sistema de archivos.
*   **Detección de Ráfagas**: Alerta si se modifican demasiados archivos en un corto periodo de tiempo.
*   **Detección de Extensiones**: Identifica archivos con extensiones sospechosas (ej. `.crypted`, `.locked`).
*   **Aislamiento de Red**: Capacidad para deshabilitar adaptadores de red (Wi-Fi/Ethernet) automáticamente al detectar una amenaza.
*   **Alertas**: Envío de notificaciones vía Webhook (Discord, Telegram, etc.).

## Instalación

1.  Clona el repositorio o descarga los archivos.
2.  Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

## Configuración

Edita el archivo `config/settings.yaml` para ajustar la configuración:

*   **directories_to_watch**: Lista de carpetas que deseas proteger.
*   **detection**: Ajusta los umbrales de detección (eventos máximos, ventana de tiempo).
*   **mitigation**: Configura la URL de tu webhook y si deseas activar el aislamiento de red.

## Uso

Ejecuta el script principal:

```bash
python main.py
```

Los registros de actividad se guardarán en `logs/sentinel.log`.

## Notas Importantes

*   **Permisos de Administrador**: Para que la función de aislamiento de red funcione correctamente, debes ejecutar el script con privilegios de administrador (Click derecho -> Ejecutar como administrador).
