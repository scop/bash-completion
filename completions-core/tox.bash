# tox completion                                           -*- shell-script -*-

_comp_cmd_tox()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    # Complete defaults following a "--"
    if [[ "${words[*]:0:cword} " == *\ --\ * && $cur != -- ]]; then
        compopt -o bashdefault -o default
        return
    fi

    local noargopts='!(-*|*[nice]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | --num | --index-url | --hashseed | --force-dep | \
            -${noargopts}[hni])
            return
            ;;
        -${noargopts}c)
            _comp_compgen_filedir ini
            return
            ;;
        --installpkg | --result-json | --workdir)
            _comp_compgen_filedir
            return
            ;;
        -${noargopts}e)
            local envs=$(
                {
                    "$1" --listenvs-all || "$1" --listenvs
                } 2>/dev/null
            )
            [[ $envs ]] || envs=$(
                command sed -e 's/,/ /g' -ne 's/^envlist[[:space:]]*=//p' \
                    tox.ini 2>/dev/null
            )
            _comp_delimited , -X '*[{}]*' -W "$envs ALL"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        _comp_compgen -a -- -W '--'
        return
    fi
} &&
    complete -F _comp_cmd_tox tox

# ex: filetype=sh
