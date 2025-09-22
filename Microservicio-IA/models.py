from pydantic import BaseModel
from typing import Optional, List

# Modelos de datos para las peticiones
class TextoEntrada(BaseModel):
    texto: str
    max_tokens: Optional[int] = 100
    temperatura: Optional[float] = 0.7

class RespuestaIA(BaseModel):
    respuesta: str
    tokens_usados: int
    modelo: str
    tiempo_procesamiento: float

class Conversacion(BaseModel):
    id: int
    texto: str
    respuesta: str
    fecha: str

class HistorialResponse(BaseModel):
    conversaciones: List[Conversacion]

class LoteResultado(BaseModel):
    indice: int
    texto_original: str
    resultado: Optional[dict] = None
    error: Optional[str] = None

class LoteResponse(BaseModel):
    resultados: List[LoteResultado]
    total_procesados: int

# Modelo para la predicción de exam_score
class ExamScorePrediction(BaseModel):
    study_hours_per_day: float
    social_media_hours: float
    netflix_hours: float
    attendance_percentage: float
    sleep_hours: float
    exercise_frequency: int
    mental_health_rating: int

    class Config:
        json_schema_extra = {
            "example": {
                "study_hours_per_day": 1.0,
                "social_media_hours": 5.0,
                "netflix_hours": 5.5,
                "attendance_percentage": 80.0,
                "sleep_hours": 7.0,
                "exercise_frequency": 4,
                "mental_health_rating": 8
            }
        }

class ExamScoreResponse(BaseModel):
    predicted_exam_score: float
    input_data: ExamScorePrediction
    model_used: str
    prediction_time: float 