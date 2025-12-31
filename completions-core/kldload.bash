# FreeBSD kldload completion                               -*- shell-script -*-

[[ $OSTYPE == *freebsd* ]] || return 1

_comp_cmd_kldload()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if _comp_looks_like_path "$cur"; then
        _comp_compgen_filedir ko
        return
    fi

    local moddirs modules i
    if _comp_split -F ";" moddirs "$(kldconfig -r 2>/dev/null)"; then
        compopt -o filenames
        for i in "${moddirs[@]}"; do
            _comp_compgen -v modules -c "$i/$cur" -- -f &&
                COMPREPLY+=("${modules[@]#$i/}")
        done
        ((${#COMPREPLY[@]})) &&
            COMPREPLY=("${COMPREPLY[@]%.ko}")
    fi

    # also add dirs in current dir
    _comp_compgen -a filedir -d

} &&
    complete -F _comp_cmd_kldload kldload

# ex: filetype=sh
