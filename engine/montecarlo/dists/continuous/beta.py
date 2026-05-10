import numpy as np

def gen_beta_montecarlo(alpha: float, beta: float, size: int) -> dict:
    values = np.random.beta(alpha + 1,beta + 1,size)

    return {
        "distribution": "beta",
        "values": values.tolist(),
        "mean": float(np.mean(values)),
        "std": float(np.std(values)),
        "p5": float(np.percentile(values, 5)),
        "p95": float(np.percentile(values, 95))
    }