import engine.montecarlo.dists.continuous.exponential as exsim
import engine.montecarlo.dists.continuous.normal as nsim
import engine.montecarlo.dists.continuous.uniform as usim
import engine.montecarlo.dists.continuous.beta as btsim
import engine.montecarlo.dists.discrete.bernoulli as besim
import engine.montecarlo.dists.discrete.binomial as bisim
import engine.montecarlo.dists.discrete.geometrical as gsim
import engine.montecarlo.dists.discrete.poisson as psim
import engine.montecarlo.dists.discrete.multinomial as msim

def generate_sim_montecarlo(dist_type: str, params: dict, size: int) -> dict:

    match dist_type:
        case "normal":
            return nsim.gen_normal_montecarlo(params["p1"],params["p2"], size)
        case "uniform":
            return usim.gen_uniform_montecarlo(params["p1"],params["p2"], size)
        case "exponential":
            return exsim.gen_exponential_montecarlo(params["p1"], size)
        case "beta":
            return btsim.gen_beta_montecarlo(params["p1"], params["p2"], size)
        case "bernoulli":
            return besim.gen_bernoulli_montecarlo(params["p1"], params["p2"], params["p3"])
        case "binomial":
            return bisim.gen_binomial_montecarlo(params["p1"], params["p2"], size)
        case "geometrical":
            return gsim.gen_geometrical_montecarlo(params["p1"])
        case "poisson":
            return psim.gen_poisson_montecarlo(params["p1"], size)
        case "multinomial":
            return msim.gen_multinomial_montecarlo(
                params["p1"], [
                    params["p2"], params["p3"], 1-(params["p2"] + params["p3"])], size )
        case _:
            raise ValueError(f"Unknown distribution type: {dist_type}")






