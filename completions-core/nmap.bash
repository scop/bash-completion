# bash completion for nmap                                 -*- shell-script -*-

_comp_cmd_nmap()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -iL | -oN | -oX | -oS | -oG | ---excludefile | --resume | --stylesheet)
            _comp_compgen_filedir
            return
            ;;
        -oA | --datadir)
            _comp_compgen_filedir -d
            return
            ;;
        -e)
            _comp_compgen_available_interfaces -a
            return
            ;;
        -b | --dns-servers)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        # strip everything following a :, inclusive
        # strip everything following a =, exclusive
        # expand -X; -Y to -X -Y
        # expand -X/-Y/-Z to -X -Y -Z
        # expand -X/Y/Z to -X -Y -Z
        # expand --foo/bar to --foo --bar
        # strip everything following a non-option name or = char
        # TODO: should expand -T<0-5> to -T0 ... -T5
        _comp_compgen_split -- "$(
            "$1" --help 2>&1 | command sed \
                -e "s/:.*$//" \
                -e "s/=.*$/=/" \
                -e "s/;[[:space:]]*-/ -/g" \
                -e "s/\/-/ -/g" \
                -e "/^[[:space:]]*-[^-]/s/\/\([^-]\)/ -\1/g" \
                -e "/^[[:space:]]*--/s/\/\([^-]\)/ --\1/g" \
                -e "s/[^[:space:]a-zA-Z0-9=-].*$//"
        )"
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        _comp_compgen_known_hosts -- "$cur"
    fi
} &&
    complete -F _comp_cmd_nmap nmap

# ex: filetype=sh
