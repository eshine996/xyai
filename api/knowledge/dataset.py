from fastapi import APIRouter, Query
import crud
from api.deps import SessionDep, TenantIdDep, CurrentUserDep
from api.response import IResponse, ok_resp, fail_resp
from model.dataset import DatasetBase

router = APIRouter(tags=["知识库"])


@router.post(path="/api/v1/dataset/create", summary="创建知识库")
def create_dataset(
        tenant_id: TenantIdDep,
        current_user: CurrentUserDep,
        req: DatasetBase,
        db_session: SessionDep,
) -> IResponse:
    try:
        _dataset = crud.dataset.create_dataset(
            tenant_id=tenant_id,
            user_id=current_user.user_id,
            dataset_base=req,
            db_session=db_session
        )
    except Exception as e:
        return fail_resp(msg="创建失败:" + str(e))

    return ok_resp()


@router.get(path="/api/v1/dataset/delete", summary="通过id删除知识库")
def del_dataset_by_id(
        tenant_id: TenantIdDep,
        current_user: CurrentUserDep,
        db_session: SessionDep,
        dataset_id: str = Query(),
) -> IResponse:
    try:
        ok = crud.dataset.delete_by_id(
            tenant_id=tenant_id,
            user_id=current_user.user_id,
            db_session=db_session,
            dataset_id=dataset_id
        )
    except Exception as e:
        return fail_resp(msg="删除失败：" + str(e))

    if not ok:
        return fail_resp()

    return ok_resp()


@router.post(path="/api/v1/dataset/update", summary="通过id更新知识库信息")
def del_dataset_by_id(session: SessionDep, req: DatasetBase) -> IResponse:
    # todo
    pass


@router.get(path="/api/v1/dataset/list", summary="获取知识库列表")
def del_dataset_list(session: SessionDep, req: DatasetBase) -> IResponse:
    # todo
    pass
