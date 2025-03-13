import os
import logging

from storages.storage_interface import IStorage


class AzureStorage(IStorage):

    def __init__(self):
        pass

    def write(self, content: bytes, file_name: str, file_subpath: str = None) -> None:
        logging.info(f'Escrevendo arquivo para AZURE: {os.path.join(os.getcwd(), file_subpath, file_name)}')

    def read(self, file_name: str, file_subpath: str = None) -> bytes:
        logging.info(f'Lendo arquivo a partir da AZURE: {os.path.join(os.getcwd(), file_subpath, file_name)}')
