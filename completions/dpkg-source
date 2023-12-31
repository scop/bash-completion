# Debian dpkg-source completion                            -*- shell-script -*-

_comp_cmd_dpkg_source()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local options word action packopts unpackopts fields

    packopts="-c -l -F -V -T -D -U -W -E -sa -i -I -sk -sr -ss -sA -sK -sP \
        -sU -sR"
    unpackopts="-sp -sn -su"
    options="-x -b --print-format --before-build --after-build --commit $packopts $unpackopts"
    fields="Format Source Version Binary Maintainer Uploader Architecture \
            Standards-Version Build-Depends Files"

    action=options
    for word in "${words[@]:1}"; do
        if [[ $word == -x ]]; then
            action=unpack
        elif [[ $word == -b ]]; then
            action=pack
        elif [[ $word == -h ]]; then
            action=help
        fi
    done

    case $action in
        unpack)
            case $prev in
                -x)
                    _comp_compgen_filedir 'dsc'
                    ;;
                *)
                    _comp_compgen -- -W "$unpackopts"
                    _comp_compgen -a filedir
                    ;;
            esac
            return
            ;;
        pack)
            case $prev in
                -b)
                    _comp_compgen_filedir -d
                    ;;
                -c | -l | -T | -i | -I)
                    # -c: get controlfile
                    # -l: get per-version info from this file
                    # -T: read variables here, not debian/substvars
                    # -i: <regexp> filter out files to ignore diffs of.
                    # -I: filter out files when building tarballs.
                    # return directory names and file names
                    _comp_compgen_filedir
                    ;;
                -F)
                    # -F: force change log format
                    _comp_compgen_split -- "$(command ls /usr/lib/dpkg/parsechangelog)"
                    ;;
                -V)
                    # -V: set a substitution variable
                    # we don't know anything about possible variables or values
                    # so we don't try to suggest any completion.
                    COMPREPLY=()
                    ;;
                -D)
                    # -D: override or add a .dsc field and value
                    # if $cur doesn't contain a = yet, suggest variable names
                    if [[ $cur == *=* ]]; then
                        # $cur contains a "="
                        COMPREPLY=()
                    else
                        _comp_compgen -- -W "$fields"
                    fi
                    ;;
                -U)
                    # -U: remove a field
                    # Suggest possible fieldnames
                    _comp_compgen -- -W "$fields"
                    ;;
                *)
                    _comp_compgen -- -W '$packopts $unpackopts'
                    ;;
            esac
            return
            ;;
        *)
            _comp_compgen -- -W "$options"
            return
            ;;
    esac
} &&
    complete -F _comp_cmd_dpkg_source dpkg-source

# ex: filetype=sh
