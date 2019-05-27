ANSIBLE_MODULES=nickjj.docker

.PHONY: dev
dev: install keys/private_key.pkcs7.pem
	ansible-playbook playbook.yml -i hosts-dev.yml

.PHONY: prod
prod: install keys/private_key.pkcs7.pem
	ansible-playbook playbook.yml -i hosts-prod.yml

keys/private_key.pkcs7.pem: /keybase/team/epfl_ressenti/private_key.pkcs7.pem
	ln -s $< $@


# -------------------------------------------------------------

ANSIBLE_MODDIRS=$(addprefix $(HOME)/.ansible/roles/,$(ANSIBLE_MODULES))

.PHONY: install
install: ansible $(ANSIBLE_MODDIRS) keys/private_key.pkcs7.pem

# TODO: this should install ansible itself...
ansible:
	@echo "This should install ansible but, for the moment, we just fail if it is not installed..."
	which ansible

$(ANSIBLE_MODDIRS): $(HOME)/.ansible/roles/
	ansible-galaxy install $(notdir $@)

$(HOME)/.ansible/roles/:
	mkdir -p $@
