from abc import ABC, abstractmethod
from uuid import UUID


class DatasetBackend(ABC):

    @abstractmethod
    def create_dataset(self, dataset_name: str) -> UUID:
        raise NotImplementedError
