VERSION:=$(shell date +%Y%m%d)
RPMTOP:=$(shell rpm --eval '%_topdir')
ARCH:=$(shell rpm --eval '%_arch')
DIST:=$(shell rpm --eval '%dist')
BRANCH=master

rpm: openssl-gost-engine-$(VERSION)-1$(DIST).$(ARCH).rpm
	
openssl-gost-engine-$(VERSION)-1$(DIST).$(ARCH).rpm: $(RPMTOP)/RPMS/$(ARCH)/openssl-gost-engine-$(VERSION)-1$(DIST).$(ARCH).rpm
	cp $^ $@

$(RPMTOP)/RPMS/$(ARCH)/openssl-gost-engine-$(VERSION)-1$(DIST).$(ARCH).rpm: $(RPMTOP)/SOURCES/openssl-gost-engine-$(VERSION).tar.bz2 $(RPMTOP)/SPECS/openssl-gost-engine.spec
	mkdir -p $(RPMTOP)/RPMS/$(ARCH) || true
	mkdir -p $(RPMTOP)/SRPMS
	CXX=/bin/true rpmbuild -ba $(RPMTOP)/SPECS/openssl-gost-engine.spec

$(RPMTOP)/SPECS/openssl-gost-engine.spec: openssl-gost-engine.spec
	mkdir -p $(RPMTOP)/SPECS || true
	sed 's/^Version:	.*$$/Version:	$(VERSION)/' $^>  $@

$(RPMTOP)/SOURCES/openssl-gost-engine-$(VERSION).tar.bz2: engine/README.md
	mkdir -p $(RPMTOP)/SOURCES || true
	cd engine; git pull
	cd engine; git archive --format tar --prefix=openssl-gost-engine-$(VERSION)/ $(BRANCH) > $@
	
engine/README.md:
	git clone https://github.com/gost-engine/engine.git


envtest:
	:	ARCH=$(ARCH)
	:	VERSION=$(VERSION)
	:	RPMTOP=$(RPMTOP)
