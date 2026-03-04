import numpy as np

# TODO recibir una lista de intentos por simulación.
#  Que de los resultados de la fiabilidad de 'p' dependiendo el número de intentos
def gen_bernoulli_montecarlo(p: float, tries: int, simulation: int) -> dict:

    results = {"res": []}
    N = tries
    for sim in range(int(simulation)):
        values = np.random.binomial(1, p, int(N))
        results["res"].append({
        "tries": f"Results with {N} tries",
        "mean": float(np.mean(values)),
        "std": float(np.std(values))
        })
        N += 500

    return results
