# Proyecto 06 — Backend: REST API + Firebase Realtime Database (Django)

Backend desarrollado con **Django** y **Django REST Framework (DRF)**, integrando **Firebase Realtime Database** como base de datos no relacional. El proyecto incluye:

- **Homepage (SSR Dashboard):** página principal renderizada en servidor que muestra métricas y registros recientes desde Firebase.
- **Demo REST API:** API de demostración para operaciones CRUD.
- **Landing API:** API conectada a Firebase para registrar y consultar *leads*.

---

## Sitio desplegado con PythonAnywhere

- **URL:** `https://manuelmatute.pythonanywhere.com/`

---

## Rúbrica 

- `homepage` 
- `demo_rest_api` 
- `landing_api` 
- `despliegue` 

---

## Estructura del proyecto

Aplicaciones principales:

- `homepage` — Dashboard SSR en `/`
- `demo_rest_api` — API demo en `/demo/rest/api/`
- `landing_api` — API Firebase en `/landing/api/`

---

## Endpoints

### 1) Homepage (SSR Dashboard)
- `GET /`  
  Muestra:
  - **Número total de respuestas**
  - **Últimos registros** (colección `leads` en Firebase)

---

### 2) Demo REST API (CRUD)

- `GET /demo/rest/api/index/` — lista recursos
- `POST /demo/rest/api/index/` — crea recurso
- `PUT /demo/rest/api/<id>/` — reemplaza recurso por `id`
- `PATCH /demo/rest/api/<id>/` — actualiza parcialmente por `id`
- `DELETE /demo/rest/api/<id>/` — eliminación lógica por `id`

> Para obtener un `<id>`, realiza primero un `GET` en `/demo/rest/api/index/` y copia el campo `id` de un elemento.

---

### 3) Landing API (Firebase Realtime Database)

- `GET /landing/api/index/` — devuelve todos los registros desde Firebase (`leads`)
- `POST /landing/api/index/` — crea un registro en Firebase agregando `timestamp`

**Ejemplo de POST** (Content-Type: `application/json`):

```json
{
  "name": "Prueba01",
  "email": "prueba01@test.com"
}
