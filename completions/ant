# bash completion for ant and phing                        -*- shell-script -*-

_comp_cmd_ant__targets()
{
    local line basedir

    [[ $1 == */* ]] && basedir=${1%/*} || basedir=.

    # parse buildfile for targets
    while read -rd '>' line; do
        if [[ $line =~ \<(target|extension-point)[[:space:]].*name=[\"\']([^\"\']+) ]]; then
            REPLY+=("${BASH_REMATCH[2]}")
        fi
    done <"$1"

    # parse imports
    while read -rd '>' line; do
        if [[ $line =~ \<import[[:space:]].*file=[\"\']([^\"\']+) ]]; then
            local imported_buildfile
            imported_buildfile="${basedir}/${BASH_REMATCH[1]}"
            if [[ -f $imported_buildfile ]]; then
                "$FUNCNAME" "$imported_buildfile"
            fi
        fi
    done <"$1"
}

_comp_cmd_ant()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -h | -help | --h | --help | -projecthelp | -p | -version | -diagnostics)
            return
            ;;
        -buildfile | -file | -f)
            _comp_compgen_filedir 'xml'
            return
            ;;
        -logfile | -l)
            [[ $1 != *phing || $prev != -l ]] && _comp_compgen_filedir
            return
            ;;
        -propertyfile)
            _comp_compgen_filedir properties
            return
            ;;
        -nice)
            _comp_compgen -- -W '{1..10}'
            return
            ;;
        -lib)
            _comp_compgen_filedir -d
            return
            ;;
        -logger | -listener | -inputhandler | -main | -find | -s)
            return
            ;;
    esac

    if [[ $cur == -D* ]]; then
        return
    elif [[ $cur == -* ]]; then
        # The </dev/null prevents "phing -" weirdness/getting just a literal
        # tab displayed on complete on CentOS 6 with phing 2.6.1.
        _comp_compgen_help -- -h </dev/null
    else
        # available targets completion
        # find which buildfile to use
        local buildfile=build.xml i
        for ((i = 1; i < cword; i++)); do
            if [[ ${words[i]} == -@(?(build)file|f) ]]; then
                buildfile=${words[i + 1]}
                break
            fi
        done
        if ((i == cword)); then
            local IFS=$' \t\n'
            for i in ${ANT_ARGS-}; do
                if [[ $prev == -@(?(build)file|f) ]]; then
                    buildfile=$i
                    break
                fi
                prev=$i
            done
        fi
        [[ ! -f $buildfile ]] && return

        local REPLY=()

        # fill targets
        _comp_cmd_ant__targets "$buildfile"

        _comp_compgen -- -W '"${REPLY[@]}"'
    fi
} &&
    complete -F _comp_cmd_ant ant phing
if type complete-ant-cmd.pl &>/dev/null; then
    complete -C complete-ant-cmd.pl -F _comp_cmd_ant ant
fi

# ex: filetype=sh
