# mysql(1) completion                                      -*- shell-script -*-

# @since 2.12
_comp_xfunc_mysql_compgen_character_sets()
{
    local -a charsets
    _comp_expand_glob charsets '/usr/share/m{ariadb,ysql}/charsets/!(Index).xml'
    charsets+=(utf8)
    charsets=("${charsets[@]##*/}")
    charsets=("${charsets[@]%.xml}")
    _comp_compgen -U charsets -- -W '"${charsets[@]}"' -X ''
}

# @deprecated 2.12
_mysql_character_sets()
{
    _comp_compgen -ax mysql character_sets "$@"
}

_comp_cmd_mysql()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    # Prefer `mysqlshow` in the same dir as the command
    local pathcmd
    pathcmd=$(type -P -- "$1") && local PATH=${pathcmd%/*}:$PATH

    local noargopts='!(-*|*[uDhSPeI]*)'
    # shellcheck disable=SC2254
    case $prev in
        --user | -${noargopts}u)
            _comp_compgen -- -u
            return
            ;;
        --database | -${noargopts}D)
            _comp_compgen_split -- "$(mysqlshow 2>/dev/null |
                command sed -ne '2d' -e 's/^|.\([^|]*\)|.*/\1/p')"
            return
            ;;

        --host | -${noargopts}h)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        --default-character-set)
            _comp_xfunc_mysql_compgen_character_sets
            return
            ;;

        --character-sets-dir | --ssl-capath)
            _comp_compgen_filedir -d
            return
            ;;
        --socket | -${noargopts}S)
            _comp_compgen_filedir sock
            return
            ;;
        --protocol)
            _comp_compgen -- -W 'tcp socket pipe memory'
            return
            ;;
        --defaults-file | --defaults-extra-file | --tee)
            _comp_compgen_filedir
            return
            ;;
        --ssl-ca | --ssl-cert)
            _comp_compgen_filedir '@(pem|cer|c?(e)rt)'
            return
            ;;
        --ssl-key)
            _comp_compgen_filedir '@(pem|key)'
            return
            ;;
        --port | --set-variable | --ssl-cipher | --connect_timeout | \
            --max_allowed_packet | --prompt | --net_buffer_length | --select_limit | \
            --max_join_size | --server-arg | --debug | --delimiter | --execute | --pager | \
            -${noargopts}[Pe])
            return
            ;;
        --help | --version | -${noargopts}[?IV])
            return
            ;;
    esac

    [[ $was_split ]] && return

    case $cur in
        --*)
            _comp_compgen_help
            _comp_compgen -a -- -W '--skip-comments --skip-ssl'
            [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
            return
            ;;

        # only complete long options
        -)
            compopt -o nospace
            COMPREPLY=(--)
            return
            ;;
    esac

    _comp_compgen_split -- "$(mysqlshow 2>/dev/null |
        command sed -ne '2d' -e 's/^|.\([^|]*\)|.*/\1/p')"
} &&
    complete -F _comp_cmd_mysql mysql

# ex: filetype=sh
