def get_distribution(datos: list[int]):
    # 1. Limpiar datos
    datos = [d for d in datos if d is not None]

    total = len(datos)
    if total == 0:
        return None

    # 2. Frecuencias
    frecuencias = {}
    for d in datos:
        frecuencias[d] = frecuencias.get(d, 0) + 1

    # 3. Probabilidades
    probabilidades = {valor: freq / total for valor, freq in frecuencias.items()}

    # 4. Estadísticas básicas
    import numpy as np
    arr = np.array(datos)

    estadisticas = {
        "media": float(np.mean(arr)),
        "desviacion": float(np.std(arr)),
        "p5": float(np.percentile(arr, 5)),
        "p95": float(np.percentile(arr, 95)),
        "min": float(np.min(arr)),
        "max": float(np.max(arr))
    }

    # 5. Resultado final
    return {
        "frecuencias": frecuencias,
        "probabilidades": probabilidades,
        "estadisticas": estadisticas,
        "total_datos": total
    }
