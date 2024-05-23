from abc import ABC, abstractmethod
from typing import BinaryIO


class Storage(ABC):

    @abstractmethod
    def save(self, filename: str, data: BinaryIO) -> str:
        raise NotImplementedError

    @abstractmethod
    def download(self, filename, target_filepath):
        raise NotImplementedError

    @abstractmethod
    def delete(self, filename):
        raise NotImplementedError
