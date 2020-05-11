SUBDIRS = t

EXTRA_DIST = config \
	     fixtures \
	     setup.cfg

all:
	$(MKDIR_P) tmp

CLEANFILES = \
	fixtures/make/extra_makefile

clean-local:
	$(RM) -rf tmp
