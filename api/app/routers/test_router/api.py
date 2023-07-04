from fastapi import (
    APIRouter,
    HTTPException,
    status
)

import uuid
import datetime
import json

from routers.test_router.entities import (
    TestPostRequest, 
    TestPostResponse,
    TestResult
)
from utils.mq_and_cache import cache
from config.get_env import (
    TEST_TASK_TYPE,
    TEST_TASK_NAME
)

router = APIRouter()

@router.post("/post")
async def post_test(request: TestPostRequest) -> TestPostResponse:
    try:
        post_time = str(datetime.datetime.utcnow())
        request_id = str(
            uuid.uuid5(
                uuid.NAMESPACE_OID,
                TEST_TASK_TYPE + TEST_TASK_NAME + post_time
            )
        )

        data_result = TestResult(
            status_code=status.HTTP_200_OK,
            status="PROCESSING",
            start_time=post_time
        )
        data_result = json.dumps(data_result.__dict__)
        cache.set(
            request_id,
            json.dumps(data_result)
        )
        
        
        return TestPostResponse(
            id=request_id, 
            time=post_time,
            status_code=status.HTTP_200_OK,
            message='response has been send succesfully'
        )
    except Exception as e:
        return TestPostResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=e
        )

@router.get("/get/{request_id}")
async def get_result(*, request_id: str):
    try:
        data = cache.get(request_id)
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

