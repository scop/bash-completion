SUBDIRS = completions helpers test

pkgdata_DATA = bash_completion

profiledir = $(sysconfdir)/profile.d
profile_DATA = bash_completion.sh

pkgconfigdir = $(datadir)/pkgconfig
pkgconfig_DATA = bash-completion.pc

bash_completion.sh: bash_completion.sh.in Makefile
	sed -e 's|@pkgdatadir[@]|$(pkgdatadir)|' <$(srcdir)/$@.in >$@

CLEANFILES = bash_completion.sh bash-completion.pc

EXTRA_DIST = CHANGES $(sysconf_DATA) $(pkgdata_DATA) bash_completion.sh.in \
        .dir-locals.el

install-data-hook:
	tmpfile=`mktemp $${TMPDIR:-/tmp}/bash_completion.XXXXXX` && \
	sed -e 's|=/etc/bash_completion\.d|=$(sysconfdir)/bash_completion.d|' \
		$(DESTDIR)$(pkgdatadir)/bash_completion > $$tmpfile && \
	mv $$tmpfile $(DESTDIR)$(pkgdatadir)/bash_completion
