# bash completion for Postgresql                           -*- shell-script -*-

_comp_cmd_psql__databases()
{
    # -w was introduced in 8.4, https://launchpad.net/bugs/164772
    # "Access privileges" in output may contain linefeeds, hence the NF > 1
    _comp_compgen_split -- "$(psql -XAtqwlF $'\t' 2>/dev/null |
        _comp_awk 'NF > 1 { print $1 }')"
}

_comp_cmd_psql__users()
{
    # -w was introduced in 8.4, https://launchpad.net/bugs/164772
    _comp_compgen_split -- "$(psql -XAtqwc 'select usename from pg_user' \
        template1 2>/dev/null)" ||
        _comp_compgen -- -u
}

# createdb(1) completion
#
_comp_cmd_createdb()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[hUOpDET]*)'
    # shellcheck disable=SC2254
    case $prev in
        --host | -${noargopts}h)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        --username | --owner | -${noargopts}[UO])
            _comp_cmd_psql__users
            return
            ;;
        --help | --version | --port | --tablespace | --encoding | --template | \
            -${noargopts}[pDET])
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        _comp_cmd_psql__databases
    fi
} &&
    complete -F _comp_cmd_createdb createdb

# createuser(1) completion
#
_comp_cmd_createuser()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[pchU]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | --port | --connection-limit | -${noargopts}[pc])
            return
            ;;
        --host | -${noargopts}h)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        --username | -${noargopts}U)
            _comp_cmd_psql__users
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_createuser createuser

# dropdb(1) completion
#
_comp_cmd_dropdb()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[hU]*)'
    # shellcheck disable=SC2254
    case $prev in
        --host | -${noargopts}h)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        --username | -${noargopts}U)
            _comp_cmd_psql__users
            return
            ;;
        --help | --version)
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        _comp_cmd_psql__databases
    fi
} &&
    complete -F _comp_cmd_dropdb dropdb

# dropuser(1) completion
#
_comp_cmd_dropuser()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[phU]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | --port | -${noargopts}p)
            return
            ;;
        --host | -${noargopts}h)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        --username | -${noargopts}U)
            _comp_cmd_psql__users
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        _comp_cmd_psql__users
    fi
} &&
    complete -F _comp_cmd_dropuser dropuser

# psql(1) completion
#
_comp_cmd_psql()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[hUdofLcFpPRTv]*)'
    # shellcheck disable=SC2254
    case $prev in
        --host | -${noargopts}h)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        --username | -${noargopts}U)
            _comp_cmd_psql__users
            return
            ;;
        --dbname | -${noargopts}d)
            _comp_cmd_psql__databases
            return
            ;;
        --output | --file | --log-file | -${noargopts}[ofL])
            _comp_compgen_filedir
            return
            ;;
        --help | --version | --command | --field-separator | --port | --pset | \
            --record-separator | --table-attr | --set | --variable | \
            -${noargopts}[?VcFpPRTv])
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        # return list of available options
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        # return list of available databases
        _comp_cmd_psql__databases
    fi
} &&
    complete -F _comp_cmd_psql psql

# ex: filetype=sh
