# include .env
# export $(shell sed 's/=.*//' .env)

TRAEFIK_DIR={{ traefik.install_path }}

.PHONY: traefik
traefik:
	cd $(TRAEFIK_DIR) && make up

.PHONY: up
up: traefik
	docker-compose up -d

.PHONY: down
down:
	docker-compose down --remove-orphans

.PHONY: pull
pull:
	docker-compose pull --include-deps

.PHONY: logs
logs:
	docker-compose logs -f

.PHONY: ps
ps:
	docker-compose ps

.PHONY: box
box:
	docker run -i -t --network={{traefik.network}} busybox

.PHONY: testc2c
testc2c:
	curl --globoff -u {{frontend.htpass | regex_search('([^:]*:[^ ]*)') }} 'https://prometheus.{{ frontend.domain }}/federate?match[]={__name__=~%22^{{ c2c.prefix }}:.*%22}'

.PHONY: purge
purge:
	docker container rm -f -v $(docker container ls -a -q)
	docker image rm -f $(docker image ls -a -q)
	docker volume rm $(docker volume ls -q)
	docker network rm $(docker network ls -q)
