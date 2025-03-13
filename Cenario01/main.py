from tasks.extract_file_task import ExtractFileTask


PIPELINE_NAME = 'pipeline_agnostica_multi_nuvem'

kwargs = dict(
    pipeline_name=PIPELINE_NAME
)

result = ExtractFileTask(**kwargs).execute()
