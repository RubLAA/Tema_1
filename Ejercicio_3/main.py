def palabras_comunes(lista1, lista2):
    try:
        # Convertir las listas a conjuntos para eliminar duplicados y encontrar intersección
        set1 = set(lista1)
        set2 = set(lista2)
        comunes = set1 & set2  # Intersección de conjuntos
        
        # Convertir el resultado a lista ordenada (opcional)
        return sorted(list(comunes))
    
    except TypeError:
        print("Error: Las entradas deben ser listas de palabras.")
        return []
    except Exception as e:
        print(f"Error inesperado: {e}")
        return []

# Ejemplo de uso:
lista1 = ["hola", "mundo", "python", "hola", "adios", "chocolate"]
lista2 = ["python", "code", "hola", "ejercicio", "chocolate"]
resultado = palabras_comunes(lista1, lista2)
print("Palabras comunes:", resultado)