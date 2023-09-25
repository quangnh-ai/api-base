from fastapi import (
    APIRouter,
    status
)

import uuid
import datetime
import json
import pytz

from api.entities.test_entities import (
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
        mq_and_cache.celecry_excutor.send_task(
            name="{app_name}.{task_name}".format(
                app_name=TEST_APP_NAME,
                task_name=TEST_TASK_NAME
            ),
            kwargs={
                'request_id': request_id,
                'data': data_result
            }
        )

        return TestPostResponse(
            request_id=request_id,
            status_code=status.HTTP_200_OK,
            message='Request is being processed',
            posted_time=post_time
        )
    except Exception as error:
        mq_and_cache.cache.set(
            request_id,
            json.dumps(
                TestResult(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    status="FAILED",
                    message="Failed when posting request: " + str(error)
                ).__dict__
            )
        )
        return TestPostResponse(
            request_id=request_id,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(error),
            posted_time=post_time
        )
    
@router.get("get/{request_id}")
async def get_result(*, request_id: str):
    try:
        data = mq_and_cache.cache.get(request_id)
        if data == None:
            return {
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "Request ID is not found"
            }
        data = json.loads(data)
        return data
    except Exception as error:
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": error
        }