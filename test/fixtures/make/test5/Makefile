# `.NOTINTERMEDIATE' (GNU make 4.4) and `.WAIT' are special targets, so -- like
# the other names in the extractor's special-target skip list -- they must not
# be offered as completion candidates (e.g. `make .NOT<TAB>' / `make .WA<TAB>').
#
# `.WAIT' is a parallel-build barrier used as a prerequisite (`a .WAIT b').  The
# GNU make manual documents creating an actual empty `.WAIT' target for
# portability with older make; that rule shows up as a target block in
# `make -npq', so it has to be filtered too.

.PHONY: all
all: a .WAIT b

a:
	@echo $@
b:
	@echo $@

.WAIT:

.NOTINTERMEDIATE:
