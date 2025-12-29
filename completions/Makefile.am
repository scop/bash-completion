# We include all the files in the tarball

bashcompdir = $(datadir)/$(PACKAGE)/completions
bashcomp_DATA =

symlinks: $(DATA)
.PHONY: symlinks

SETUP_SYMLINKS = $(srcdir)/../setup-symlinks.sh

all-local: ss = $(SETUP_SYMLINKS) .
all-local: symlinks

install-data-hook: ss = $(SETUP_SYMLINKS) $(DESTDIR)$(bashcompdir)
install-data-hook: symlinks

check-local:
	REPLY=0; \
	for file in $(bashcomp_DATA); do \
		$${bashcomp_bash:-$${BASH:-bash}} \
			-O extglob -n $(srcdir)/$$file || REPLY=$$?; \
	done; \
	exit $$REPLY

install-data-local:
	$(MKDIR_P) $(DESTDIR)$(datadir)/bash-completion/$(subdir)

uninstall-local:
	-rmdir $(DESTDIR)$(datadir)/bash-completion/$(subdir)
