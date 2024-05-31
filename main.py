from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from api.agent import agent
from api.base import login, tenant
from api.knowledge import dataset, document
from api.file import file
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="晓羊AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["POST", "GET"],
    allow_headers=["Tenant-ID", "XY-AI-Token"],
)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": str(exc)})


app.include_router(login.router)  # 登录相关
app.include_router(tenant.router)  # 租户相关
app.include_router(agent.router)  # 智能体相关
app.include_router(dataset.router)  # 数据集相关
app.include_router(document.router)  # 文档相关
app.include_router(file.router)  # 文件相关

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
