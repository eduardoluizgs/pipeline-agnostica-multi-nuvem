import logging

from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient


class AzureStorage(object):

    def __init__(
            self,
            azure_container_name: str,
            azure_account_name: str,
            azure_account_key: str,
        ):
        service_client = DataLakeServiceClient(account_url=f"https://{azure_account_name}.dfs.core.windows.net", credential=azure_account_key)
        self.file_system_client = service_client.get_file_system_client(file_system=azure_container_name)

    def write(self, content: bytes, file_name: str, file_subpath: str = '/') -> None:
        try:
            directory_client = self.file_system_client.get_directory_client(file_subpath)
            file_client = directory_client.get_file_client(file_name)
            
            file_client.upload_data(content, overwrite=True)
            logging.info(f"Upload concluído para {file_name}")
        except Exception as e:
            logging.error(f"Erro ao fazer upload: {e}")

    def read(self, file_name: str, file_subpath: str = '/') -> bytes:
        try:
            directory_client = self.file_system_client.get_directory_client(file_subpath)
            file_client = directory_client.get_file_client(file_name)
            
            logging.info(f"Lendo arquivo {file_name}")
            return file_client.download_file().readall()
        except Exception as e:
            logging.err(f"Erro ao ler arquivo: {e}")
