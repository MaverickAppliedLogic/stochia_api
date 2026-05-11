import httpx
import logging
import os
from fastapi import FastAPI, HTTPException, Security, Request
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse

# ── configuración ─────────────────────────────────────────────────────────────

API_KEY = os.environ["API_KEY"]
FUNCTIONS_BASE_URL = os.environ["AZURE_FUNCTIONS_BASE_URL"].rstrip("/")
FUNCTIONS_KEY = os.environ["AZURE_FUNCTIONS_KEY"]

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

app = FastAPI(title="Stochia API", version="1.0.0")
logger = logging.getLogger("stochia")


# ── autenticación ─────────────────────────────────────────────────────────────

def verify_api_key(key: str = Security(api_key_header)) -> str:
    if key != API_KEY:
        raise HTTPException(status_code=401, detail="API key inválida")
    return key


# ── cliente HTTP hacia Azure Functions ────────────────────────────────────────

def functions_url(route: str) -> str:
    return f"{FUNCTIONS_BASE_URL}/{route}?code={FUNCTIONS_KEY}"


async def call_function(route: str, body: dict) -> dict:
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(functions_url(route), json=body)
            response.raise_for_status()
            return response.json()
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="Azure Functions tardó demasiado")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=502, detail=f"Error en Azure Functions: {e.response.text}")
    except Exception as e:
        logger.exception("Error inesperado llamando a Functions")
        raise HTTPException(status_code=500, detail=str(e))


# ── endpoints ─────────────────────────────────────────────────────────────────

@app.post("/montecarlo")
async def montecarlo(req: Request, _: str = Security(verify_api_key)):
    body = await req.json()
    result = await call_function("montecarlo", body)
    return JSONResponse(content=result)


@app.post("/markov")
async def markov(req: Request, _: str = Security(verify_api_key)):
    body = await req.json()
    result = await call_function("markov", body)
    return JSONResponse(content=result)


@app.post("/distribution")
async def distribution(req: Request, _: str = Security(verify_api_key)):
    body = await req.json()
    result = await call_function("distribution", body)
    return JSONResponse(content=result)


# ── health check ──────────────────────────────────────────────────────────────

@app.get("/health")
async def health():
    return {"status": "ok"}
