# inside the project folder
uv init backend
cd backend
uv add django djangorestframework django-cors-headers
uv run python -m django startproject core .
uv run python manage.py startapp accounts
uv run python manage.py startapp campaigns