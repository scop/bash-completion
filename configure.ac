AC_PREREQ([2.60])
AC_INIT([bash-completion], [2.13.0]) dnl x-release-please-version
dnl tar-pax for portable UTF-8 handling
AM_INIT_AUTOMAKE([
    foreign dist-xz no-dist-gzip tar-pax -Wall -Wno-portability -Werror
])
AC_PROG_LN_S
AC_PROG_MKDIR_P
AC_PROG_SED
AC_ARG_WITH([pytest],[  --with-pytest=executable],[PYTEST="$withval"])
if test "x$PYTEST" = x; then
    AC_CHECK_PROGS([PYTEST],[pytest pytest-3],[pytest])
fi
AC_CONFIG_FILES([
Makefile
completions/Makefile
doc/Makefile
helpers/Makefile
test/Makefile
test/fallback/Makefile
test/fallback/completions/Makefile
test/t/Makefile
test/t/unit/Makefile
])
AC_OUTPUT
