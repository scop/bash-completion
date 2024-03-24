# bash completion for xmlwf(1)                             -*- shell-script -*-

_comp_cmd_xmlwf()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*d)
            _comp_compgen_filedir -d
            return
            ;;
        -*e)
            _comp_compgen -- -W 'US-ASCII UTF-8 UTF-16 ISO-8859-1'
            return
            ;;
        -*[abv])
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help || _comp_compgen_usage
        return
    fi

    _comp_compgen_filedir '@(*ml|htm|svg|xs[dl]|rng|wsdl|jnlp|tld|dbk|docbook|page|rss)'
} &&
    complete -F _comp_cmd_xmlwf xmlwf

# ex: filetype=sh
