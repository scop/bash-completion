# mtx completion                                           -*- shell-script -*-
# by Jon Middleton <jjm@ixtab.org.uk>

_comp_cmd_mtx()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local options tapes drives

    options="-f nobarcode invert noattach --version inquiry noattach \
        inventory status load unload eepos first last next"

    tapes=$(mtx status 2>/dev/null |
        _comp_awk '/Storage Element [0-9]+:Full/ { printf "%s ", $3 }')
    tapes=${tapes//:Full/}

    drives=$(mtx status 2>/dev/null |
        _comp_awk '/Data Transfer Element [0-9]+:(Full|Empty)/ { printf "%s ", $4 }')
    drives=${drives//:Full/}
    drives=${drives//:Empty/}

    if ((cword > 1)); then
        case $prev in
            load)
                _comp_compgen -- -W "$tapes"
                ;;
            unload | first | last | next)
                _comp_compgen -- -W "$drives"
                ;;
            -f)
                true
                ;;
            *)
                true
                ;;
        esac
    else
        _comp_compgen -- -W "$options"
    fi
} &&
    complete -F _comp_cmd_mtx mtx

# ex: filetype=sh
