# perlcritic(1) completion                                 -*- shell-script -*-

_comp_cmd_perlcritic()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --help | --version | --top | --include | --exclude | --single-policy | \
            --colo?(u)r-severity-* | --program-extensions | -[?HVs])
            return
            ;;
        --severity)
            _comp_compgen -- -W '{1..5} brutal cruel harsh stern gentle'
            return
            ;;
        --profile | -p)
            _comp_compgen_filedir perlcriticrc
            return
            ;;
        --theme)
            _comp_compgen_split -- "$("$1" --list-themes 2>/dev/null)"
            return
            ;;
        --profile-strictness)
            _comp_compgen -- -W 'warn fatal quiet'
            return
            ;;
        --verbose)
            _comp_compgen -- -W '{1..11}'
            return
            ;;
        --pager)
            _comp_compgen_commands
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
        return
    fi

    _comp_compgen_filedir 'p[lm]'
} &&
    complete -F _comp_cmd_perlcritic perlcritic

# ex: filetype=sh
