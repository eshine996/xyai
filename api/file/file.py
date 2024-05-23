from fastapi import APIRouter, UploadFile, File
from api.deps import SessionDep, StorageDep
from utils.storage import Storage
from pydantic import BaseModel
from api.response import IResponse, fail_resp, ok_resp

router = APIRouter(tags=["文件"])


class UploadFileResp(BaseModel):
    filepath: str


@router.post(path="/api/v1/file/upload", summary="上传文件")
def upload_file(
        storage: StorageDep,
        file: UploadFile = File(...),
) -> IResponse[UploadFileResp]:
    print(file.filename)
    storage.save(file.filename, file.read())
    return ok_resp()


@router.get(path="/api/v1/file/{filename}", summary="下载文件")
def create_dataset(session: SessionDep):
    # todo
    pass
