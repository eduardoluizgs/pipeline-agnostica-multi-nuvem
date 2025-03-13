from storages.aws_storage import AWSStorage
from storages.azure_storage import AzureStorage
from storages.disk_storage import DiskStorage


class StorageFactory(object):

    @classmethod
    def get_storage(cls, **kwargs):

        storage_type = kwargs.pop('storage_type', None)
        if not storage_type:
            raise Exception('O parâmetro `storage_type` deve ser informado!')

        if storage_type == 'disk':
            return DiskStorage(**kwargs)
        elif storage_type == 'aws':
            return AWSStorage(**kwargs)
        elif storage_type == 'azure':
            return AzureStorage(**kwargs)
        else:
            raise Exception(f'Tipo de storage `{storage_type}` inválido!')
