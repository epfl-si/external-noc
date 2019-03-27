DOCKERLIST = $(docker ps -aq --filter 'ancestor=grafana/grafana')

docker-list:
	@echo $(value DOCKERLIST)

stop:
	docker stop $(value DOCKERLIST) 

rm:
	docker rm $(value DOCKERLIST)

clean: stop rm

run: clean
	docker run \
	  -d \
	  -p 443:3000 \
	  --name=idevfsd-grafana \
	  -v /root/grafana/conf/grafana.ini:/etc/grafana/grafana.ini \
	  -v /root/grafana/data:/var/lib/grafana \
	  -v /root/grafana/home/usr/share/grafana \
	  -v /root/grafana/logs:/var/log/grafana \
	  -v /root/grafana/plugins:/var/lib/grafana/plugins \
	  -v /root/grafana/provisioning:/etc/grafana/provisioning \
	  -v /root/grafana/ssl/fullchain.pem:/var/ssl/server.crt \
	  -v /root/grafana/ssl/privkey.pem:/var/ssl/server.key \
	  -e "GF_SERVER_ROOT_URL=https://exmple.com" \
	  -e "GF_SECURITY_ADMIN_PASSWORD=A_v3ry_v3ry-v3ry-s3cur3→p4sSw0rd" \
	  grafana/grafana

log:
	docker logs -f idevfsd-grafana

logs: log

redirect-clean:
	docker rm -f idevfsd-redirect

redirect-build:
	cd nginx-redirect; docker build . -t epflidevelop/idevfsd-redirect; cd ..

redirect-run:
	docker run -p 80:80 -p 3000:80 --name idevfsd-redirect -d epflidevelop/idevfsd-redirect
# docker run --net=host --name idevfsd-redirect -d epflidevelop/idevfsd-redirect


