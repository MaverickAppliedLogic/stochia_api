def get_distribution(data: list[int]) -> dict:
    # 1. Clean data
    data = [d for d in data if d is not None]

    total = len(data)
    if total == 0:
        return None

    # 2. Frequencies
    frequencies = {}
    for d in data:
        frequencies[d] = frequencies.get(d, 0) + 1

    # 3. Probabilities
    probabilities = {value: freq / total for value, freq in frequencies.items()}

    # 4. Basic statistics
    import numpy as np
    arr = np.array(data)

    # 5. Final result
    return {
        "frequencies": frequencies,
        "probabilities": probabilities,
        "mean": float(np.mean(arr)),
        "std_dev": float(np.std(arr)),
        "p5": float(np.percentile(arr, 5)),
        "p95": float(np.percentile(arr, 95)),
        "min": float(np.min(arr)),
        "max": float(np.max(arr)),
        "total": total
    }
