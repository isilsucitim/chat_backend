from fastapi import APIRouter
import routes.auth

router = APIRouter()
router.include_router(auth.router)
