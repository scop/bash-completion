# bash completion for GNU find                             -*- shell-script -*-
# This makes heavy use of ksh style extended globs and contains Linux specific
# code for completing the parameter to the -fstype option.

_comp_cmd_find()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local i
    for ((i = 1; i < cword; i++)); do
        if [[ ${words[i]} == -@(exec|ok)?(dir) ]]; then
            _comp_command_offset $((i + 1))
            return
        fi
    done

    case $prev in
        -maxdepth | -mindepth)
            _comp_compgen -- -W '{0..9}'
            return
            ;;
        -newer | -anewer | -cnewer | -fls | -fprint | -fprint0 | -fprintf | -name | -[il]name | \
            -ilname | -wholename | -[il]wholename | -samefile)
            _comp_compgen_filedir
            return
            ;;
        -fstype)
            _comp_compgen_fstypes
            [[ $OSTYPE == *bsd* ]] &&
                _comp_compgen -a -- -W 'local rdonly'
            return
            ;;
        -gid)
            _comp_compgen_gids
            return
            ;;
        -group)
            _comp_compgen -- -g
            return
            ;;
        -xtype | -type)
            _comp_compgen -- -W 'b c d p f l s'
            return
            ;;
        -uid)
            _comp_compgen_uids
            return
            ;;
        -user)
            _comp_compgen -- -u
            return
            ;;
        -[acm]min | -[acm]time | -inum | -path | -ipath | -regex | -iregex | -links | -perm | \
            -size | -used | -printf | -context)
            # do nothing, just wait for a parameter to be given
            return
            ;;
        -regextype)
            _comp_compgen -- -W 'emacs posix-awk posix-basic posix-egrep
                posix-extended'
            return
            ;;
    esac

    local i exprfound=""
    # set exprfound to true if there is already an expression present
    for i in "${words[@]}"; do
        [[ $i == [-\(\),\!]* ]] && exprfound=set && break
    done

    # handle case where first parameter is not a dash option
    if [[ ! $exprfound && $cur != [-\(\),\!]* ]]; then
        _comp_compgen_filedir -d
        return
    fi

    # complete using basic options
    _comp_compgen -- -W '-daystart -depth -follow -help -ignore_readdir_race
        -maxdepth -mindepth -mindepth -mount -noignore_readdir_race -noleaf
        -regextype -version -warn -nowarn -xdev -amin -anewer -atime -cmin
        -cnewer -ctime -empty -executable -false -fstype -gid -group -ilname
        -iname -inum -ipath -iregex -iwholename -links -lname -mmin -mtime
        -name -newer -nogroup -nouser -path -perm -readable -regex -samefile
        -size -true -type -uid -used -user -wholename -writable -xtype -context
        -delete -exec -execdir -fls -fprint -fprint0 -fprintf -ls -ok -okdir
        -print -print0 -printf -prune -quit'

    if ((${#COMPREPLY[@]} != 0)); then
        # this removes any options from the list of completions that have
        # already been specified somewhere on the command line, as long as
        # these options can only be used once (in a word, "options", in
        # opposition to "tests" and "actions", as in the find(1) manpage).
        local -A onlyonce=([-daystart]=1 [-depth]=1 [-follow]=1 [-help]=1
            [-ignore_readdir_race]=1 [-maxdepth]=1 [-mindepth]=1 [-mount]=1
            [-noignore_readdir_race]=1 [-noleaf]=1 [-nowarn]=1 [-regextype]=1
            [-version]=1 [-warn]=1 [-xdev]=1)
        local j
        for i in "${words[@]}"; do
            [[ $i && -v onlyonce["$i"] ]] || continue
            for j in "${!COMPREPLY[@]}"; do
                [[ ${COMPREPLY[j]} == "$i" ]] && unset -v 'COMPREPLY[j]'
            done
        done
    fi

    _comp_compgen -a filedir

} &&
    complete -F _comp_cmd_find find

# ex: filetype=sh
