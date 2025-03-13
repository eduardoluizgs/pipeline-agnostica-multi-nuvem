import logging
import requests


class ExtractFileTask(object):

    def __init__(
            self,
            pipeline_name: str,
            storage: object
        ):
        self.pipeline_name = pipeline_name
        self.storage = storage

    def execute(self):

        response = requests.get('https://www.gov.br/receitafederal/dados/municipios.csv')
        if not response.status_code == 200:
            raise Exception('Erro ao baixar o arquivo!')

        content = response.content

        logging.info('Realizando gravação do Arquivo!')
        self.storage.write(content, 'municipios.csv', 'data')

        logging.info('Realizando leitura do Arquivo!')
        content = self.storage.read('municipios.csv', 'data')

        return True
