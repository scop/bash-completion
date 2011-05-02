SUBDIRS = completions test

data_DATA = bash_completion

profiledir = $(sysconfdir)/profile.d
profile_DATA = bash_completion.sh

bash_completion.sh: bash_completion.sh.in Makefile
	sed -e 's|@datadir[@]|$(datadir)|' <$(srcdir)/$@.in >$@

CLEANFILES = bash_completion.sh

EXTRA_DIST = CHANGES $(sysconf_DATA) bash_completion.sh.in

install-data-hook:
	tmpfile=`mktemp $${TMPDIR:-/tmp}/bash_completion.XXXXXX` && \
	sed -e 's|=/usr/share/bash-completion/|=$(datadir)/|' \
		-e 's|=/etc/bash_completion|=$(sysconfdir)/bash_completion|' \
		$(DESTDIR)$(datadir)/bash_completion > $$tmpfile && \
	mv $$tmpfile $(DESTDIR)$(datadir)/bash_completion
