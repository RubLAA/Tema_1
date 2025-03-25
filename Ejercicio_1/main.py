def formatear_receta(cadena_corrupta):
    try:
        cadena_volteada = cadena_corrupta[::-1]  # Volteamos la cadena
        
        # Dividir por espacios para separar posibles números y texto
        partes = cadena_volteada.split()
        
        # Buscamos partes numéricas (calorías)
        calorias = None
        nombre_partes = []
        
        for parte in partes:
            if parte.isdigit():
                if calorias is None:  # Tomamos solo el primer número encontrado
                    calorias = parte.lstrip('0') or '0'  # Quita ceros a la izquierda
            else:
                nombre_partes.append(parte)
        
        if calorias is None or not nombre_partes:
            raise ValueError("Formato de cadena incorrecto")
        
        nombre_receta = ' '.join(nombre_partes[::-1])  # Volteamos las palabras del nombre
        
        return f"La receta de {nombre_receta} contiene {calorias} calorías."
    
    except Exception as e:
        return f"Error: {e}. Cadena no válida."

print(formatear_receta("500 nómlas"))