.PHONY: nothing
nothing:
	@cat Makefile |grep '.[P]HONY: '| sed 's/^.*: /make /' |sort

.PHONY: dev
dev: eyaml_key
	./ansible/nocsible -vv $(arg)

.PHONY: prod
prod: eyaml_key
	./ansible/nocsible --prod $(arg)

.PHONY: eyaml_key
eyaml_key: ansible/keys/private_key.pkcs7.pem
	[ -f $< ] || [ -L $< ] && [ -e $< ]

ansible/keys/private_key.pkcs7.pem: /keybase/team/epfl_ressenti/private_key.pkcs7.pem
	[ -f $< ]
	ln -s $< $@
