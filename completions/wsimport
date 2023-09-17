# wsimport(1) completion                                   -*- shell-script -*-

_comp_cmd_wsimport()
{
    local cur prev words cword comp_args
    _comp_initialize -n : -- "$@" || return

    case $prev in
        -help | -version | -B | -p | -wsdllocation)
            return
            ;;
        -b)
            _comp_compgen_filedir '@(xml|xjb)'
            return
            ;;
        -catalog)
            _comp_compgen_filedir '@(xml|soc|catalog)'
            return
            ;;
        -d | –s)
            _comp_compgen_filedir -d
            return
            ;;
        -target)
            _comp_compgen -- -W '2.0 2.1 2.2'
            return
            ;;
        -clientjar)
            _comp_compgen_filedir jar
            return
            ;;
    esac

    if [[ $cur == -httpproxy:* ]]; then
        _comp_compgen_known_hosts -- "${cur#-httpproxy:}"
        return
    elif [[ $cur == -* ]]; then
        _comp_compgen_help -- -help
        [[ ${COMPREPLY-} == *: ]] && compopt -o nospace
        _comp_ltrim_colon_completions "$cur"
        return
    fi

    _comp_compgen_filedir wsdl
} &&
    complete -F _comp_cmd_wsimport wsimport

# ex: filetype=sh
