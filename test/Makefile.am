DEJATOOL = completion install unit
AM_RUNTESTFLAGS = --outdir log --ignore $(PACKAGE).log

SUBDIRS = t

EXTRA_DIST = completion \
	     config \
	     fixtures \
	     lib \
	     unit

all:
	$(MKDIR_P) log tmp

clean-local:
	rm -rf log tmp

AUTOMAKE_OPTIONS = dejagnu
