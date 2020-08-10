ANSIBLE_MODULES=nickjj.docker

.PHONY: nothing
nothing:
	@cat Makefile |grep '.[P]HONY: '| sed 's/^.*: /make /' |sort

.PHONY: dev
dev: install eyaml_key
	ansible-playbook playbook.yml -i hosts-dev.yml $(arg)

.PHONY: prod
prod: install eyaml_key
	ansible-playbook playbook.yml -i hosts-prod.yml $(arg)

.PHONY: eyaml_key
eyaml_key: keys/private_key.pkcs7.pem
	[ -f $< ] || [ -L $< ] && [ -e $< ]

keys/private_key.pkcs7.pem: /keybase/team/epfl_ressenti/private_key.pkcs7.pem
	[ -f $< ]
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
