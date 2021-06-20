# makefile

all: abc/xyz
.PHONY: abc/xyz
abc/xyz 123/xaa 123/xbb:
	mkdir -p $(@:/%=)
	date > $@

sub1test/bar/alpha sub1test/bar/beta:
	mkdir -p $(@:/%=)
	date > $@

sub2test/bar/alpha:
	mkdir -p $(@:/%=)
	date > $@

sub3test/bar/alpha sub3test/foo/alpha:
	mkdir -p $(@:/%=)
	date > $@

sub4test/bar/alpha sub4test/bar/beta sub4test2/foo/gamma:
	mkdir -p $(@:/%=)
	date > $@
