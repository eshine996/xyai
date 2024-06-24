from fastapi import APIRouter
from api.response import IResponse, fail_resp, ok_resp
from api.deps import SessionDep, TenantIdDep, CurrentUserDep
import crud
from model.agent import AgentPublic
from typing import List

router = APIRouter(tags=["智能体"])


@router.get(path="/api/v1/agent/list", summary="获取智能体列表")
def get_agent_list(
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
