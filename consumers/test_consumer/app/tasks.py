import json
import datetime
import pytz
from celery import (
    Celery,
    Task
)

from utils import mq_and_cache
from config import get_env

app = Celery(
    get_env.TEST_APP_NAME,
    broker=get_env.RABBITMQ_LINK,
    backend=get_env.REDIS_LINK
)


@app.task(
    name="{app_name}.{task_name}".format(
        app_name=get_env.TEST_APP_NAME,
        task_name=get_env.TEST_TASK_NAME
    )
)
def test_task(
    request_id: str,
    data: bytes
):  
    data = json.loads(data)
    print('--------------------------')
    print('Start processing')
    print('--------------------------')
    try:
        data['result'] = [
            {
                "staff": "1",
                "a": "2"
            },
            {
                "staff": "1",
                "a": "2"
            }
        ]
        data['end_time'] = str(
            datetime.datetime.now(
                pytz.timezone('Asia/Ho_Chi_Minh')
            )
        )
        data['status'] = "SUCCESSED"
        data['status_code'] = 200
        data['message'] = "OK"
        mq_and_cache.cache.set(
            request_id,
            json.dumps(data)
        )
    except Exception as e:
        data['status_code'] = 500
        data['status'] = 'FAILED'
        data['message'] = str(e)
        data['end_time'] = str(
            datetime.datetime.now(
                pytz.timezone('Asia/Ho_Chi_Minh')
            )
        )
        mq_and_cache.cache.set(
            request_id,
            json.dumps(data)
        )
