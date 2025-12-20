outdir ?= .

srpm:
	sudo dnf install -y git
	$(eval VERSION := $(shell grep "Version:" extension-manager.spec | awk '{print $$2}'))
	git archive --format=tar.gz --prefix=extension-manager-$(VERSION)/ -o extension-manager-$(VERSION).tar.gz HEAD
	rpmbuild -bs --define "_sourcedir ." --define "_srcrpmdir $(outdir)" extension-manager.spec
