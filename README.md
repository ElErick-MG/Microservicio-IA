# API de Predicción de Exam Score - SVR Model

## Descripción
Esta API utiliza un modelo SVR (Support Vector Regression) con MinMaxScaler para predecir el `exam_score` basado en variables de entrada relacionadas con hábitos de estudio y estilo de vida.

## Variables de Entrada
| Variable | Tipo | Descripción |
|----------|------|-------------|
| `study_hours_per_day` | float | Horas de estudio por día |
| `social_media_hours` | float | Horas en redes sociales |
| `netflix_hours` | float | Horas viendo Netflix |
| `attendance_percentage` | float | Porcentaje de asistencia |
| `sleep_hours` | float | Horas de sueño |
| `exercise_frequency` | int | Frecuencia de ejercicio |
| `mental_health_rating` | int | Calificación de salud mental |

## Instalación y Ejecución

### 1. Activar el entorno virtual
```bash
.venv\Scripts\activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar la aplicación
```bash
python main.py
```

La API estará disponible en: `http://localhost:8000`

## Endpoints Principales

- `GET /health` - Verificación del estado de la API
- `POST /predict/exam_score` - Predicción individual
- `GET /docs` - Documentación Swagger UI

## Ejemplo de Uso

```bash
curl -X POST "http://localhost:8000/predict/exam_score" \
     -H "Content-Type: application/json" \
     -d '{
       "study_hours_per_day": 1.0,
       "social_media_hours": 5.0,
       "netflix_hours": 5.5,
       "attendance_percentage": 80.0,
       "sleep_hours": 7.0,
       "exercise_frequency": 4,
       "mental_health_rating": 8
     }'
```

## Swagger UI
Documentación interactiva disponible en: `http://localhost:8000/docs`

## Estructura del Proyecto
```
├── main.py                 # Aplicación principal FastAPI
├── models.py              # Modelos Pydantic
├── svr_model.pkl          # Modelo SVR entrenado
├── min_max_scaler.pkl     # Escalador MinMaxScaler
├── requirements.txt       # Dependencias
├── routes/
│   ├── basic_routes.py    # Rutas básicas
│   ├── get_routes.py      # Rutas GET
│   └── post_routes.py     # Rutas POST (predicciones)
└── .venv/                 # Entorno virtual
```

## Tecnologías
- FastAPI
- Pydantic
- Scikit-learn
- NumPy
- Uvicorn
