import numpy as np

def gen_exponential_montecarlo(lam: float, size: int) -> dict:
    values = np.random.exponential(lam, size)

    return {
        "values": values.tolist(),
        "mean": float(np.mean(values)),
        "std": float(np.std(values)),
        "p5": float(np.percentile(values, 5)),
        "p95": float(np.percentile(values, 95))
    }