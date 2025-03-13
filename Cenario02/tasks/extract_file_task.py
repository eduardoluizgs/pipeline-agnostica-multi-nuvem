import boto3
import requests

from hdfs import InsecureClient


class ExtractFileTask(object):

    def __init__(
            self,
            pipeline_name: str,
            storage_type: str
        ):
        self.pipeline_name = pipeline_name
        self.storage_type = storage_type

    def execute(self):

        response = requests.get('https://www.gov.br/receitafederal/dados/municipios.csv')
        if not response.status_code == 200:
            raise Exception('Erro ao baixar o arquivo!')

        content = response.content

        # grava arquivo baixo para o data lake em DISCO
        # with open('data/municipios.csv', 'wb') as f:
        #     f.write(content)

        # TODO : Este código não está funcional, foi colocado aqui apenas para fins de exemplo
        
        # grava arquivo baixo para o data lake em HDFS
        if self.storage_type == 'hdfs':
            
            client = InsecureClient('http://namenode_host:50070', user='hadoop')
            with client.write('/user/hadoop/testfile.txt', overwrite=True) as writer:
                writer.write(content.encode())

        # grava arquivo baixo para o data lake na AWS S3
        elif self.storage_type == 'aws':
            self.s3_client = boto3.client('s3')
            self.s3_client.upload_file('<file_name>', '<bucket_name>', '<file_name>')

        # retorna um erro caso o tipo de storage não estvier dentro do esperado
        else:
            raise Exception(f'Tipo de storage não localizado: {self.storage_type}')

        return True
