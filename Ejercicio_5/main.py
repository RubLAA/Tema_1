import random
import re

def generar_ip_aleatoria():
    """Genera una dirección IP válida aleatoria."""
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def descomponer_ip(ip):
    """
    Descompone una dirección IP en sus octetos.
    :param ip: Dirección IP (str) en formato "X.X.X.X".
    :return: Lista de octetos o None si es inválida.
    """
    try:
        # Validar formato con regex
        if not re.match(r'^(\d{1,3}\.){3}\d{1,3}$', ip):
            raise ValueError("Formato de IP inválido.")
        
        octetos = ip.split('.')
        if len(octetos) != 4:
            raise ValueError("La IP debe tener 4 octetos.")
        
        # Validar rango de cada octeto (0-255)
        for octeto in octetos:
            num = int(octeto)
            if not 0 <= num <= 255:
                raise ValueError(f"Octeto inválido: {octeto} (debe ser 0-255).")
        
        return octetos
    
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Ejemplo de uso
ip_aleatoria = generar_ip_aleatoria()
print(f"Dirección IP generada: {ip_aleatoria}")

octetos = descomponer_ip(ip_aleatoria)
if octetos:
    print("Octetos:")
    for i, octeto in enumerate(octetos, 1):
        print(f"Octeto {i}: {octeto}")