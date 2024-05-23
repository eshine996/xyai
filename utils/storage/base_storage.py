from abc import ABC, abstractmethod


class BaseStorage(ABC):

    @abstractmethod
    def save(self, filename: str, data):
        raise NotImplementedError

    @abstractmethod
    def download(self, filename, target_filepath):
        raise NotImplementedError

    @abstractmethod
    def delete(self, filename):
        raise NotImplementedError
