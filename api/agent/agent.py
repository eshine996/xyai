from fastapi import APIRouter, Query
from api.deps import SessionDep
from api.common import ResponseModel
from pydantic import BaseModel
from typing import List

router = APIRouter(tags=["智能体"])


class Agent(BaseModel):
    agent_name: str
    desc: str
    type: int


@router.post(path="/api/v1/agent/create", summary="创建智能体")
def create_agent(session: SessionDep, req: Agent) -> ResponseModel():
    # todo
    pass


@router.post(path="/api/v1/agent/update", summary="更新智能体信息")
def update_agent(session: SessionDep, req: Agent) -> ResponseModel():
    # todo
    pass


@router.get(path="/api/v1/agent/getById", summary="根据id获取智能体信息")
def get_agent_by_id(session: SessionDep, agent_id: str = Query()) -> ResponseModel(data=Agent):
    # todo
    pass


@router.get(path="/api/v1/agent/conversation/list", summary="获取对话列表")
def get_conversation_list(session: SessionDep, agent_id: str = Query()) -> ResponseModel():
    # todo
    pass


@router.get(path="/api/v1/agent/conversation/rename", summary="重命名对话名称")
def raname_conversation(session: SessionDep) -> ResponseModel():
    # todo
    pass


@router.get(path="/api/v1/agent/conversation/stop", summary="停止对话")
def stop_conversation(session: SessionDep) -> ResponseModel():
    # todo
    pass


class ToolInfo(BaseModel):
    tool_name: str


@router.get(path="/api/v1/agent/getTools", summary="获取工具列表")
def create_agent(session: SessionDep) -> ResponseModel(data=List[ToolInfo]):
    # todo
    pass
