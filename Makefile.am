SUBDIRS = completions doc helpers test

pkgdata_DATA = bash_completion

# Empty, but here just to get the compat dir created with install
compatdir = $(sysconfdir)/bash_completion.d
compat_DATA = bash_completion.d/000_bash_completion_compat.bash

profiledir = $(sysconfdir)/profile.d
profile_DATA = bash_completion.sh

pkgconfigdir = $(datadir)/pkgconfig
pkgconfig_DATA = bash-completion.pc

cmakeconfigdir = $(datadir)/cmake/$(PACKAGE)/
cmakeconfig_DATA = bash-completion-config.cmake \
                   bash-completion-config-version.cmake

%: %.in Makefile
	$(SED) \
		-e 's|@prefix[@]|$(prefix)|' \
		-e 's|@datadir[@]|$(datadir)|' \
		-e 's|@sysconfdir[@]|$(sysconfdir)|' \
		-e 's|@PACKAGE[@]|$(PACKAGE)|' \
		-e 's|@VERSION[@]|$(VERSION)|' \
		<$(srcdir)/$@.in >$@

CLEANFILES = bash_completion.sh bash-completion.pc \
	bash-completion-config.cmake bash-completion-config-version.cmake

EXTRA_DIST = CHANGELOG.md $(pkgdata_DATA) bash_completion.sh.in .dir-locals.el \
	.editorconfig README.md CONTRIBUTING.md pyproject.toml .perltidyrc \
	.shellcheckrc bash-completion.pc.in bash-completion-config.cmake.in \
	bash-completion-config-version.cmake.in setup-symlinks.sh \
	$(compat_DATA)

install-data-hook:
	tmpfile=`mktemp $${TMPDIR:-/tmp}/bash_completion.XXXXXX` && \
	$(SED) -e 's|-/etc/bash_completion\.d|-$(compatdir)|' \
	    $(DESTDIR)$(datadir)/$(PACKAGE)/bash_completion >$$tmpfile && \
	cat $$tmpfile >$(DESTDIR)$(datadir)/$(PACKAGE)/bash_completion && \
	rm $$tmpfile
