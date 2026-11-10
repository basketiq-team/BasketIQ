from fastapi import APIRouter
from core.config import get_settings

router = APIRouter()

@router.get("/App")
def get_app_name():
    settings = get_settings()
    return {"message" : f"welcome to {settings.app_name}"}