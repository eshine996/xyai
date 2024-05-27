from dataset import DatasetBackend
from uuid import UUID
import uuid


class XiaoYangDatasetBackend(DatasetBackend):
    def create_dataset(self, dataset_name: str) -> UUID:
        return uuid.uuid4()
