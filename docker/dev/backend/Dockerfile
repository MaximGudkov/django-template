FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_HOME=/usr/src/backend

WORKDIR $APP_HOME


RUN apk add --update --no-cache curl

COPY ./backend/setup.cfg ./backend/pyproject.toml $APP_HOME
COPY ./backend/requirements ./requirements
RUN pip install -e .[local]

COPY  ./backend $APP_HOME

COPY  ./docker/dev/backend/entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
