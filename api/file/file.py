from fastapi import APIRouter, UploadFile, File
from api.deps import SessionDep, StorageDep
from pydantic import BaseModel
from api.response import IResponse, fail_resp, ok_resp
import os
import uuid

router = APIRouter(tags=["文件"])


class UploadFileResp(BaseModel):
    filepath: str


@router.post(path="/api/v1/file/upload", summary="上传文件")
def upload_file(
        storage: StorageDep,
        file: UploadFile = File(...),
) -> IResponse[UploadFileResp]:
    src_filename = file.filename
    ext = os.path.splitext(src_filename)[-1]
    new_filename = uuid.uuid4().hex + ext

    try:
        filepath = storage.save(new_filename, file.file)
    except Exception as e:
        return fail_resp(msg=str(e))

    return ok_resp(data=UploadFileResp(filepath=filepath))


@router.get(path="/api/v1/file/{filename}", summary="下载文件")
def create_dataset(session: SessionDep):
    # todo
    pass
