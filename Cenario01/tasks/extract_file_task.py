import requests


class ExtractFileTask(object):

    def __init__(
            self,
            pipeline_name: str
        ):
        self.pipeline_name = pipeline_name

    def execute(self):

        response = requests.get('https://www.gov.br/receitafederal/dados/municipios.csv')
        if not response.status_code == 200:
            raise Exception('Erro ao baixar o arquivo!')

        content = response.content

        # grava arquivo baixo para o data lake em DISCO
        with open('data/municipios.csv', 'wb') as f:
            f.write(content)

        return True
