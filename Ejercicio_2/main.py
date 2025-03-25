def calcular_interes_compuesto():
    capital_inicial = 1000  # Valor fijo según el enunciado
    
    try:
        # Solicitar tasa de interés anual (1%-10%)
        tasa = float(input("Ingrese la tasa de interés anual (1-10%): "))
        if not 1 <= tasa <= 10:
            raise ValueError("La tasa debe estar entre 1% y 10%.")
        
        # Solicitar número de años
        años = int(input("Ingrese el número de años: "))
        if años < 1:
            raise ValueError("El número de años debe ser positivo.")
        
        # Cálculo del interés compuesto
        capital_final = capital_inicial * (1 + tasa / 100) ** años
        
        # Mostrar resultado con 2 decimales
        print(f"Capital final: ${capital_final:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}. Por favor, ingrese valores válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Ejecutar la función
calcular_interes_compuesto()