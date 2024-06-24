from fastapi import APIRouter
from api.response import IResponse, fail_resp, ok_resp
from api.deps import SessionDep, TenantIdDep, CurrentUserDep
import crud
from model.agent import AgentPublic
from typing import List

router = APIRouter(tags=["智能体"])


@router.get(path="/api/v1/conversation/list", summary="获取对话列表")
def get_conversation_list(
        tenant_id: TenantIdDep,
        current_user: CurrentUserDep,
        db_session: SessionDep,
) -> IResponse[List[AgentPublic]]:
    try:
        agent_list = crud.agent.get_agent_list(
            tenant_id=tenant_id,
            user_id=current_user.user_id,
            db_session=db_session
        )
    except Exception as e:
        return fail_resp(msg=str(e))

    return ok_resp(data=agent_list)


@router.post(path="/api/v1/conversation/create", summary="创建新对话")
def create_conversation(
        tenant_id: TenantIdDep,
        current_user: CurrentUserDep,
        db_session: SessionDep,
) -> IResponse[List[AgentPublic]]:
    try:
        agent_list = crud.agent.get_agent_list(
            tenant_id=tenant_id,
            user_id=current_user.user_id,
            db_session=db_session
        )
    except Exception as e:
        return fail_resp(msg=str(e))

    return ok_resp(data=agent_list)


@router.get(path="/api/v1/conversation/history", summary="获取对话历史记录")
def get_conversation_history(
        tenant_id: TenantIdDep,
        current_user: CurrentUserDep,
        db_session: SessionDep,
) -> IResponse[List[AgentPublic]]:
    try:
        agent_list = crud.agent.get_agent_list(
            tenant_id=tenant_id,
            user_id=current_user.user_id,
            db_session=db_session
        )
    except Exception as e:
        return fail_resp(msg=str(e))

    return ok_resp(data=agent_list)
