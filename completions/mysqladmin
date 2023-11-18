# bash completion for mysqladmin                           -*- shell-script -*-

_comp_cmd_mysqladmin()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[uhScPOiw]*)'
    # shellcheck disable=SC2254
    case $prev in
        --user | -${noargopts}u)
            _comp_compgen -- -u
            return
            ;;
        --host | -${noargopts}h)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        --character-sets-dir | --ssl-capath)
            _comp_compgen_filedir -d
            return
            ;;
        --default-character-set)
            _comp_compgen -x mysql character_sets
            return
            ;;
        --socket | -${noargopts}S)
            _comp_compgen_filedir sock
            return
            ;;
        --defaults-file | --defaults-extra-file)
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
        --count | --port | --set-variable | --sleep | --ssl-cipher | --wait | \
            --connect_timeout | --shutdown_timeout | -${noargopts}[cPOiw])
            return
            ;;
        --help | --version | -${noargopts}[?V])
            return
            ;;
    esac

    [[ $was_split ]] && return

    _comp_compgen_help

    _comp_compgen -a -- -W 'create debug drop extended-status flush-hosts
        flush-logs flush-status flush-tables flush-threads flush-privileges
        kill password old-password ping processlist reload refresh shutdown
        status start-slave stop-slave variables version'

    [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
} &&
    complete -F _comp_cmd_mysqladmin mysqladmin

# ex: filetype=sh
