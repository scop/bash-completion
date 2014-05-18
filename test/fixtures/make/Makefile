$(info confuse: make)

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
