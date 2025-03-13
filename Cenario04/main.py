import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

from storages.storage_factory import StorageFactory
from tasks.extract_file_task import ExtractFileTask


PIPELINE_NAME = 'pipeline_agnostica_multi_nuvem'

# TIP : As configurações abaixo podem ser adicionado a nível de ambiente, deixando o código mais flexível.

# storage do tipo DISK
AZURE_STORAGE_CONFIG = dict(
    storage_type='disk'
)
storage = StorageFactory.get_storage(**AZURE_STORAGE_CONFIG)

# storage do tipo AZURE
# AZURE_STORAGE_CONFIG = dict(
#     storage_type='azure',
#     azure_container_name='pipeline-agnostica-multi-nuvem',
#     azure_account_name='',
#     azure_account_key='',
# )
# storage = StorageFactory.get_storage(**AZURE_STORAGE_CONFIG)

# storage do tipo AWS
# AWS_STORAGE_CONFIG = dict(
#     storage_type='aws',
#     aws_bucket_name='pipeline-agnostica-multi-nuvem',
#     aws_access_key_id='',
#     aws_secret_access_key='',
#     aws_region_name='us-east-2'
# )
# storage = StorageFactory.get_storage(**AWS_STORAGE_CONFIG)

kwargs = dict(
    pipeline_name=PIPELINE_NAME,
    storage=storage
)
result = ExtractFileTask(**kwargs).execute()
