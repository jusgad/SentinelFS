import requests
import logging
import json

def send_alert(webhook_url, message):
    """
    Envía una alerta a un webhook (ej. Discord, Slack, Telegram).
    """
    logging.info(f"Enviando alerta: {message}")
    if not webhook_url:
        logging.warning("No hay URL de webhook configurada. Omitiendo alerta.")
        return

    payload = {"content": message} # Por defecto para Discord
    # Para Telegram/Slack, la estructura del payload podría diferir.
    
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        logging.info("Alerta enviada exitosamente.")
    except Exception as e:
        logging.error(f"Error al enviar la alerta: {e}")
