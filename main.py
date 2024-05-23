from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from api.agent import agent
from api.base import login, tenant
from api.knowledge import dataset, document
from api.file import file

app = FastAPI(title="小羊AI")

app.include_router(login.router)  # 登录相关
app.include_router(tenant.router)  # 租户相关
app.include_router(agent.router)  # 智能体相关
app.include_router(dataset.router)  # 数据集相关
app.include_router(document.router)  # 文档相关
app.include_router(file.router)  # 文件相关


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": str(exc)})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
