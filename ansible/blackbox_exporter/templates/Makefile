TRAEFIK_DIR={{ traefik.install_path }}

.PHONY: traefik
traefik:
	cd $(TRAEFIK_DIR) && make up

.PHONY: up
up: traefik
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
