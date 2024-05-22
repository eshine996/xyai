from fastapi import APIRouter, Query
from pydantic import BaseModel, Field
from api.deps import SessionDep
from api.common import ResponseModel
from typing import List

router = APIRouter(tags=["知识库"])


class Dataset(BaseModel):
    dataset_name: str
    desc: str


@router.post(path="/api/v1/dataset/create", summary="创建知识库")
def create_dataset(session: SessionDep, req: Dataset) -> ResponseModel():
    # todo
    pass


@router.get(path="/api/v1/dataset/delete", summary="通过id删除知识库")
def del_dataset_by_id(session: SessionDep, dataset_id: str = Query()) -> ResponseModel():
    # todo
    pass


@router.post(path="/api/v1/dataset/update", summary="通过id更新知识库信息")
def del_dataset_by_id(session: SessionDep, req: Dataset) -> ResponseModel():
    # todo
    pass


@router.get(path="/api/v1/dataset/list", summary="获取知识库列表")
def del_dataset_list(session: SessionDep, req: Dataset) -> ResponseModel(data=List[Dataset]):
    # todo
    pass