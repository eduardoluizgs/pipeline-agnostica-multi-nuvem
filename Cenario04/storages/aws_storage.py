import os
import boto3
import logging
import tempfile

from botocore.exceptions import NoCredentialsError


class AWSStorage(object):

    def __init__(
            self,
            aws_bucket_name: str,
            aws_access_key_id: str,
            aws_secret_access_key: str,
            aws_region_name: str
        ):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region_name
        )
        self.bucket_name = aws_bucket_name

    def write(self, content: bytes, file_name: str, file_subpath: str = None) -> None:
        try:
            with tempfile.NamedTemporaryFile(delete=True) as temp_file:
                temp_file.write(content)
                self.s3_client.upload_file(temp_file.name, self.bucket_name, os.path.join(file_subpath, file_name))
                logging.info(f"Upload concluído: {file_name} para {self.bucket_name}/{file_name}")
        except NoCredentialsError:
            logging.error("Erro: Credenciais do AWS não encontradas.")
            raise
        except Exception as e:
            logging.error(f"Erro ao fazer upload: {e}")
            raise

    def read(self, file_name: str, file_subpath: str = None) -> bytes:
        try:
            response = self.s3_client.get_object(Bucket=self.bucket_name, Key=os.path.join(file_subpath, file_name))
            content = response['Body'].read()
            logging.info(f"Lendo do arquivo {file_name}")
            return content
        except NoCredentialsError:
            logging.error("Erro: Credenciais do AWS não encontradas.")
            raise
        except Exception as e:
            logging.error(f"Erro ao ler arquivo: {e}")
            raise
