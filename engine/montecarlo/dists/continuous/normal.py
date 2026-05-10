import numpy as np

def gen_normal_montecarlo(mu: float, sigma: float, size: int) -> dict:
    values = np.random.normal(mu, sigma, size)

    return {
        "distribution": "normal",
        "values": values.tolist(),
        "mean": float(np.mean(values)),
        "std": float(np.std(values)),
        "p5": float(np.percentile(values, 5)),
        "p95": float(np.percentile(values, 95))
    }