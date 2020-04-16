# include .env
# export $(shell sed 's/=.*//' .env)

TRAEFIK_DIR={{ traefik.install_path }}

.PHONY: nothing
nothing:
	@cat Makefile |grep '.[P]HONY: '| sed 's/^.*: /make /' |sort

.PHONY: traefik
traefik:
	cd $(TRAEFIK_DIR) && make up

.PHONY: up
up:
	traefik
	docker-compose up -d

.PHONY: up_blackbox-exporter
up_blackbox-exporter:
	cd ./blackbox-exporter && make up
	
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
	read -p "Would you like to purge containers, images, volumes and networks ? [Yy]: " -n 1 -r; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		docker container rm -f -v $(docker container ls -a -q) ; \
		docker image rm -f $(docker image ls -a -q) ; \
		docker volume rm $(docker volume ls -q) ; \
		docker network rm $(docker network ls -q) ; \
	fi