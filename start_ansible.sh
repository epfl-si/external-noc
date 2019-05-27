#!/bin/bash
#Petit script pour démarrer tout le binz
#zf190527.1604


cd ansible
ansible-playbook -i hosts.yml playbook.yml



echo -e "

il faut redémarrer le service prometheus avec:

ssh root@prometheus.idev-fsd.ml \"cd /root/anoc2/noc ; docker-compose restart prometheus\"

docker-compose restart prometheus

ne PAS oublier quand tout est terminé de faire


rm ./ansible/keys/private_key.pkcs7.pem



Pour ajouter la machine à surveiller:

nano ~/external-noc/ansible/idevfsd-noc/vars/main.yml

"


