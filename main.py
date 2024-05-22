from fastapi import FastAPI
from api.agent import agent
from api.base import login, tenant
from api.knowledge import dataset, document, file

app = FastAPI(title="小羊AI")

app.include_router(login.router)
app.include_router(tenant.router)
app.include_router(agent.router)
app.include_router(dataset.router)
app.include_router(document.router)
app.include_router(file.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
