#!/bin/bash
#Petit script pour démarrer tout le binz
#zf190527.1531


cd ansible
ansible-playbook -i hosts.yml playbook.yml

echo -e "



ne PAS oublier quand tout est terminé de faire


rm ./ansible/keys/private_key.pkcs7.pem


"


