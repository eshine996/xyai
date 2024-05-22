from fastapi import APIRouter
from api.deps import SessionDep
from api.common import ResponseModel

router = APIRouter(tags=["知识库"])


@router.post(path="/api/v1/file/upload", summary="上传文件")
def create_dataset(session: SessionDep) -> ResponseModel():
    # todo
    pass
