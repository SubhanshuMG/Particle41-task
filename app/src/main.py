from fastapi import FastAPI, Request
from datetime import datetime
import os

app = FastAPI()

@app.get("/")
async def root(request: Request):
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "ip": request.client.host
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)