.PHONY: nothing
nothing:
	@cat Makefile |grep '.[P]HONY: '| sed 's/^.*: /make /' |sort

.PHONY: dev
dev:
	./ansible/nocsible -vv $(arg)

.PHONY: prod
prod:
	./ansible/nocsible --prod $(arg)
