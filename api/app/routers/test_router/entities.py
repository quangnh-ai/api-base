from pydantic import BaseModel

## -------------------Entities for Test API------------------- ##
class TestPostRequest(BaseModel):
    test_code: int
    test_str: str

class TestPostResponse(BaseModel):
    request_id: str = None
    post_time: str = None
    status_code: int
    message: str

class TestResult(BaseModel):
    status_code: int = None
    status: str = None
    message: str = None
    start_time: str = None
    end_time: str = None
    result: list = None