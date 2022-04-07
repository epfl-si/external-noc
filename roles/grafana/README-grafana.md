# Grafana


## Install notes
http://docs.grafana.org/installation/docker/
http://docs.grafana.org/installation/configuration/

http://docs.grafana.org/auth/github/

http://docs.grafana.org/administration/provisioning/#example-datasource-config-file

### Let's encrypt
https://forum.cloud.switch.ch/t/calling-your-switchengines-instances-by-name-dns-and-other-mechanisms/20
(Note that this is not working without the CNAME: Requested name 86.119.37.70 is an IP address. The Let's Encrypt certificate authority will not issue certificates for a bare IP address.)

https://blog.stefanproell.at/2018/10/12/grafana-and-influxdb-with-ssl-inside-a-docker-container/

```
# apt install certbot

# dig +short ptr -x 86.119.37.70
fl-5-70.zhdk.cloud.switch.ch.

# certbot certonly --standalone --preferred-challenges http --renew-by-default -d fl-5-70.zhdk.cloud.switch.ch

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/fl-5-70.zhdk.cloud.switch.ch/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/fl-5-70.zhdk.cloud.switch.ch/privkey.pem
   Your cert will expire on 2019-06-24. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot
   again. To non-interactively renew *all* of your certificates, run
   "certbot renew"
 - Your account credentials have been saved in your Certbot
   configuration directory at /etc/letsencrypt. You should make a
   secure backup of this folder now. This configuration directory will
   also contain certificates and private keys obtained by Certbot so
   making regular backups of this folder is ideal.
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le


# ls -al /etc/letsencrypt/live/fl-5-70.zhdk.cloud.switch.ch/
total 12
drwxr-xr-x 2 root root 4096 Mar 26 14:15 .
drwx------ 3 root root 4096 Mar 26 14:15 ..
-rw-r--r-- 1 root root  543 Mar 26 14:15 README
lrwxrwxrwx 1 root root   52 Mar 26 14:15 cert.pem -> ../../archive/fl-5-70.zhdk.cloud.switch.ch/cert1.pem
lrwxrwxrwx 1 root root   53 Mar 26 14:15 chain.pem -> ../../archive/fl-5-70.zhdk.cloud.switch.ch/chain1.pem
lrwxrwxrwx 1 root root   57 Mar 26 14:15 fullchain.pem -> ../../archive/fl-5-70.zhdk.cloud.switch.ch/fullchain1.pem
lrwxrwxrwx 1 root root   55 Mar 26 14:15 privkey.pem -> ../../archive/fl-5-70.zhdk.cloud.switch.ch/privkey1.pem

```

### GitHub OAuth2 Authentication

To enable the GitHub OAuth2 you must register your application with GitHub. GitHub will generate a client ID and secret key for you to use.
Configure GitHub OAuth application

You need to create a GitHub OAuth application (you find this under the GitHub settings page). When you create the application you will need to specify a callback URL. Specify this as callback:

http://<my_grafana_server_name_or_ip>:<grafana_server_port>/login/github
http://86.119.37.70:3000/login/github
