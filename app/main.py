from fastapi import FastAPI

app = FastAPI(
    title="ZeroTouch AppSec Cloud",
    description="Enterprise Application Security Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "product": "ZeroTouch AppSec Cloud",
        "version": "1.0.0",
        "status": "Running"
    }

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }
