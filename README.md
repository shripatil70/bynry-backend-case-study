
# Bynry Backend Engineering Intern – Case Study (Final)

## Overview
A backend service for managing utility consumers, meters, readings, and billing.
Designed to align with Bynry SMART360 platform.

## Tech Stack
- FastAPI
- Python
- SQLite
- SQLAlchemy

## Features
- Consumer registration
- Meter assignment
- Meter readings
- Automated billing
- Swagger API docs

## Run Locally
pip install -r requirements.txt
uvicorn app.main:app --reload

## Docker
docker build -t bynry-backend .
docker run -p 8000:8000 bynry-backend
