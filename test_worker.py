from celery import Celery
import json

celecry_excutor = Celery(
    broker='amqp://guest:guest@localhost:5672/',
    backend='redis://localhost:6379/0'
)

celecry_excutor.send_task(
    name="test.test_task",
    kwargs={
        "request_id": "0497f634-5104-566c-b202-41f9a5eb778c",
        "data": json.dumps({
            "status_code": 200,
            "status": "PROCESSING",
            "message": "request is being processed",
            "start_time": "111",
            "end_time": "1111",
            "result": None
        })
    }
)