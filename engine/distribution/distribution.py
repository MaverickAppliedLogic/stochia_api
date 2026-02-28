import numpy as np

def generate_distribution(dist_type: str, params: dict, size: int) -> dict:
    if dist_type == "normal":
        values = np.random.normal(params["p1"], params["p2"], size)
    elif dist_type == "uniform":
        values = np.random.uniform(params["p1"], params["p2"], size)
    elif dist_type == "exponential":
        values = np.random.exponential(params["p1"], size)
    else:
        raise ValueError(f"Unknown distribution type: {dist_type}")

    return {
        "values": values.tolist(),
        "mean": float(np.mean(values)),
        "std": float(np.std(values)),
        "p5": float(np.percentile(values, 5)),
        "p95": float(np.percentile(values, 95))
    }
