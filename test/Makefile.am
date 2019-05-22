AUTOMAKE_OPTIONS = dejagnu
DEJATOOL = completion install unit
AM_RUNTESTFLAGS = --outdir log --ignore $(PACKAGE).log

SUBDIRS = t

EXTRA_DIST = completion \
	     config \
	     fixtures \
	     lib \
	     setup.cfg \
	     unit

all:
	$(MKDIR_P) log tmp

CLEANFILES = \
	fixtures/make/extra_makefile

clean-local:
	$(RM) -rf log tmp
