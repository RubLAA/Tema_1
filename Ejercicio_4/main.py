import heapq

def priorizar_misiones(misione):
    misiones = list(misione)
    """
    :param misiones: Lista de tuplas (dificultad, nombre_mission).
    :return: Cola priorizada (solo nombres).
    """
    try:
        if not misiones:
            print("Advertencia: Lista de misiones vacía.")
            return []
        
        # Crear un heap basado en la dificultad
        heapq.heapify(misiones)  # Ordena in-place por el primer elemento de la tupla (dificultad)
        
        # Extraer nombres en orden de prioridad
        cola_priorizada = []
        while misiones:
            dificultad, nombre = heapq.heappop(misiones)
            cola_priorizada.append(nombre)
        
        return cola_priorizada
    
    except (TypeError, IndexError):
        print("Error: Formato incorrecto. Usa tuplas (dificultad, nombre).")
        return []
    except Exception as e:
        print(f"Error inesperado: {e}")
        return []

# Ejemplo de uso:
misiones = {
    (3, "Recuperar el artefacto"),
    (1, "Derrotar al jefe inicial"),
    (2, "Explorar el bosque"),
    (4, "Destruir la base enemiga"),
    (9, f"Derrotar al jefe final"),
    (7, "Descubre la verdad")
}

print("Misiones ordenadas:", priorizar_misiones(misiones))