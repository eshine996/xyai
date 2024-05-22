from fastapi import APIRouter, Query
from pydantic import BaseModel, Field
from api.deps import SessionDep
from api.common import ResponseModel
from typing import List

router = APIRouter(tags=["知识库"])


class Dataset(BaseModel):
    dataset_name: str
    desc: str


@router.post(path="/api/v1/document/create", summary="上传文档")
def create_dataset(session: SessionDep, req: Dataset) -> ResponseModel():
    # todo
    pass


@router.get(path="/api/v1/document/delete", summary="删除文档")
def create_dataset(session: SessionDep, req: Dataset) -> ResponseModel():
    # todo
    pass


@router.get(path="/api/v1/document/list", summary="获取文档列表")
def create_dataset(session: SessionDep, dataset_id: str = Query()) -> ResponseModel():
    # todo
    pass


@router.get(path="/api/v1/document/preview", summary="文档预览")
def create_dataset(session: SessionDep, dataset_id: str = Query()) -> ResponseModel():
    # todo
    pass


@router.get(path="/api/v1/document/indexing-estimeate", summary="文档清洗分段结果预览")
def create_dataset(session: SessionDep, dataset_id: str = Query(), document_id: str = Query()) -> ResponseModel():
    # todo
    pass
