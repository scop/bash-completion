# bash completion for k3b                                  -*- shell-script -*-

_comp_cmd_k3b()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --help* | --author | -v | --version | --license | --lang)
            return
            ;;
        --datacd | --audiocd | --videocd | --mixedcd | --emovixcd | --videodvd)
            _comp_compgen_filedir
            return
            ;;
        --copydvd | --formatdvd | --videodvdrip)
            _comp_compgen_dvd_devices
            return
            ;;
        --copycd | --erasecd | --cddarip | --videocdrip)
            _comp_compgen_cd_devices
            _comp_compgen -a dvd_devices
            return
            ;;
        --cdimage | --image)
            _comp_compgen_filedir '@(cue|iso|toc)'
            return
            ;;
        --dvdimage)
            _comp_compgen_filedir iso
            return
            ;;
        --ao)
            _comp_compgen -- -W 'alsa arts'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        _comp_compgen_filedir
    fi
} &&
    complete -F _comp_cmd_k3b k3b

# ex: filetype=sh
