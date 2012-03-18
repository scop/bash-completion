AC_PREREQ([2.60])
AC_INIT([bash-completion], [2.1])
AM_INIT_AUTOMAKE([foreign dist-bzip2 no-dist-gzip -Wall -Werror])
AC_PROG_LN_S
AC_PROG_MKDIR_P
AC_SUBST(compatdir, $sysconfdir/bash_completion.d)
AC_CONFIG_FILES([
Makefile
completions/Makefile
doc/Makefile
helpers/Makefile
test/Makefile
bash-completion.pc
bash-completion-config.cmake
bash-completion-config-version.cmake
])
AC_OUTPUT
