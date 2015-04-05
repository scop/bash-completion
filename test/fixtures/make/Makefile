$(info confuse: make)

CFLAGS=-MMD -MP
NAME := sample

.PHONY: all
all: $(NAME)

$(NAME): sample.c
	cc -o $@ $^

.PHONY: install
install: all
	mkdir -p /usr/bin
	install -m 755 $(NAME) /usr/bin

.PHONY: clean
clean:
	-rm -f $(NAME)

ifndef __BASH_MAKE_COMPLETION__
-include sample.d
endif
