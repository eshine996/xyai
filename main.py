from fastapi import FastAPI
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

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
