import subprocess
import platform
import logging

def isolate_network():
    """
    Deshabilita las interfaces de red para aislar la máquina.
    """
    system = platform.system()
    logging.info(f"Intentando aislar la red en {system}...")
    
    try:
        if system == "Windows":
            # Comando para deshabilitar todos los adaptadores de red
            # Requiere privilegios de administrador
            cmd = "netsh interface set interface name=\"Wi-Fi\" admin=disable"
            subprocess.run(cmd, shell=True, check=True)
            cmd = "netsh interface set interface name=\"Ethernet\" admin=disable"
            subprocess.run(cmd, shell=True, check=True)
            logging.info("Adaptadores de red deshabilitados en Windows.")
        elif system == "Linux":
            # Ejemplo para Linux (necesita adaptación para distro/interfaz específica)
            cmd = "nmcli networking off"
             # O: "ip link set eth0 down"
            subprocess.run(cmd, shell=True, check=True)
            logging.info("Red deshabilitada en Linux.")
        else:
            logging.warning(f"Aislamiento de red no implementado para {system}.")
    except Exception as e:
        logging.error(f"Error al aislar la red: {e}")
