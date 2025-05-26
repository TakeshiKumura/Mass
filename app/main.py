from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# main.py
from .utils import generate_primitive_pythagorean_triples

app = FastAPI()

@app.get("/triples")
def get_triples(limit: int = 10):
    return generate_primitive_pythagorean_triples(limit)

# CORS設定（必要に応じて）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 静的ファイル（HTML/JSなど）を提供
app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/triples")
def get_triples(limit: int = 100):
    triples = generate_primitive_pythagorean_triples(limit)
    return JSONResponse(content={"triples": triples})
