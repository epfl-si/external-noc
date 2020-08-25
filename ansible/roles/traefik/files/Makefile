#canary200429.1514

.PHONY: up
up: acme.json network
	docker-compose up -d

.PHONY: down
down:
	docker-compose down --remove-orphans

.PHONY: logs
logs:
	docker-compose logs -f

.PHONY: ps
ps:
	docker-compose ps

.PHONY: network
network:
	docker network ls --format "{{.ID}} {{.Name}}" --filter "name=traefik"  | grep -q ' traefik$$' || docker network create --subnet=192.168.129.0/24 traefik

.PHONY: clean
clean: down
	docker network inspect traefik --format='{{ range $$key, $$value := .Containers}}{{ $$key }} {{ end }}' | xargs docker stop | xargs docker rm
	docker network rm traefik

acme.json:
	touch $@ && chmod 600 $@
