$(info confuse: make)

CFLAGS=-MMD -MP
NAME := sample

.PHONY: all
all: $(NAME)

$(NAME): sample.o

.INTERMEDIATE: sample.o
sample.o: sample.c

.PHONY: install
install: all
	mkdir -p /usr/bin
	install -m 755 $(NAME) /usr/bin

.PHONY: clean
clean:
	-rm -f $(NAME)

.test_passes:
	./sample >/dev/null
	touch ^@

.cache/.1:
	touch $@

.cache/.2:
	touch $@

.cache/1:
	touch $@

.cache/2:
	touch $@

ifndef __BASH_MAKE_COMPLETION__
-include sample.d
endif

VARIABLE_LOOKS_A_BIT_LIKE_A_TARGET := fooled-you
extra_makefile:
	touch $@
include extra_makefile
