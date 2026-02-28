
import distribution.distribution as dist

if __name__ == "__main__":
    dist_type = input("Tipo de distribucion: ")
    params = {}

    param = input("new param: ")
    count = 0
    while not (param == "stop"):
        count += 1
        params[f"p{count}"] = int(param)
        param = input("new param: ")

    print(dist.generate_distribution(dist_type,params,10))
