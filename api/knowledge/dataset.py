from fastapi import APIRouter, Query
from pydantic import BaseModel
from api.deps import SessionDep
from api.response import IResponse, ok_resp

router = APIRouter(tags=["知识库"])


class Dataset(BaseModel):
    dataset_name: str


@router.post(path="/api/v1/dataset/create", summary="创建知识库")
def create_dataset(session: SessionDep, req: Dataset) -> IResponse:
    print(req.dataset_name)
    return ok_resp()


@router.get(path="/api/v1/dataset/delete", summary="通过id删除知识库")
def del_dataset_by_id(session: SessionDep, dataset_id: str = Query()) -> IResponse:
    # todo
    pass


@router.post(path="/api/v1/dataset/update", summary="通过id更新知识库信息")
def del_dataset_by_id(session: SessionDep, req: Dataset) -> IResponse:
    # todo
    pass


@router.get(path="/api/v1/dataset/list", summary="获取知识库列表")
def del_dataset_list(session: SessionDep, req: Dataset) -> IResponse:
    # todo
    pass
