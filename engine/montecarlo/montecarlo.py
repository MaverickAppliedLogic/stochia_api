import distributions.continuous.normal as nsim
import distributions.continuous.uniform as usim
import  distributions.continuous.exponential as exsim

def generate_sim_montecarlo(dist_type: str, params: dict, size: int) -> dict:

    match dist_type:
        case "normal":
            return nsim.gen_normal_montecarlo(params["p1"],params["p2"], size)
        case "uniform":
            return usim.gen_uniform_montecarlo(params["p1"],params["p2"], size)
        case "exponential":
            return exsim.gen_exponential_montecarlo(params["p1"], size)
        case _:
            raise ValueError(f"Unknown distribution type: {dist_type}")






