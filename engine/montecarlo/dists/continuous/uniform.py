import numpy as np

def gen_uniform_montecarlo(low: int, high: int, size: int) -> dict:
    values = np.random.uniform(low, high, size)

    return {
        "values": values.tolist(),
        "mean": float(np.mean(values)),
        "std": float(np.std(values)),
        "p5": float(np.percentile(values, 5)),
        "p95": float(np.percentile(values, 95))
    }