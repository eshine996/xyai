from fastapi import APIRouter, Query
from pydantic import BaseModel, Field
from api.deps import SessionDep
from api.response import IResponse
from typing import List
from enum import Enum
from uuid import UUID

router = APIRouter(tags=["知识库"])


class Document(BaseModel):
    dataset_id: UUID
    document_id: UUID
    document_url: str


@router.post(path="/api/v1/document/insert", summary="上传文档")
def insert_document_to_dify(session: SessionDep, req: Document) -> IResponse:
    # todo
    # 文档分片，存储到向量数据库。我觉得这个地方有俩种处理方式，一种是依赖于dify，一种事自己写。我打算写俩种
    # 存储文档链接到数据库
    pass


@router.get(path="/api/v1/document/delete", summary="删除文档")
def create_dataset(session: SessionDep, req: Document) -> IResponse:
    # todo
    pass


@router.get(path="/api/v1/document/list", summary="获取文档列表")
def create_dataset(session: SessionDep, dataset_id: str = Query()) -> IResponse:
    # todo
    pass


@router.get(path="/api/v1/document/preview", summary="文档预览")
def create_dataset(session: SessionDep, dataset_id: str = Query()) -> IResponse:
    # todo
    pass


@router.get(path="/api/v1/document/indexing-estimeate", summary="文档清洗分段结果预览")
def create_dataset(session: SessionDep, dataset_id: str = Query(), document_id: str = Query()) -> IResponse:
    # todo
    pass
