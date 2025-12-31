helpersdir = $(datadir)/$(PACKAGE)/helpers
helpers_DATA =

EXTRA_DIST = $(helpers_DATA)

install-data-local:
	$(MKDIR_P) $(DESTDIR)$(datadir)/bash-completion/$(subdir)

uninstall-local:
	-rmdir $(DESTDIR)$(datadir)/bash-completion/$(subdir)
