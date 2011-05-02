AC_PREREQ([2.59])
AC_INIT([bash-completion], [1.99])
AM_INIT_AUTOMAKE([foreign dist-bzip2 no-dist-gzip -Wall -Werror])
AC_SUBST(datadir, $datarootdir/bash-completion)
AC_SUBST(bashcompdir, $datadir/completions)
AC_SUBST(helpersdir, $datadir/helpers)
AC_SUBST(compatdir, $sysconfdir/bash_completion.d)
AC_CONFIG_FILES([Makefile completions/Makefile completions/helpers/Makefile test/Makefile])
AC_OUTPUT
