import numpy as np


def gen_multinomial_montecarlo(n: int, p: list[float], simulations: int) -> dict:

    values = np.random.multinomial(n, p, simulations)
    return {
        "distribution": "multinomial",
        "mean": np.mean(values, axis=0),
        "std": np.std(values, axis=0),
        "p5": np.percentile(values, 5, axis=0),
        "p95": np.percentile(values, 95, axis=0)
    }
