from prettyconf import config


QUEUE_NAME = config('QUEUE_NAME', default='dronemapp_event_cloud')
CONFIG_FILE_PATH = config('CONFIG_FILE_PATH', default='config.yaml')
THREAD_POOL_SIZE = config('THREAD_POOL_SIZE', default=0, cast=int)

AWS_REGION = config('AWS_REGION')
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

TOKEN = config('TOKEN')
