import numpy as np

def gen_geometrical_montecarlo(p: int) -> dict:

    tries = np.random.geometric(p, size=None)

    return {
        "distribution": "geometrical",
        "tries": tries,
    }
