# mypy completion                                          -*- shell-script -*-

_comp_cmd_mypy()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    [[ $cword -gt 2 && ${words[cword - 2]} == --shadow-file ]] &&
        prev=--shadow-file # hack; takes two args

    local noargopts='!(-*|*[pcm]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | --python-version | --platform | --always-true | \
            --always-false | --@(dis|en)able-error-code | --find-occurrences | \
            --exclude | --package | --command | -${noargopts}[hVpc])
            return
            ;;
        --config-file)
            _comp_compgen_filedir
            return
            ;;
        --follow-imports)
            _comp_compgen -- -W 'normal silent skip error'
            return
            ;;
        --python-executable)
            _comp_compgen -c "${cur:-py}" commands
            return
            ;;
        --*-dir | --*-report)
            _comp_compgen_filedir -d
            return
            ;;
        --custom-typing-module | --module | -${noargopts}m)
            _comp_compgen -x python modules
            return
            ;;
        --shadow-file)
            _comp_compgen_filedir '@(py|pyi)'
            return
            ;;
        --junit-xml)
            _comp_compgen_filedir xml
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen_filedir '@(py|pyi)'
} &&
    complete -F _comp_cmd_mypy mypy

# ex: filetype=sh
