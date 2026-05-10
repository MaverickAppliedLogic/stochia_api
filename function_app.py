import json
import logging
import numpy as np
import azure.functions as func

from engine.montecarlo.montecarlo_gen import generate_sim_montecarlo
from engine.markov.markov import gen_sim_markov
from engine.distribution.distribution import get_distribution

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


class _NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)


def _ok(data) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps(data, cls=_NumpyEncoder),
        mimetype="application/json",
        status_code=200,
    )


def _err(message: str, status: int = 400) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps({"error": message}),
        mimetype="application/json",
        status_code=status,
    )


@app.route(route="montecarlo", methods=["POST"])
def montecarlo(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
        result = generate_sim_montecarlo(
            dist_type=body["dist_type"],
            params=body["params"],
            size=body["size"],
        )
        return _ok(result)
    except (KeyError, TypeError) as e:
        return _err(f"Missing or invalid field: {e}")
    except ValueError as e:
        return _err(str(e))
    except Exception as e:
        logging.exception("montecarlo error")
        return _err(str(e), 500)


@app.route(route="markov", methods=["POST"])
def markov(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
        result = gen_sim_markov(
            states=body["states"],
            probs=body["probs"],
            init_state=body["init_state"],
            steps=body["steps"],
        )
        return _ok(result)
    except (KeyError, TypeError) as e:
        return _err(f"Missing or invalid field: {e}")
    except Exception as e:
        logging.exception("markov error")
        return _err(str(e), 500)


@app.route(route="distribution", methods=["POST"])
def distribution(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
        result = get_distribution(data=body["data"])
        if result is None:
            return _err("Empty or invalid data")
        return _ok(result)
    except (KeyError, TypeError) as e:
        return _err(f"Missing or invalid field: {e}")
    except Exception as e:
        logging.exception("distribution error")
        return _err(str(e), 500)
