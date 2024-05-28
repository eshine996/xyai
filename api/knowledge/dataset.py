from fastapi import APIRouter, Query
import crud
from api.deps import SessionDep, TenantIdDep, CurrentUserDep, DatasetBackendDep
from api.response import IResponse, ok_resp, fail_resp
from model.dataset import DatasetBase, DatasetPublic
from uuid import UUID

router = APIRouter(tags=["知识库"])


@router.post(path="/api/v1/dataset/create", summary="创建知识库")
def create_dataset(
        tenant_id: TenantIdDep,
        current_user: CurrentUserDep,
        req: DatasetBase,
        db_session: SessionDep,
        dataset_backend: DatasetBackendDep
) -> IResponse:
    dataset_id = dataset_backend.create_dataset(req.dataset_name)
    try:
        _dataset = crud.dataset.create_dataset(
            tenant_id=tenant_id,
            user_id=current_user.user_id,
            dataset_base=req,
            db_session=db_session,
            dataset_id=dataset_id
        )
    except Exception as e:
        return fail_resp(msg="失败:" + str(e))

    return ok_resp()


@router.get(path="/api/v1/dataset/delete", summary="通过id删除知识库")
def del_dataset_by_id(
        tenant_id: TenantIdDep,
        current_user: CurrentUserDep,
        db_session: SessionDep,
        dataset_id: UUID = Query(),
) -> IResponse:
    try:
        ok = crud.dataset.delete_by_id(
            db_session=db_session,
            tenant_id=tenant_id,
            user_id=current_user.user_id,
            dataset_id=dataset_id
        )
    except Exception as e:
        return fail_resp(msg="失败：" + str(e))

    if not ok:
        return fail_resp()

    return ok_resp()


@router.post(path="/api/v1/dataset/update", summary="通过id更新知识库信息")
def update_dataset_by_id(
        tenant_id: TenantIdDep,
        current_user: CurrentUserDep,
        db_session: SessionDep,
        req: DatasetPublic
) -> IResponse:
    try:
        ok = crud.dataset.update(
            db_session=db_session,
            tenant_id=tenant_id,
            user_id=current_user.user_id,
            dataset_public=req
        )
    except Exception as e:
        return fail_resp(msg="失败：" + str(e))

    if not ok:
        return fail_resp()

    return ok_resp()


@router.get(path="/api/v1/dataset/getById", summary="通过id获取知识库信息")
def get_dataset_by_id(
        tenant_id: TenantIdDep,
        current_user: CurrentUserDep,
        db_session: SessionDep,
        dataset_id: UUID = Query()
) -> IResponse[DatasetPublic]:
    try:
        _dataset = crud.dataset.delete_by_id(
            db_session=db_session,
            tenant_id=tenant_id,
            user_id=current_user.user_id,
            dataset_id=dataset_id
        )
    except Exception as e:
        return fail_resp(msg="失败：" + str(e))

    return ok_resp(
        data=DatasetPublic(
            dataset_id=_dataset.dataset_id,
            dataset_name=_dataset.dataset_name,
            desc=_dataset.desc,
            dataset_type=_dataset.dataset_type,
        )
    )


@router.get(path="/api/v1/dataset/list", summary="获取知识库列表")
def del_dataset_list(
        tenant_id: TenantIdDep,
        current_user: CurrentUserDep,
        db_session: SessionDep,
) -> IResponse:
    try:
        dataset_list = crud.dataset.get_list(
            db_session=db_session,
            tenant_id=tenant_id,
            user_id=current_user.user_id,
        )
    except Exception as e:
        return fail_resp(msg="失败：" + str(e))

    return ok_resp(data=dataset_list)
