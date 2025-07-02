from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from api.crud import router as crud_router
from api.ai import router as ai_router

app = FastAPI(
    title='FastApi FitCoding!!!',
    description='Tutorial API with custom documentation',
    version='1.0.0',
    contact={
        'name': 'FitCoding Team',
        'email': 'contacto@email.com'
    }
)

app.include_router(crud_router)
app.include_router(ai_router)


@app.get(
    "/", 
    tags=["Home"],
    summary='Welcome Endpoint',
    description='Returns a personalized welcome message.',
    response_description='Welcome message in HTML format.'
)
def home():
    return HTMLResponse("<h1>Welcome to the FitCoding API!</h1>")
