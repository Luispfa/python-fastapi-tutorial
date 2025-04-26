from fastapi import FastAPI

app = FastAPI(
    title='FastApi FitCoding!!!',
    description='API tutorial con documentación personalizada',
    version='1.0.0',
    contact={
        'name': 'FitCoding Team',
        'email': 'contacto@email.com' 
    }
)


@app.get(
    "/" , 
    tags=['Home'],
    summary='Endpoint de bienvenida',
    description='Retorna una salida personalizada',
    response_description='Mensaje de bienvenida en texto plano'
)
def home():
 return "Hello world!!"