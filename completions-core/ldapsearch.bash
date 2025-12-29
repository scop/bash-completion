# bash completion for openldap                             -*- shell-script -*-

_comp_cmd_ldapsearch__ldap_uris()
{
    _comp_compgen -- -W 'ldap:// ldaps://'
}

_comp_cmd_ldapsearch__ldap_protocols()
{
    _comp_compgen -- -W '2 3'
}

_comp_cmd_ldapsearch()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*h)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        -*H)
            _comp_cmd_ldapsearch__ldap_uris
            return
            ;;
        -*T)
            _comp_compgen_filedir -d
            return
            ;;
        -*[fy])
            _comp_compgen_filedir
            return
            ;;
        -*s)
            _comp_compgen -- -W 'base one sub children'
            return
            ;;
        -*a)
            _comp_compgen -- -W 'never always search find'
            return
            ;;
        -*P)
            _comp_cmd_ldapsearch__ldap_protocols
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        _comp_compgen -a -- -W '-MM -ZZ'
    fi
} &&
    complete -F _comp_cmd_ldapsearch ldapsearch

_comp_cmd_ldapadd()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*h)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        -*H)
            _comp_cmd_ldapsearch__ldap_uris
            return
            ;;
        -*[Sfy])
            _comp_compgen_filedir
            return
            ;;
        -*P)
            _comp_cmd_ldapsearch__ldap_protocols
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        _comp_compgen -a -- -W '-MM -ZZ'
    fi
} &&
    complete -F _comp_cmd_ldapadd ldapadd ldapmodify

_comp_cmd_ldapdelete()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*h)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        -*H)
            _comp_cmd_ldapsearch__ldap_uris
            return
            ;;
        -*[fy])
            _comp_compgen_filedir
            return
            ;;
        -*P)
            _comp_cmd_ldapsearch__ldap_protocols
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        _comp_compgen -a -- -W '-MM -ZZ'
    fi
} &&
    complete -F _comp_cmd_ldapdelete ldapdelete

_comp_cmd_ldapcompare()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*h)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        -*H)
            _comp_cmd_ldapsearch__ldap_uris
            return
            ;;
        -*y)
            _comp_compgen_filedir
            return
            ;;
        -*P)
            _comp_cmd_ldapsearch__ldap_protocols
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        _comp_compgen -a -- -W '-MM -ZZ'
    fi
} &&
    complete -F _comp_cmd_ldapcompare ldapcompare

_comp_cmd_ldapmodrdn()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*h)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        -*H)
            _comp_cmd_ldapsearch__ldap_uris
            return
            ;;
        -*[fy])
            _comp_compgen_filedir
            return
            ;;
        -*P)
            _comp_cmd_ldapsearch__ldap_protocols
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        _comp_compgen -a -- -W '-ZZ -MM'
    fi
} &&
    complete -F _comp_cmd_ldapmodrdn ldapmodrdn

_comp_cmd_ldapwhoami()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*h)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        -*H)
            _comp_cmd_ldapsearch__ldap_uris
            return
            ;;
        -*[fy])
            _comp_compgen_filedir
            return
            ;;
        -*P)
            _comp_cmd_ldapsearch__ldap_protocols
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        _comp_compgen -a -- -W '-MM -ZZ'
    fi
} &&
    complete -F _comp_cmd_ldapwhoami ldapwhoami

_comp_cmd_ldappasswd()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*h)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        -*H)
            _comp_cmd_ldapsearch__ldap_uris
            return
            ;;
        -*[tTy])
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        _comp_compgen -a -- -W '-MM -ZZ'
    fi
} &&
    complete -F _comp_cmd_ldappasswd ldappasswd

# ex: filetype=sh
