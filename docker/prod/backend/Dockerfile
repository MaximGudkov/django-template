FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_HOME=/usr/src/backend

WORKDIR $APP_HOME


RUN pip install --no-cache-dir -e .[local]  # !!!
