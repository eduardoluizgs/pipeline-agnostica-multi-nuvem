import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

from tasks.extract_file_task import ExtractFileTask

from storages.aws_storage import AWSStorage
from storages.azure_storage import AzureStorage
from storages.disk_storage import DiskStorage


PIPELINE_NAME = 'pipeline_agnostica_multi_nuvem'

kwargs = dict(
    pipeline_name=PIPELINE_NAME,
    storage=DiskStorage(),
    # storage=AzureStorage(),
    # storage=AWSStorage(),
)

result = ExtractFileTask(**kwargs).execute()
