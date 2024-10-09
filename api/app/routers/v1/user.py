from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from core.database.schemas.user import User
from core.database.crud import get_user_crud
from core.database import get_database_session

user_router = APIRouter()
user_crud = get_user_crud()

@user_router.get(
    "/get_by_id/{id}",
    name="Get User By ID",
    response_model=User,
    status_code=status.HTTP_200_OK, 
    response_model_exclude_none=True
)
async def get_user_by_id(*, id: int, database_session = Depends(get_database_session)):
    user = user_crud.get_user_by_id(database_session=database_session, id=id)
    if user:
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No User Found"
        )

@user_router.get(
    "/get_by_user_name/{user_name}",
    name="Get User By Name",
    response_model=User,
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_user_by_user_name(*, user_name: str, database_session=Depends(get_database_session)):
    user = user_crud.get_user_by_name(database_session=database_session, user_name=user_name)
    if user:
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No User Found"   
        )
    
@user_router.get(
    "/get_by_user_email/{email}",
    name="Get User By Email",
    response_model=User,
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_user_by_email(*, email: str, database_session=Depends(get_database_session)):
    user = user_crud.get_user_by_email(database_session=database_session, email=email)
    if user:
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No User Found"
        )

@user_router.get(
    "/get_all_users/",    
    name="Get User By Email",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_all_users(*, database_session=Depends(get_database_session)):
    user = user_crud.get_all_users(database_session=database_session)
    return user

# @user_router.get