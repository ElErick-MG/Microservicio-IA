from fastapi import APIRouter, HTTPException
from models import ExamScorePrediction, ExamScoreResponse, TextoEntrada, RespuestaIA
import pickle
import numpy as np
import time
import os

router = APIRouter()

# Cargar el modelo SVR y el escalador al iniciar
model_path = "svr_model.pkl"
scaler_path = "min_max_scaler.pkl"

try:
    with open(model_path, 'rb') as f:
        svr_model = pickle.load(f)
    print("Modelo SVR cargado exitosamente")
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    svr_model = None

try:
    with open(scaler_path, 'rb') as f:
        min_max_scaler = pickle.load(f)
    print("Escalador MinMaxScaler cargado exitosamente")
except Exception as e:
    print(f"Error al cargar el escalador: {e}")
    print("⚠️ Continuando sin escalador - las predicciones pueden ser incorrectas")
    min_max_scaler = None

@router.post("/predict/exam_score", response_model=ExamScoreResponse)
async def predict_exam_score(data: ExamScorePrediction):
    """
    Predice el exam_score basado en las variables de entrada usando el modelo SVR
    """
    if svr_model is None:
        raise HTTPException(status_code=500, detail="Modelo no disponible")
    
    try:
        start_time = time.time()
        
        # Preparar los datos de entrada en el orden correcto
        input_features = np.array([[
            data.study_hours_per_day,
            data.social_media_hours,
            data.netflix_hours,
            data.attendance_percentage,
            data.sleep_hours,
            data.exercise_frequency,
            data.mental_health_rating
        ]])
        
        # Escalar los datos si tenemos el escalador
        if min_max_scaler is not None:
            input_features_scaled = min_max_scaler.transform(input_features)
            print(f"📊 Datos originales: {input_features[0]}")
            print(f"📊 Datos escalados: {input_features_scaled[0]}")
        else:
            input_features_scaled = input_features
            print("⚠️ Usando datos sin escalar - puede afectar la precisión")
        
        # Hacer la predicción
        prediction = svr_model.predict(input_features_scaled)[0]
        
        prediction_time = time.time() - start_time
        
        return ExamScoreResponse(
            predicted_exam_score=float(prediction),
            input_data=data,
            model_used="SVR (Support Vector Regression)" + (" + MinMaxScaler" if min_max_scaler else " sin escalador"),
            prediction_time=prediction_time
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la predicción: {str(e)}")

@router.post("/predict/batch_exam_score")
async def predict_batch_exam_score(data_list: list[ExamScorePrediction]):
    """
    Realiza predicciones en lote para múltiples conjuntos de datos
    """
    if svr_model is None:
        raise HTTPException(status_code=500, detail="Modelo no disponible")
    
    try:
        start_time = time.time()
        results = []
        
        for i, data in enumerate(data_list):
            try:
                input_features = np.array([[
                    data.study_hours_per_day,
                    data.social_media_hours,
                    data.netflix_hours,
                    data.attendance_percentage,
                    data.sleep_hours,
                    data.exercise_frequency,
                    data.mental_health_rating
                ]])
                
                # Escalar los datos si tenemos el escalador
                if min_max_scaler is not None:
                    input_features_scaled = min_max_scaler.transform(input_features)
                else:
                    input_features_scaled = input_features
                
                prediction = svr_model.predict(input_features_scaled)[0]
                
                results.append({
                    "index": i,
                    "input_data": data.dict(),
                    "predicted_exam_score": float(prediction),
                    "status": "success"
                })
                
            except Exception as e:
                results.append({
                    "index": i,
                    "input_data": data.dict(),
                    "predicted_exam_score": None,
                    "status": "error",
                    "error": str(e)
                })
        
        total_time = time.time() - start_time
        
        return {
            "results": results,
            "total_processed": len(data_list),
            "processing_time": total_time,
            "model_used": "SVR (Support Vector Regression)" + (" + MinMaxScaler" if min_max_scaler else " sin escalador")
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en predicción por lotes: {str(e)}")

# Ruta legacy para compatibilidad
@router.post("/generar", response_model=RespuestaIA)
async def generar_respuesta(entrada: TextoEntrada):
    """
    Ruta de ejemplo para generar respuestas (mantener compatibilidad)
    """
    start_time = time.time()
    
    respuesta = f"Procesando: {entrada.texto[:50]}..."
    processing_time = time.time() - start_time
    
    return RespuestaIA(
        respuesta=respuesta,
        tokens_usados=len(entrada.texto.split()),
        modelo="Sistema de ejemplo",
        tiempo_procesamiento=processing_time
    )
