def separar_personajes(personajes):
    """
    Separa personajes humanos y no humanos, ordenados alfabéticamente.
    
    :param personajes: Lista de diccionarios con claves 'nombre' y 'es_humano'.
    :return: Dos listas (humanos, no_humanos).
    """
    try:
        if not personajes:
            print("Advertencia: La lista de personajes está vacía.")
            return [], []
        
        humanos = []
        no_humanos = []
        
        for personaje in personajes:
            if not isinstance(personaje, dict) or 'nombre' not in personaje or 'es_humano' not in personaje:
                raise ValueError("Cada personaje debe ser un diccionario con 'nombre' y 'es_humano'.")
            
            if personaje['es_humano']:
                humanos.append(personaje['nombre'])
            else:
                no_humanos.append(personaje['nombre'])
        
        # Ordenar alfabéticamente
        humanos.sort()
        no_humanos.sort()
        
        return humanos, no_humanos
    
    except Exception as e:
        print(f"Error: {e}")
        return [], []

# Ejemplo de uso:
personajes = [
    {'nombre': 'Geralt', 'es_humano': True},
    {'nombre': 'Yennefer', 'es_humano': True},
    {'nombre': 'Ciri', 'es_humano': True},
    {'nombre': 'Eredin', 'es_humano': False},
    {'nombre': 'Triss', 'es_humano': True},
    {'nombre': 'Geralt', 'es_humano': True},  # Duplicado para prueba
    {'nombre': 'Dettlaff', 'es_humano': False},
    {'nombre': 'Syanna', 'es_humano': True},
    {'nombre': 'Emiel', 'es_humano': True},
    {'nombre': 'Gaunter O\'Dimm', 'es_humano': False},  # Error de escritura
]

humanos, no_humanos = separar_personajes(personajes)
print("Humanos:", humanos)
print("No humanos:", no_humanos)