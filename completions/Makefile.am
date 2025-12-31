# We include all the files in the tarball

scriptfiles =

bashcompdir = $(datadir)/$(PACKAGE)/completions
bashcomp_DATA = README.md $(scriptfiles)

EXTRA_DIST = $(bashcomp_DATA)

symlinks: $(DATA)
.PHONY: symlinks

SETUP_SYMLINKS = $(srcdir)/../setup-symlinks.sh

all-local: ss = $(SETUP_SYMLINKS) .
all-local: symlinks

install-data-hook: ss = $(SETUP_SYMLINKS) $(DESTDIR)$(bashcompdir)
install-data-hook: symlinks

check-local:
	REPLY=0; \
	for file in $(scriptfiles); do \
		$${bashcomp_bash:-$${BASH:-bash}} \
			-O extglob -n $(srcdir)/$$file || REPLY=$$?; \
	done; \
	exit $$REPLY
