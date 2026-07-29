<div align="center">

# 🤖 Microservicio IA - Predicción de Rendimiento Académico

### _API RESTful de Machine Learning para predecir calificaciones de exámenes (`exam_score`) mediante Support Vector Regression (SVR)_

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2.5.0-red?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.24.0-499885?style=for-the-badge&logo=uvicorn&logoColor=white)](https://www.uvicorn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

---

</div>

## 📌 Tabla de Contenidos

- [Descripción General](#-descripción-general)
- [Características Principales](#-características-principales)
- [Variables de Entrada del Modelo](#-variables-de-entrada-del-modelo)
- [Arquitectura y Estructura del Proyecto](#-arquitectura-y-estructura-del-proyecto)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Instalación y Configuración](#-instalación-y-configuración)
- [Ejecución del Servicio](#-ejecución-del-servicio)
- [Documentación y Endpoints de la API](#-documentación-y-endpoints-de-la-api)
- [Ejemplos de Uso](#-ejemplos-de-uso)
  - [1. Predicción Individual](#1-predicción-individual)
  - [2. Predicción en Lote (Batch)](#2-predicción-en-lote-batch)
  - [3. Consulta de Información del Modelo](#3-consulta-de-información-del-modelo)
- [Manejo de Errores y Tolerancia a Fallos](#-manejo-de-errores-y-tolerancia-a-fallos)
- [Licencia](#-licencia)

---

## 💡 Descripción General

**Microservicio-IA** es un microservicio back-end desarrollado con **FastAPI** que sirve predicciones en tiempo real sobre el rendimiento académico de estudiantes (`exam_score`).

El núcleo predictivo se apoya en un algoritmo de **Support Vector Regression (SVR)** junto con un preprocesador **MinMaxScaler** (serializados mediante `pickle`), los cuales analizan patrones comportamentales como horas diarias de estudio, consumo de entretenimiento, horas de sueño, porcentaje de asistencia y salud mental.

Diseñado para ser ligero, modular y de alto rendimiento, este servicio expone interfaces asíncronas HTTP, documentación Swagger interactiva y endpoints para inferencias individuales y por lotes (batch processing).

---

## ✨ Características Principales

- ⚡ **Inferencia en Tiempo Real**: Respuesta ultrarrápida mediante el modelo SVR preserializado.
- 📦 **Procesamiento por Lotes (Batch API)**: Endpoint `/predict/batch_exam_score` para procesar múltiples registros en una sola solicitud HTTP.
- 📊 **Escalado Automático de Características**: Integración transparente de `MinMaxScaler` para normalizar los datos de entrada antes de ser procesados por la SVR.
- 📐 **Validación Estricta de Datos**: Tipado y esquemas fuertemente validados en tiempo de ejecución con **Pydantic v2**.
- 🛠️ **Arquitectura Modular**: Separación limpia entre definición de modelos (`models.py`), lógica de rutas (`routes/`) y servidor principal (`main.py`).
- 📖 **Documentación OpenAPI Autogenerada**: Documentación interactiva en `/docs` (Swagger UI) y `/redoc` (ReDoc).
- 🩺 **Health Check & Metadatos**: Endpoints para verificar el estado de salud del sistema e inspeccionar las características del modelo en producción.

---

## 📊 Variables de Entrada del Modelo

El modelo predictivo evalúa **7 variables clave** relacionadas con el estilo de vida y hábitos de estudio del estudiante:

| Variable                |  Tipo   |     Unidad / Formato     | Descripción                                          |
| :---------------------- | :-----: | :----------------------: | :--------------------------------------------------- |
| `study_hours_per_day`   | `float` |        Horas/día         | Cantidad media de horas dedicadas al estudio al día. |
| `social_media_hours`    | `float` |        Horas/día         | Tiempo diario transcurrido en redes sociales.        |
| `netflix_hours`         | `float` |        Horas/día         | Tiempo diario viendo plataformas de streaming.       |
| `attendance_percentage` | `float` | Porcentaje (`0` - `100`) | Porcentaje global de asistencia a clases.            |
| `sleep_hours`           | `float` |       Horas/noche        | Promedio de horas de sueño por noche.                |
| `exercise_frequency`    |  `int`  |       Días/semana        | Frecuencia semanal de ejercicio físico (`0` a `7`).  |
| `mental_health_rating`  |  `int`  |   Escala (`1` - `10`)    | Autoevaluación del estado de salud mental.           |

### 🎯 Variable de Salida (Target)

- **`predicted_exam_score`** (`float`): Calificación estimada del examen generada por el modelo.

---

## 📂 Arquitectura y Estructura del Proyecto

El proyecto sigue una estructura limpia y fácil de mantener:

```text
Microservicio-IA/
│
├── Microservicio-IA/           # Código fuente del microservicio
│   ├── routes/                 # Capa de Enrutamiento (API Routers)
│   │   ├── __init__.py         # Inicializador del paquete routes
│   │   ├── basic_routes.py    # Rutas raíz y Health Check (`/`, `/health`)
│   │   ├── get_routes.py      # Rutas de consulta (`/historial`, `/modelo/info`)
│   │   └── post_routes.py     # Rutas de inferencia SVR (`/predict/...`)
│   │
│   ├── main.py                 # Punto de entrada de FastAPI y servidor Uvicorn
│   ├── models.py              # Esquemas de datos Pydantic (Request/Response)
│   ├── svr_model.pkl          # Modelo SVR entrenado y serializado
│   ├── min_max_scaler.pkl     # Escalador MinMaxScaler ajustado
│   └── requirements.txt       # Dependencias del proyecto
│
└── README.md                   # Documentación principal del repositorio
```

---

## 🛠️ Tecnologías Utilizadas

- **[Python 3.9+](https://www.python.org/)** - Lenguaje principal de desarrollo.
- **[FastAPI 0.104.1](https://fastapi.tiangolo.com/)** - Framework web asíncrono de alto rendimiento.
- **[Scikit-Learn 1.1+](https://scikit-learn.org/)** - Implementación de `SVR` y `MinMaxScaler`.
- **[Pydantic 2.5.0](https://docs.pydantic.dev/)** - Validación de datos y gestión de esquemas.
- **[NumPy](https://numpy.org/)** - Operaciones matriciales y manipulación de vectores de características.
- **[Uvicorn 0.24.0](https://www.uvicorn.org/)** - Servidor ASGI asíncrono para producción y desarrollo.

---

## 🚀 Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/ElErick-MG/Microservicio-IA.git
cd Microservicio-IA/Microservicio-IA
```

### 2. Crear y activar el entorno virtual

En Windows (PowerShell / CMD):

```bash
python -m venv .venv
.venv\Scripts\activate
```

En Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

## ⚙️ Ejecución del Servicio

Para iniciar la API en modo de desarrollo con recarga automática:

```bash
python main.py
```

O ejecutando directamente con Uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

La API estará disponible en **`http://localhost:8000`**.

---

## 📖 Documentación y Endpoints de la API

Una vez iniciada la aplicación, puedes acceder a la documentación interactiva en tu navegador:

- 🌐 **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- 📑 **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Tabla de Endpoints

| Método | Endpoint                    | Descripción                                 | Requiere Body |
| :----: | :-------------------------- | :------------------------------------------ | :-----------: |
| `GET`  | `/`                         | Comprobación de estado básico de la API     |      ❌       |
| `GET`  | `/health`                   | Monitoreo de salud del servicio (`healthy`) |      ❌       |
| `GET`  | `/modelo/info`              | Metadatos y variables del modelo SVR        |      ❌       |
| `GET`  | `/historial`                | Registro/historial de consultas             |      ❌       |
| `POST` | `/predict/exam_score`       | Predicción individual de calificación       |      ✅       |
| `POST` | `/predict/batch_exam_score` | Predicción en lote (múltiples estudiantes)  |      ✅       |
| `POST` | `/generar`                  | Endpoint legacy para procesamiento de texto |      ✅       |

---

## 🧪 Ejemplos de Uso

### 1. Predicción Individual

**Solicitud (`POST /predict/exam_score`):**

```bash
curl -X 'POST' \
  'http://localhost:8000/predict/exam_score' \
  -H 'Content-Type: application/json' \
  -d '{
    "study_hours_per_day": 4.5,
    "social_media_hours": 2.0,
    "netflix_hours": 1.5,
    "attendance_percentage": 92.0,
    "sleep_hours": 8.0,
    "exercise_frequency": 5,
    "mental_health_rating": 9
  }'
```

**Respuesta Exitosa (`200 OK`):**

```json
{
  "predicted_exam_score": 88.42,
  "input_data": {
    "study_hours_per_day": 4.5,
    "social_media_hours": 2.0,
    "netflix_hours": 1.5,
    "attendance_percentage": 92.0,
    "sleep_hours": 8.0,
    "exercise_frequency": 5,
    "mental_health_rating": 9
  },
  "model_used": "SVR (Support Vector Regression) + MinMaxScaler",
  "prediction_time": 0.0021
}
```

---

### 2. Predicción en Lote (Batch)

**Solicitud (`POST /predict/batch_exam_score`):**

```bash
curl -X 'POST' \
  'http://localhost:8000/predict/batch_exam_score' \
  -H 'Content-Type: application/json' \
  -d '[
    {
      "study_hours_per_day": 1.0,
      "social_media_hours": 5.0,
      "netflix_hours": 5.5,
      "attendance_percentage": 80.0,
      "sleep_hours": 7.0,
      "exercise_frequency": 4,
      "mental_health_rating": 8
    },
    {
      "study_hours_per_day": 6.0,
      "social_media_hours": 1.0,
      "netflix_hours": 0.5,
      "attendance_percentage": 98.0,
      "sleep_hours": 8.5,
      "exercise_frequency": 6,
      "mental_health_rating": 10
    }
  ]'
```

**Respuesta Exitosa (`200 OK`):**

```json
{
  "results": [
    {
      "index": 0,
      "input_data": {
        "study_hours_per_day": 1.0,
        "social_media_hours": 5.0,
        "netflix_hours": 5.5,
        "attendance_percentage": 80.0,
        "sleep_hours": 7.0,
        "exercise_frequency": 4,
        "mental_health_rating": 8
      },
      "predicted_exam_score": 62.15,
      "status": "success"
    },
    {
      "index": 1,
      "input_data": {
        "study_hours_per_day": 6.0,
        "social_media_hours": 1.0,
        "netflix_hours": 0.5,
        "attendance_percentage": 98.0,
        "sleep_hours": 8.5,
        "exercise_frequency": 6,
        "mental_health_rating": 10
      },
      "predicted_exam_score": 95.8,
      "status": "success"
    }
  ],
  "total_processed": 2,
  "processing_time": 0.0043,
  "model_used": "SVR (Support Vector Regression) + MinMaxScaler"
}
```

---

### 3. Consulta de Información del Modelo

**Solicitud (`GET /modelo/info`):**

```bash
curl -X 'GET' 'http://localhost:8000/modelo/info'
```

**Respuesta Exitosa (`200 OK`):**

```json
{
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
```

---

## 🛡️ Manejo de Errores y Tolerancia a Fallos

- **Model Loading Fallbacks**: En caso de indisponibilidad temporal del archivo del escalador (`min_max_scaler.pkl`), la API continúa operando advirtiendo en los logs sobre el uso de características no transformadas. Si el archivo `svr_model.pkl` falla al cargar, los endpoints de predicción devuelven HTTP `500 Internal Server Error` controlados con un mensaje explícito.
- **Validación Pydantic**: Si el formato de algún parámetro en la solicitud es inválido (ej. enviar texto en lugar de un flotante o faltar un campo obligatorio), FastAPI retorna automáticamente un error HTTP `422 Unprocessable Entity` detallando el campo defectuoso.

---

## 📄 Licencia

Este proyecto está bajo la Licencia **MIT**. Consulta el archivo `LICENSE` para obtener más detalles.

---

<div align="center">

Desarrollado por ElErick-MG - erickdevlml@gmail.com

</div>
