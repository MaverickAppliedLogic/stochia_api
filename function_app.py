import json
import logging
import os
import time
import numpy as np
import azure.functions as func
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace.samplers import AlwaysOnSampler
from opencensus.trace.tracer import Tracer

from engine.montecarlo.montecarlo_gen import generate_sim_montecarlo
from engine.markov.markov import gen_sim_markov
from engine.distribution.distribution import get_distribution

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

_CONN_STR = os.environ.get("APPLICATIONINSIGHTS_CONNECTION_STRING", "")

# Conectar el logger de Python directamente a Application Insights
if _CONN_STR:
    _ai_handler = AzureLogHandler(connection_string=_CONN_STR)
    logging.getLogger().addHandler(_ai_handler)


def _track_request(name: str, url: str, status: int, duration_ms: float, success: bool):
    if not _CONN_STR:
        return
    try:
        tracer = Tracer(
            exporter=AzureExporter(connection_string=_CONN_STR),
            sampler=AlwaysOnSampler(),
        )
        with tracer.span(name=name) as span:
            span.add_attribute("http.status_code", status)
            span.add_attribute("http.url", url)
            span.add_attribute("http.method", "POST")
    except Exception:
        pass


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
    start = time.time()
    try:
        body = req.get_json()
        result = generate_sim_montecarlo(
            dist_type=body["dist_type"],
            params=body["params"],
            size=body["size"],
        )
        response = _ok(result)
    except (KeyError, TypeError) as e:
        response = _err(f"Missing or invalid field: {e}")
    except ValueError as e:
        response = _err(str(e))
    except Exception as e:
        logging.exception("montecarlo error")
        response = _err(str(e), 500)

    logging.info("REQUEST montecarlo status=%d", response.status_code)
    return response


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
        response = _ok(result)
    except (KeyError, TypeError) as e:
        response = _err(f"Missing or invalid field: {e}")
    except Exception as e:
        logging.exception("markov error")
        response = _err(str(e), 500)

    logging.info("REQUEST markov status=%d", response.status_code)
    return response


@app.route(route="distribution", methods=["POST"])
def distribution(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
        result = get_distribution(data=body["data"])
        if result is None:
            response = _err("Empty or invalid data")
        else:
            response = _ok(result)
    except (KeyError, TypeError) as e:
        response = _err(f"Missing or invalid field: {e}")
    except Exception as e:
        logging.exception("distribution error")
        response = _err(str(e), 500)

    logging.info("REQUEST distribution status=%d", response.status_code)
    return response
