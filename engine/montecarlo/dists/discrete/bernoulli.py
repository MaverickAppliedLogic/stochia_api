import numpy as np

def gen_bernoulli_montecarlo(p: float, tries: int, simulation: int) -> dict:

    results = {
        "distribution": "bernoulli",
        "res": []
    }
    N = tries
    for sim in range(int(simulation)):
        values = np.random.binomial(1, p, int(N))
        results["res"].append({
        "tries": N,
        "mean": float(np.mean(values)),
        "std": float(np.std(values))
        })
        N += 500

    return results
