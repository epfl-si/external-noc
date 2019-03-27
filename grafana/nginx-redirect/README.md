# nginx-redirect

Redirect to the DNS name of the server, e.g. 86.119.37.70 → https://fl-5-70.zhdk.cloud.switch.ch

## Info

* redirect-clean:
	`docker rm -f idevfsd-redirect`

* redirect-build:
	`cd nginx-redirect; docker build . -t epflidevelop/idevfsd-redirect; cd ..`

* redirect-run:
	`docker run -p 80:80 -p 3000:80 --name idevfsd-redirect -d epflidevelop/idevfsd-redirect`
