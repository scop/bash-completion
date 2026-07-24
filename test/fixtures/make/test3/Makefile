# CMake "Unix Makefiles" style: phony targets whose names use `/' as a naming
# convention, not a directory boundary.  `make -p' marks them phony, so the
# completion offers them as-is instead of collapsing `install' into `install/'
# or dropping the plain `MyProgram' in favor of only `MyProgram/fast'.
#
#   - single-child case: `MyProgram' alongside `MyProgram/fast'
#   - multi-child case:  `install' alongside `install/local' and `install/strip'

all: MyProgram
.PHONY: all

MyProgram MyProgram/fast:
	@echo $@
.PHONY: MyProgram MyProgram/fast

clean clean/fast:
	@echo $@
.PHONY: clean clean/fast

install install/local install/strip:
	@echo $@
.PHONY: install install/local install/strip
