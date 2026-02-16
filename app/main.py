from fastapi import FastAPI

app = FastAPI(title="Hospitality Inventory SaaS")

@app.get("/health")
def health_check():
    return {"status": "ok"}
