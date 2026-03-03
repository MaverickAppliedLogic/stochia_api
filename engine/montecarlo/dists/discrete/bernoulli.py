import numpy as np

# TODO recibir una lista de intentos por simulación.
#  Que de los resultados de la fiabilidad de 'p' dependiendo el número de intentos
def gen_bernoulli_montecarlo(p: float, tries: int) -> dict:

    values = np.random.binomial(1, p, int(tries))

    return {
        "mean": np.mean(values),
        "std": np.std(values),
        "p5": np.percentile(values, 5),
        "p95": np.percentile(values, 95)
    }
