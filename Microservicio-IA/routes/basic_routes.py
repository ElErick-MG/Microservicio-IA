from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "API de Modelo IA funcionando correctamente"}

@router.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API is running"}
