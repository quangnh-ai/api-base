from fastapi import APIRouter, status, Request

general_router = APIRouter()

@general_router.get('/health', status_code=status.HTTP_200_OK)
def get_health(request: Request):
    return {
        "message": "Everything is ok"
    }