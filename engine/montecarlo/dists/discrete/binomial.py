import numpy as np

def gen_binomial_montecarlo(n: int, p: float, simulations: int) -> dict:

    values = np.random.binomial(n, p, simulations)

    return {
        "distribution": "binomial",
        "mean": float(np.mean(values)),
        "std": float(np.std(values)),
        "p5": float(np.percentile(values, 5)),
        "p50": float(np.percentile(values, 50)),
        "p95": float(np.percentile(values, 95)),
    }
