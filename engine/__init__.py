import pandas

import engine.montecarlo.montecarlo_gen as dist
from pandas import DataFrame as df

if __name__ == "__main__":
    dist_type = input("Tipo de distribucion: ")
    params = {}

    param = input("new param: ")
    count = 0
    while not (param == "stop"):
        count += 1
        params[f"p{count}"] = float(param)
        param = input("new param: ")

    results = df(dist.generate_sim_montecarlo(dist_type,params,10000))
    pandas.set_option('display.max_colwidth', None)
    pandas.set_option('display.max_rows', None)
    print(results)
