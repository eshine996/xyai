from utils.storage import Storage, MinioStorage
from config import settings, StorageType


def get_storage() -> Storage:
    if settings.STORAGE_TYPE == StorageType.MINIO:
        return MinioStorage(
            endpoint=settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            bucket_name=settings.MINIO_BUCKET_NAME
        )
    else:
        raise Exception("不支持的存储类型")
