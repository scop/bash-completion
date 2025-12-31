# bash completion for xmllint(1)                           -*- shell-script -*-

_comp_cmd_xmllint()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -o | --output)
            _comp_compgen_filedir
            return
            ;;
        --path | --dtdvalidfpi | --maxmem | --pattern | --xpath)
            # argument required but no completions available
            return
            ;;
        --dtdvalid)
            _comp_compgen_filedir 'dtd?(.gz)'
            return
            ;;
        --relaxng)
            _comp_compgen_filedir 'rng?(.gz)'
            return
            ;;
        --schema)
            _comp_compgen_filedir 'xsd?(.gz)'
            return
            ;;
        --schematron)
            _comp_compgen_filedir 'sch?(.gz)'
            return
            ;;
        --encode)
            _comp_compgen -x iconv charsets
            return
            ;;
        --pretty)
            _comp_compgen -- -W '{0..2}'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        COMPREPLY=("${COMPREPLY[@]%:}")
        return
    fi

    _comp_compgen_filedir '@(*ml|htm|svg?(z)|xs[dl]|rng|wsdl|jnlp|tld|dbk|docbook|page|rss)?(.gz)'
} &&
    complete -F _comp_cmd_xmllint xmllint

# ex: filetype=sh
