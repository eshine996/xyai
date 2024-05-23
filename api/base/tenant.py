from fastapi import APIRouter, Query
from pydantic import BaseModel, Field
from api.deps import SessionDep
from api.response import IResponse

router = APIRouter(tags=["租户"])


class CreateTenantReq(BaseModel):
    tenant_name: str = Field(..., title="租户名称")


@router.post(path="/api/v1/tenant/create", summary="创建租户")
def create_tenant(session: SessionDep, req: CreateTenantReq) -> IResponse:
    # todo
    pass


class TenantInfo(BaseModel):
    tenant_id: str
    school_id: str


@router.get(path="/api/v1/tenant/getById", summary="根据租户id获取租户信息")
def get_tenant_by_id(session: SessionDep, tenant_id: str = Query()) -> IResponse:
    # todo
    pass


@router.get(path="/api/v1/tenant/deleteById", summary="根据租户id删除租户信息")
def del_tenant_by_id(session: SessionDep, tenant_id: str = Query()) -> IResponse:
    # todo
    pass
