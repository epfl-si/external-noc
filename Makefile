TRAEFIK_DIR=traefik

.PHONY: traefik
traefik:
	cd $(TRAEFIK_DIR) && make up

.PHONY: up
up: .env traefik
	docker-compose up -d

.PHONY: down
down:
	docker-compose down

.PHONY: logs
logs:
	docker-compose logs -f

.PHONY: ps
ps:
	docker-compose ps

.PHONY: box
box:
	docker run -i -t busybox