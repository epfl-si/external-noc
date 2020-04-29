# Listes de commandes souvent utilisées pour le dev du NOC
#zf200429.1755


# Accès via ssh
```
sshg czufferey@noc-tst.idev-fsd.ml
sudo -sE
cd /srv/noc
```


# Accès à Grafana
```
https://grafana-tst.idev-fsd.ml/login
https://grafana.idev-fsd.ml/login
```


# Copier le contenu du fichier *Makefile* dans le clipboard du MAC
**ATTENTION AUX PASSWORDS QUI POURRAIENT S'Y TROUVER**
```
sshg czufferey@noc-tst.idev-fsd.ml cat /srv/noc/Makefile | pbcopy
sshg czufferey@noc-tst.idev-fsd.ml cat /srv/noc/traefik/Makefile | pbcopy
sshg czufferey@noc-tst.idev-fsd.ml cat /srv/noc/blackbox-exporter/Makefile | pbcopy

```





