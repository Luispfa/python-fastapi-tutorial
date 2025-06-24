# 🐍 FastAPI Demo / Demostración FastAPI

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Modern%20Web%20Framework-009688?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Required-blue?logo=docker)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI%20Server-critical?logo=uvicorn)

## Bilingual README / README Bilingüe

This repository is bilingual. Below you will find the English version followed by the Spanish version.  
Este repositorio es bilingüe. A continuación encontrarás la versión en inglés seguida de la versión en español.

---

<div style="display: block; text-align: center;">
<img src="youtube-banner.png" alt="@fitCoding - Python - FastAPI" style="max-width: 30%; float: left; margin-right: 20px;">

  <div style="max-width: 70%; text-align: left;">
    <strong style="font-size: 30px; font-weight: bold;">Tutorial "Python - FastAPI"</strong>
    <br>
    <span style="font-size: 24px;">Software Development with Python 3.11.9</span>
    <br>
    <span style="font-size: 24px;">Desarrollo de Software con Python 3.11.9</span>
  </div>
</div>
<p></p>

---

# Python FastAPI Tutorial

This repository showcases a demonstration project built with **Python** and **FastAPI**, focusing on clean architecture, high performance, and scalability. It serves as a practical example for building modern APIs using FastAPI's powerful features.

## 🚀 Features

- **FastAPI**: A modern, high-performance web framework for building APIs with Python 3.7+.
- **Uvicorn**: A lightning-fast ASGI server implementation, using `uvloop` and `httptools`.
- **Dockerized**: Simplified setup and deployment using Docker and Docker Compose.
- **Interactive Documentation**: Automatically generated API docs with Swagger UI and ReDoc.

## 📦 Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Luispfa/python-fastapi-tutorial.git
   cd python-fastapi-tutorial
   ```

2. Build and run the Docker container:

   ```bash
   docker-compose up --build
   ```

   The application will be accessible at [http://localhost:8000](http://localhost:8000).

## 📚 API Documentation

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

These interfaces provide interactive exploration and testing of the API endpoints.

## 🧪 Example Endpoints

- `GET /`: Returns a welcome message.

Feel free to extend the API with additional routes and functionalities as needed.

## 🛠️ Project Structure

```
python-fastapi/
├── docker/
|    ├── Dockerfile
|    └── requirements.txt
├── main.py
└── docker-compose.yml
```

- `main.py`: Entry point of the FastAPI application.
- `Dockerfile`: Defines the Docker image for the application.
- `docker-compose.yml`: Configures the Docker services.

---

# Tutorial de Python con FastAPI

Este repositorio presenta un proyecto de demostración construido con **Python** y **FastAPI**, enfocándose en una arquitectura limpia, alto rendimiento y escalabilidad. Sirve como un ejemplo práctico para construir APIs modernas utilizando las potentes características de FastAPI.

## 🚀 Características

- **FastAPI**: Un framework web moderno y de alto rendimiento para construir APIs con Python 3.7+.
- **Uvicorn**: Un servidor ASGI extremadamente rápido, utilizando `uvloop` y `httptools`.
- **Dockerizado**: Configuración y despliegue simplificados usando Docker y Docker Compose.
- **Documentación Interactiva**: Documentación de la API generada automáticamente con Swagger UI y ReDoc.

## 📦 Comenzando

### Requisitos Previos

- Tener [Docker](https://www.docker.com/get-started) instalado en tu máquina.

### Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/Luispfa/python-fastapi-tutorial.git
   cd python-fastapi-tutorial
   ```

2. Construye y ejecuta el contenedor Docker:

   ```bash
   docker-compose up --build
   ```

   La aplicación estará accesible en [http://localhost:8000](http://localhost:8000).

## 📚 Documentación de la API

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

Estas interfaces proporcionan una exploración y prueba interactivas de los endpoints de la API.

## 🧪 Endpoints de Ejemplo

- `GET /`: Devuelve un mensaje de bienvenida.

Siéntete libre de extender la API con rutas y funcionalidades adicionales según sea necesario.

## 🛠️ Estructura del Proyecto

```
python-fastapi/
├── docker/
|    ├── Dockerfile
|    └── requirements.txt
├── main.py
└── docker-compose.yml
```

- `main.py`: Punto de entrada de la aplicación FastAPI.
- `Dockerfile`: Define la imagen Docker para la aplicación.
- `docker-compose.yml`: Configura los servicios Docker.

