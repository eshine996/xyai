from fastapi import APIRouter, Query, Header
from pydantic import BaseModel, Field
from api.deps import SessionDep
from api.response import IResponse, ok_resp, fail_resp
import crud
from model import Tenant

router = APIRouter(tags=["租户"])


class CreateTenantReq(BaseModel):
    tenant_name: str = Field(..., title="租户名称")


@router.post(path="/api/v1/tenant/create", summary="创建租户")
def create_tenant(db_session: SessionDep, req: CreateTenantReq) -> IResponse[Tenant]:
    try:
        _tenant = crud.tenant.create_tenant(req.tenant_name, db_session)
    except Exception as e:
        return fail_resp(msg="创建失败:" + str(e))

    return ok_resp(data=_tenant)


@router.get(path="/api/v1/tenant/getById", summary="根据租户id获取租户信息")
def get_tenant_by_id(session: SessionDep, tenant_id: str = Query()) -> IResponse:
    # todo
    pass


@router.get(path="/api/v1/tenant/deleteById", summary="根据租户id删除租户信息")
def del_tenant_by_id(session: SessionDep, tenant_id: str = Query()) -> IResponse:
    # todo
    pass
