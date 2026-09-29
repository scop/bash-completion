all: fluff
fluff:
	touch fluff

common-proc:
	echo $(OUCH)
.PHONY: common-proc

foobar: OUCH = glitch
foobar: common-proc

barbaz: OUCH = switch
barbaz: common-proc
