from engine.markov.markov import sim_markov


def pedir_estados():
    print("=== CADENA DE MARKOV ===")
    print("Ingresa los estados separados por coma (ej: Soleado, Nublado, Lluvia):")
    entrada = input("> ")
    estados = [e.strip() for e in entrada.split(",")]
    return estados

def pedir_estado_inicial(estados):
    print("\nEstado inicial (elige uno de estos):")
    print(", ".join(estados))
    estado = input("> ").strip()
    while estado not in estados:
        print("Estado no válido. Intenta de nuevo.")
        estado = input("> ").strip()
    return estado

def pedir_pasos():
    print("\n¿Cuántos pasos quieres simular?")
    while True:
        try:
            pasos = int(input("> "))
            if pasos > 0:
                return pasos
        except:
            pass
        print("Número inválido. Intenta de nuevo.")

def pedir_matriz_transicion(estados):
    print("\nAhora define las probabilidades de transición.")
    print("Para cada estado, indica la probabilidad de pasar a cada otro estado.")
    print("Las probabilidades deben sumar 1.\n")

    matriz = {}

    for estado in estados:
        print(f"\n--- Desde '{estado}' ---")
        probs = {}
        suma = 0.0

        for destino in estados:
            while True:
                try:
                    p = float(input(f"Probabilidad de ir a '{destino}': "))
                    if 0 <= p <= 1:
                        probs[destino] = p
                        suma += p
                        break
                except:
                    pass
                print("Valor inválido. Debe ser un número entre 0 y 1.")

        if abs(suma - 1.0) > 1e-6:
            print("\n❌ Las probabilidades no suman 1. Vuelve a ingresar esta fila.")
            return pedir_matriz_transicion(estados)

        matriz[estado] = probs

    return matriz

# --- EJECUCIÓN DEL MENÚ ---
if __name__ == "__main__":
    estados = pedir_estados()
    estado_inicial = pedir_estado_inicial(estados)
    pasos = pedir_pasos()
    matriz = pedir_matriz_transicion(estados)

    print("\nSimulando cadena de Markov...\n")
    resultado = sim_markov(estado_inicial, matriz, pasos)

    print("Recorrido:")
    print(" → ".join(resultado))
