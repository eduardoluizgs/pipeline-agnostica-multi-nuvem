import os


class DiskStorage(object):

    def __init__(self):
        pass

    def write(self, content: bytes, file_name: str, file_subpath: str = None) -> None:
        file_path = os.path.join(os.getcwd(), file_subpath, file_name)
        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))
        with open(file_path, 'wb') as f:
            f.write(content)

    def read(self, file_name: str, file_subpath: str = None) -> bytes:
        file_path = os.path.join(os.getcwd(), file_subpath, file_name)
        if not os.path.exists(file_path):
            raise Exception(f'Arquivo não existe {file_path}')
        with open(os.path.join(file_subpath, file_name), 'rb') as f:
            return f.read()
