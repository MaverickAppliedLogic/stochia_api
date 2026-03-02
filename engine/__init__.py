import engine.montecarlo.montecarlo_gen as dist

if __name__ == "__main__":
    dist_type = input("Tipo de distribucion: ")
    params = {}

    param = input("new param: ")
    count = 0
    while not (param == "stop"):
        count += 1
        params[f"p{count}"] = float(param)
        param = input("new param: ")

    print(dist.generate_sim_montecarlo(dist_type,params,10000))
