from fastapi import (
    APIRouter,
    HTTPException,
    status
)

import uuid
import datetime
import json
import pytz

from routers.test_router.entities import (
    TestPostRequest, 
    TestPostResponse,
    TestResult
)
from utils import mq_and_cache
from config.get_env import (
    TEST_APP_NAME,
    TEST_TASK_NAME
)

router = APIRouter()

@router.post("/post")
async def post_test(request: TestPostRequest) -> TestPostResponse:
    post_time = str(
        datetime.datetime.now(
            pytz.timezone('Asia/Ho_Chi_Minh')
        )
    )
    request_id = str(
        uuid.uuid5(
            uuid.NAMESPACE_OID,
            TEST_APP_NAME + TEST_TASK_NAME + post_time
        )
    )
    try:
        data_result = TestResult(
            status_code=status.HTTP_200_OK,
            status="PROCESSING",
            start_time=post_time
        )
        data_result = json.dumps(data_result.__dict__)
        mq_and_cache.cache.set(
            request_id,
            data_result
        )

        print('---------------------------------')
        print("{app_name}.{task_name}".format(
                app_name=TEST_APP_NAME,
                task_name=TEST_TASK_NAME
            ))
        print('---------------------------------')

        mq_and_cache.celecry_excutor.send_task(
            name="test.test_task",
            kwargs={
                'request_id': request_id,
                'data': data_result
            }
        )
        
        return TestPostResponse(
            request_id=request_id, 
            post_time=post_time,
            status_code=status.HTTP_200_OK,
            message='response has been send succesfully'
        )
    
    except Exception as e:
        mq_and_cache.cache.set(
            request_id,
            json.dumps(
                TestResult(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    status="FAILED",
                    message="Failed when posting request: " + str(e)
                ).__dict__
            )
        )
        return TestPostResponse(
            request_id=request_id,
            post_time=post_time,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e)
        )
    
@router.get("/get/{request_id}")
async def get_result(*, request_id: str):
    try:
        data = mq_and_cache.cache.get(request_id)
        if data == None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='request id is not found'
            )
        data = json.loads(data)
        return data
    except Exception as e:
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": e
        }

