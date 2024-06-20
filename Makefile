up:
	docker compose up --build

down:
	docker compose down

exec:
	docker exec -it temki_backend /bin/sh

execdb:
	docker exec -it temki_postgres psql -U postgres -d temki

compile:
	docker exec -it backend python manage.py compilemessages
