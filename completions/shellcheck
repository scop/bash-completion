# bash completion for shellcheck(1)                        -*- shell-script -*-

_comp_cmd_shellcheck__optarg()
{
    local args=$("$1" --help 2>&1 |
        command sed -e 's/,/ /g' -ne 's/^.*'"$2"'\>.*(\([^)]*\)).*/\1/p')
    _comp_compgen -a -- -W '$args'
}

_comp_cmd_shellcheck()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[eifCsoPW]*)'
    # shellcheck disable=SC2254
    case $prev in
        --version | -${noargopts}V*)
            return
            ;;
        --exclude | --include | -${noargopts}[ei])
            return
            ;;
        --format | -${noargopts}f)
            local args=$("$1" --format=nonexistent-format /dev/null 2>&1 |
                command sed -ne '/^Supported formats/,//p' |
                command sed -ne '/^[[:space:]]/p')
            _comp_compgen -- -W '$args'
            return
            ;;
        --color | -${noargopts}C)
            _comp_cmd_shellcheck__optarg "$1" --color
            return
            ;;
        --shell | -${noargopts}s)
            _comp_cmd_shellcheck__optarg "$1" --shell
            return
            ;;
        --enable | -${noargopts}o)
            _comp_compgen -- -W 'all' # TODO others?
            return
            ;;
        --source-path | -${noargopts}P)
            _comp_compgen_filedir -d
            _comp_compgen -a -- -W 'SCRIPTDIR'
            return
            ;;
        --wiki-link-count | -${noargopts}W)
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_shellcheck shellcheck

# ex: filetype=sh
