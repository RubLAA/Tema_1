def agregar_item(inventario, item):
    """
    Añade un ítem al inventario si no está repetido.
    
    :param inventario: Lista actual de ítems.
    :param item: Nuevo ítem a añadir.
    :raises ValueError: Si el ítem ya existe en el inventario.
    :return: None (modifica la lista original).
    """
    if item in inventario:
        raise ValueError(f"El ítem '{item}' ya existe en el inventario.")
    inventario.append(item)

# Ejemplo de uso:
inventario = ["espada", "poción", "escudo"]

try:
    agregar_item(inventario, "arco")
    agregar_item(inventario, "lanza")
    print("Ítem añadido:", inventario)  # Output: ["espada", "poción", "escudo", "arco", "lanza"]
    agregar_item(inventario, "poción")  # Lanza ValueError
    
except ValueError as e:
    print("Error:", e) # Output: "El ítem 'poción' ya existe en el inventario."