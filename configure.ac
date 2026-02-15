AC_PREREQ([2.60])
AC_INIT([bash-completion], [2.17.0]) dnl x-release-please-version
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

AC_CANONICAL_HOST

install_bsd=
install_freebsd=
install_solaris=
case ${host_os} in
    *bsd*)
        install_bsd=yes
        case ${host_os} in
            *freebsd*)
                install_freebsd=yes ;;
        esac ;;
    *solaris*)
        install_solaris=yes ;;
esac

AM_CONDITIONAL([BSD], [test "${install_bsd}" = yes])
AM_CONDITIONAL([FREEBSD], [test "${install_freebsd}" = yes])
AM_CONDITIONAL([SOLARIS], [test "${install_solaris}" = yes])

AC_CONFIG_FILES([
Makefile
completions/Makefile
completions-core/Makefile
completions-fallback/Makefile
doc/Makefile
helpers/Makefile
helpers-core/Makefile
startup/Makefile
startup-core/Makefile
test/Makefile
test/t/Makefile
test/t/unit/Makefile
])
AC_OUTPUT
