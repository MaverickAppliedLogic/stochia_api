import numpy as np

def gen_poisson_montecarlo(p: float, size: int) -> dict:

    values = np.random.poisson(p, size)

    return {
        "distribution": "poisson",
        "mean": float(np.mean(values)),
        "std": float(np.std(values)),
        "p5": float(np.percentile(values, 5)),
        "p50": float(np.percentile(values, 50)),
        "p95": float(np.percentile(values, 95))
    }
