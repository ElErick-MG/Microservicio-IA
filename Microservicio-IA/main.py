from fastapi import FastAPI
from routes import basic_routes, get_routes, post_routes

# Crear una instancia de FastAPI
app = FastAPI(
    title="API de Modelo IA",
    description="API para interactuar con modelos de inteligencia artificial",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Incluir las rutas
app.include_router(basic_routes.router)
app.include_router(get_routes.router)
app.include_router(post_routes.router)

# Ejecutar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
