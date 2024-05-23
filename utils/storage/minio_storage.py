from .base_storage import Storage
from minio import Minio
from typing import BinaryIO
import os


class MinioStorage(Storage):
    def __init__(
            self, endpoint: str, access_key: str, secret_key: str, bucket_name: str
    ):
        self.endpoint = endpoint
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name
        self.client = Minio(
            endpoint=self.endpoint,
            access_key=self.access_key,
            secret_key=self.secret_key,
            secure=False,
        )
        self.make_bucket()

    def make_bucket(self) -> str:
        if not self.client.bucket_exists(self.bucket_name):
            self.client.make_bucket(self.bucket_name)
        return self.bucket_name

    def save(self, object_name: str, file_data: BinaryIO) -> str:
        self.client.put_object(
            bucket_name=self.bucket_name,
            object_name=object_name,
            data=file_data,
            length=-1,
            part_size=10 * 1024 * 1024,
        )
        return os.path.join("http://{}".format(self.endpoint), self.bucket_name, object_name)

    def download(self, filename, target_filepath):
        raise NotImplementedError

    def delete(self, filename):
        raise NotImplementedError
