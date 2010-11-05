DEJATOOL = completion install unit
AM_RUNTESTFLAGS = --outdir log

EXTRA_DIST = completion \
	     config \
	     fixtures \
	     lib \
	     unit

all:
	$(mkdir_p) log tmp

distclean-local:
	rm -rf log tmp
