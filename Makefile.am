SUBDIRS = completions test

sysconf_DATA = bash_completion

profiledir = $(sysconfdir)/profile.d
profile_DATA = bash_completion.sh

bash_completion.sh: bash_completion.sh.in Makefile
	sed -e 's|@sysconfdir[@]|$(sysconfdir)|' <$(srcdir)/$@.in >$@

CLEANFILES = bash_completion.sh

EXTRA_DIST = CHANGES $(sysconf_DATA) bash_completion.sh.in
