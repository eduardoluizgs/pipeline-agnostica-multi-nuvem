import abc

class IStorage(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def write(self, content: bytes, file_name: str, file_subpath: str = None) -> None:
        pass
    
    @abc.abstractmethod
    def read(self, file_name: str, file_subpath: str = None) -> bytes:
        pass
