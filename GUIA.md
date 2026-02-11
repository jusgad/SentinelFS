# 📘 Manual de Usuario de SentinelFS

Bienvenido a la guía oficial de **SentinelFS**. Este documento te guiará paso a paso para instalar, configurar y utilizar tu sistema de monitoreo anti-ransomware.

---

## 📋 Tabla de Contenidos

1. [Introducción](#introducción)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Instalación](#instalación)
4. [Configuración Detallada](#configuración-detallada)
5. [Ejecución del Monitor](#ejecución-del-monitor)
6. [Pruebas de Seguridad (Simulacros)](#pruebas-de-seguridad-simulacros)
7. [Solución de Problemas](#solución-de-problemas)

---

## 1. Introducción

**SentinelFS** es un programa diseñado para proteger tus carpetas importantes. Funciona como un "vigilante" silencioso que observa si:
*   Alguien (o algo) crea muchos archivos muy rápido (típico de un ataque de ransomware).
*   Los archivos cambian de nombre a extensiones extrañas (como `.crypted` o `.locked`).

Si detecta esto, SentinelFS puede avisarte por Discord/Telegram y desconectar Internet para evitar que el ataque se propague.

---

## 2. Requisitos del Sistema

*   **Sistema Operativo**: Windows 10/11 (recomendado) o Linux.
*   **Python**: Versión 3.8 o superior instalada.
*   **Permisos**: Privilegios de Administrador (para poder bloquear la red si es necesario).

---

## 3. Instalación

Sigue estos pasos para preparar el sistema:

1.  **Descargar el Proyecto**: Asegúrate de tener todos los archivos en una carpeta (ej. `Anti-Rasomware Basico`).
2.  **Abrir la Terminal**:
    *   En Windows: Abre CMD o PowerShell.
    *   Navega a la carpeta: `cd "ruta\a\tu\carpeta"`
3.  **Instalar Librerías**:
    Ejecuta el siguiente comando para instalar las herramientas necesarias:
    ```bash
    pip install -r requirements.txt
    ```

---

## 4. Configuración Detallada

El corazón de SentinelFS es el archivo `config/settings.yaml`. Puedes abrirlo con cualquier editor de texto (Bloc de notas, VS Code).

### Explicación de Parámetros:

*   **`directories_to_watch`**:
    *   Aquí pones las rutas de las carpetas que quieres cuidar.
    *   *Ejemplo*: `C:/Users/TuUsuario/Documentos/Finanzas`
    *   ⚠️ Usa barras inclinadas hacia adelante `/` o dobles barras invertidas `\\` en Windows.

*   **`detection`**:
    *   `max_events`: Cantidad máxima de cambios permitidos. (Recomendado: 50).
    *   `time_window_seconds`: Tiempo en segundos para contar esos cambios. (Recomendado: 10).
    *   *Significado*: "Si hay más de 50 cambios en 10 segundos, ¡es un ataque!"
    *   `suspicious_extensions`: Lista de extensiones prohibidas (ej. `.enc`).

*   **`mitigation`**:
    *   `enable_network_isolation`: `true` (activado) o `false` (desactivado). Si está en `true`, apagará el Wi-Fi al detectar peligro.
    *   `webhook_url`: Pega aquí tu enlace de Webhook de Discord o Telegram para recibir alertas en tu celular.

---

## 5. Ejecución del Monitor

Para iniciar la vigilancia:

1.  Abre tu terminal **como Administrador** (Importante para el bloqueo de red).
2.  Ejecuta:
    ```bash
    python main.py
    ```
3.  Verás un mensaje: `INFO - Iniciando SentinelFS Monitor Anti-Ransomware...`

¡Listo! El programa está corriendo. No cierres la ventana de la terminal.

---

## 6. Pruebas de Seguridad (Simulacros)

Es importante verificar que funcione sin esperar a un ataque real.

### Prueba A: Detección de Extensiones
1.  Crea un archivo de texto llamado `prueba.txt` en una carpeta vigilada.
2.  Cámbiale el nombre a `prueba.crypted`.
3.  **Resultado esperado**:
    *   En la consola verás: `ALERTA: Extensión sospechosa detectada...`
    *   Si configuraste el Webhook, recibirás una notificación.
    *   Si configuraste el bloqueo de red, tu internet se desconectará.

### Prueba B: Detección de Ráfaga
1.  Descarga o crea un pequeño script que genere 100 archivos vacíos rápidamente, o cópialos y pégalos manualmente muy rápido en la carpeta vigilada.
2.  **Resultado esperado**:
    *   Alerta de "Actividad masiva sospechosa".

---

## 7. Solución de Problemas

*   **Error "Module not found"**: Te faltó ejecutar `pip install -r requirements.txt`.
*   **La red no se desconecta**: Asegúrate de ejecutar `python main.py` en una terminal con permisos de Administrador.
*   **No envía alertas**: Verifica que la `webhook_url` en `settings.yaml` sea correcta y tenga comillas.

---
**Recuerda**: SentinelFS es una herramienta de monitoreo, no un antivirus completo. Úsalo como una capa extra de seguridad.
