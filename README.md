# Band Website

# Introduction

This project is designed to demonstrate how to build and run the application using Python `venv` and Docker.

# Prerequisites

Ensure you have the following installed:
- Python 3.x
- Docker
- Git

# Setup

Create and activate a virtual environment using venv:
python -m venv venv
.\venv\Scripts\activate

Install the required dependencies:
pip install -r requirements.txt

Run the application:
python manage.py runserver

Building and Running with Docker

Build the Docker image:
docker build -t consolidation ./
docker run -p 8000:8000 consolidation
