import os



#=========================================================================
#                          API INFORMATION 
#=========================================================================
API_TITLE = os.environ['API_TITLE']
API_OPENAPI_URL = os.environ['API_OPENAPI_URL']
API_DOCS_URL = os.environ['API_DOCS_URL']
API_REDOC_URL = os.environ['API_REDOC_URL']

#=========================================================================
#                          REDIS INFORMATION 
#=========================================================================
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = int(os.environ['REDIS_PORT'])
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
REDIS_DB = int(os.environ['REDIS_DB'])
REDIS_LINK = "redis://:{password}@{hostname}:{port}/{db}".format(
    hostname=REDIS_HOST,
    password=REDIS_PASSWORD,
    port=str(REDIS_PORT),
    db=str(REDIS_DB)
)

# #=========================================================================
# #                          BROKER INFORMATION 
# #=========================================================================
# RABBITMQ_LINK = "amqp://{user}:{password}@{hostname}:{port}/{vhost}".format(
#     user=os.environ['RABBITMQ_USER'],
#     password = os.environ['RABBITMQ_PASSWORD'],
#     hostname=os.environ['RABBITMQ_HOST'],
#     port=os.environ['RABBITMQ_PORT'],
#     vhost=os.environ['RABBITMQ_VHOST']
# )

#=========================================================================
#                          TEST TASK INFORMATION 
#=========================================================================
TEST_TASK_TYPE=os.environ["TEST_TASK_TYPE"]
TEST_TASK_NAME=os.environ["TEST_TASK_NAME"]