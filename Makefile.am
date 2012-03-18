SUBDIRS = completions doc helpers test

pkgdata_DATA = bash_completion

# Empty, but here just to get the compat dir created with install
compat_DATA =

profiledir = $(sysconfdir)/profile.d
profile_DATA = bash_completion.sh

pkgconfigdir = $(datadir)/pkgconfig
pkgconfig_DATA = bash-completion.pc

cmakeconfigdir = $(datadir)/cmake/$(PACKAGE)/
cmakeconfig_DATA = bash-completion-config.cmake \
                   bash-completion-config-version.cmake

bash_completion.sh: bash_completion.sh.in Makefile
	sed -e 's|@pkgdatadir[@]|$(pkgdatadir)|' <$(srcdir)/$@.in >$@

CLEANFILES = bash_completion.sh bash-completion.pc

EXTRA_DIST = CHANGES $(sysconf_DATA) $(pkgdata_DATA) bash_completion.sh.in \
        .dir-locals.el

install-data-hook:
	tmpfile=`mktemp $${TMPDIR:-/tmp}/bash_completion.XXXXXX` && \
	sed -e 's|=/etc/bash_completion\.d|=$(compatdir)|' \
	    $(DESTDIR)$(pkgdatadir)/bash_completion > $$tmpfile && \
	cat $$tmpfile > $(DESTDIR)$(pkgdatadir)/bash_completion && \
	sed -e 's|\$${prefix}|$(prefix)|' \
	    $(DESTDIR)$(datadir)/cmake/$(PACKAGE)/bash-completion-config.cmake \
	         > $$tmpfile && \
	cat $$tmpfile > \
	    $(DESTDIR)$(datadir)/cmake/$(PACKAGE)/bash-completion-config.cmake && \
	rm $$tmpfile
