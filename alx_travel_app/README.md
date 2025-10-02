# ALX Travel App (0x00)

A Django-based travel listings API project built as part of the ALX backend engineering journey.  
This repository includes models, serializers, seeders, and commands to populate the initial dataset.

## Overview

This project implements a backend for travel listings. It allows you to define travel-related models such as destinations and listings, serialize those models into JSON for API endpoints, and seed the database with initial data using a custom management command. The goal is to provide a foundation for a travel app’s backend — serving endpoints for travel offers, destinations, and more.

## Features

- Django ORM models for travel entities  
- REST-style serializers  
- Custom “seed” command to populate the database with starter data  
- SQLite (default) for quick setup  
- Easily extensible to support authentication, filters, or more advanced endpoints  

## Tech Stack

- **Python** (3.8+)  
- **Django**  
- **Django REST Framework** *(if enabled)*  
- **SQLite** by default (can be replaced with PostgreSQL or another database)  

## Project Structure
- **alx_travel_app/**: Project settings and URL configs  
- **listings/**: Models, serializers, views, and seeding logic  
- **manage.py**: Entry point for Django commands  
- **requirement.txt**: Project dependencies  

## Getting Started

### Prerequisites

- Python 3.8+  
- pip (Python package manager)  
- (Optional) virtualenv or venv for isolated environments  

### Installation

Clone the repository and set up the environment:

```bash
git clone https://github.com/IfeJayeola/alx_travel_app_0x00.git
cd alx_travel_app_0x00
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
pip install -r requirement.txt

Database & Migrations

Run migrations to set up the database schema:

python manage.py makemigrations
python manage.py migrate

Seeding Data

Populate the database with starter data:

python manage.py seed

Running the App

Start the development server:

python manage.py runserver

The app will be available at:
👉 http://127.0.0.1:8000/

Usage Examples

GET /api/destinations/ — List all destinations

GET /api/listings/ — List all travel listings

POST /api/listings/ — Create a new listing (if POST is supported)
