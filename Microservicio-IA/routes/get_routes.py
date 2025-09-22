from fastapi import APIRouter
from models import HistorialResponse, Conversacion

router = APIRouter()

@router.get("/historial", response_model=HistorialResponse)
async def obtener_historial():
    # Ejemplo de historial (en un caso real vendría de una base de datos)
    conversaciones_ejemplo = [
        Conversacion(
            id=1,
            texto="¿Cómo funciona el modelo de predicción?",
            respuesta="El modelo SVR predice exam_score basado en factores como horas de estudio, uso de redes sociales, etc.",
            fecha="2025-07-17"
        )
    ]
    return HistorialResponse(conversaciones=conversaciones_ejemplo)

@router.get("/modelo/info")
async def info_modelo():
    return {
        "nombre": "SVR Model",
        "descripcion": "Modelo de Support Vector Regression para predecir exam_score",
        "variables_entrada": [
            "study_hours_per_day",
            "social_media_hours", 
            "netflix_hours",
            "attendance_percentage",
            "sleep_hours",
            "exercise_frequency",
            "mental_health_rating"
        ],
        "variable_salida": "exam_score"
    }
