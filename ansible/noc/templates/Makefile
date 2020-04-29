# include .env
# export $(shell sed 's/=.*//' .env)
#zf200429.1758

TRAEFIK_DIR={{ traefik.install_path }}
BBE_DIR={{ bbe.install_path }}

.PHONY: nothing
nothing:
	@cat Makefile |grep '.[P]HONY: '| sed 's/^.*: /make /' |sort

.PHONY: traefik_up
traefik_up:
	cd $(TRAEFIK_DIR) && make up

.PHONY: traefik_down
traefik_down:
	cd $(TRAEFIK_DIR) && make down

.PHONY: blackbox-exporter_up
blackbox-exporter_up:
	cd $(BBE_DIR) && make up

.PHONY: blackbox-exporter_down
blackbox-exporter_down:
	cd $(BBE_DIR) && make down

.PHONY: up
up: traefik_up blackbox-exporter_up
	docker-compose up -d
	docker container ls -a

.PHONY: down
down: traefik_down blackbox-exporter_down
	docker-compose down --remove-orphans
	docker container ls -a

.PHONY: pull
pull:
	docker-compose pull --include-deps

.PHONY: logs
logs:
	docker-compose logs -f

.PHONY: ps
ps:
	docker container ls -a

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
