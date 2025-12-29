# koji completion                                          -*- shell-script -*-

_comp_cmd_koji__search()
{
    _comp_compgen -a split -- "$("$1" -q search "$2" "$cur*" 2>/dev/null)"
}

_comp_cmd_koji__build()
{
    _comp_cmd_koji__search "$1" build
}

_comp_cmd_koji__package()
{
    _comp_cmd_koji__search "$1" package
}

_comp_cmd_koji__user()
{
    _comp_cmd_koji__search "$1" user
}

_comp_cmd_koji__tag()
{
    _comp_compgen -a split -- "$("$1" -q list-tags 2>/dev/null)"
}

_comp_cmd_koji__target()
{
    _comp_compgen -a split -- "$("$1" -q list-targets 2>/dev/null |
        _comp_awk '{ print $1 }')"
}

_comp_cmd_koji()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local commandix command="" has_command=""
    for ((commandix = 1; commandix < cword; commandix++)); do
        if [[ ${words[commandix]} != -* ]]; then
            command=${words[commandix]}
            has_command=set
            break
        fi
    done

    local noargopts='!(-*|*[co]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --help-commands | -${noargopts}h*)
            return
            ;;
        --config | --keytab | -${noargopts}[co])
            _comp_compgen_filedir
            return
            ;;
        --runas | --user | --editor | --by)
            _comp_cmd_koji__user "$1"
            return
            ;;
        --authtype)
            _comp_compgen -- -W 'noauth ssl password kerberos'
            return
            ;;
        --topdir)
            _comp_compgen_filedir -d
            return
            ;;
        --type)
            case ${command-} in
                latest-pkg | list-tagged)
                    _comp_compgen -- -W 'maven'
                    ;;
            esac
            return
            ;;
        --name)
            case ${command-} in
                list-targets)
                    _comp_cmd_koji__target "$1"
                    ;;
            esac
            return
            ;;
        --owner)
            _comp_cmd_koji__user "$1"
            return
            ;;
        --tag | --latestfrom)
            _comp_cmd_koji__tag "$1"
            return
            ;;
        --package)
            _comp_cmd_koji__package "$1"
            return
            ;;
        --build)
            _comp_cmd_koji__build "$1"
            return
            ;;
        --build-target)
            _comp_cmd_koji__target "$1"
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $has_command ]]; then
        if [[ $cur == -* ]]; then
            _comp_compgen_help -- "$command" --help
            [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
            return
        fi

        # How many'th non-option arg (1-based) for $command are we completing?
        local i nth=1
        for ((i = commandix + 1; i < cword; i++)); do
            [[ ${words[i]} == -* ]] || ((nth++))
        done

        case $command in
            build | maven-build | win-build)
                case $nth in
                    1)
                        _comp_cmd_koji__target "$1"
                        ;;
                    2)
                        _comp_compgen_filedir src.rpm
                        ;;
                esac
                ;;
            cancel)
                _comp_cmd_koji__build "$1"
                ;;
            chain-build)
                case $nth in
                    1)
                        _comp_cmd_koji__target "$1"
                        ;;
                esac
                ;;
            download-build)
                case $nth in
                    1)
                        _comp_cmd_koji__build "$1"
                        ;;
                esac
                ;;
            import-comps)
                case $nth in
                    1)
                        _comp_compgen_filedir xml
                        ;;
                    2)
                        _comp_cmd_koji__tag "$1"
                        ;;
                esac
                ;;
            latest-by-tag)
                _comp_cmd_koji__package "$1"
                ;;
            latest-pkg | list-groups | list-tag-inheritance | show-groups)
                case $nth in
                    1)
                        _comp_cmd_koji__tag "$1"
                        ;;
                esac
                ;;
            list-tagged)
                case $nth in
                    1)
                        _comp_cmd_koji__tag "$1"
                        ;;
                    2)
                        _comp_cmd_koji__package "$1"
                        ;;
                esac
                ;;
            list-untagged)
                case $nth in
                    1)
                        _comp_cmd_koji__package "$1"
                        ;;
                esac
                ;;
            move-pkg)
                case $nth in
                    1 | 2)
                        _comp_cmd_koji__tag "$1"
                        ;;
                    *)
                        _comp_cmd_koji__package "$1"
                        ;;
                esac
                ;;
            search)
                case $nth in
                    1)
                        _comp_compgen -- -W 'package build tag target user host
                            rpm'
                        ;;
                esac
                ;;
            tag-pkg | untag-pkg)
                case $nth in
                    1)
                        _comp_cmd_koji__tag "$1"
                        ;;
                    *)
                        _comp_cmd_koji__package "$1"
                        ;;
                esac
                ;;
            taginfo)
                _comp_cmd_koji__tag "$1"
                ;;
            wait-repo)
                case $nth in
                    1)
                        for ((i = commandix + 1; i < cword; i++)); do
                            if [[ ${words[i]} == --target ]]; then
                                _comp_cmd_koji__target "$1"
                                return
                            fi
                        done
                        _comp_cmd_koji__tag "$1"
                        ;;
                esac
                ;;
        esac
        return
    fi

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    elif [[ ! $has_command ]]; then
        _comp_compgen_split -- "$("$1" --help-commands 2>/dev/null |
            _comp_awk '/^(  +|\t)/ { print $1 }')"
    fi
} &&
    complete -F _comp_cmd_koji koji arm-koji ppc-koji s390-koji sparc-koji

# ex: filetype=sh
