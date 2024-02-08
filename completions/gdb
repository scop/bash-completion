# bash completion for gdb                                  -*- shell-script -*-

_comp_cmd_gdb()
{
    local cur prev words cword comp_args i
    _comp_initialize -- "$@" || return

    # gdb [options] --args executable-file [inferior-arguments ...]
    for ((i = 1; i < cword; i++)); do
        if [[ ${words[i]} == --args ]]; then
            _comp_command_offset $((i + 1))
            return $?
        fi
    done

    # gdb [options] [executable-file [core-file or process-id]]
    if ((cword == 1)); then
        compopt -o filenames
        if _comp_looks_like_path "$cur"; then
            # compgen -c works as expected if $cur contains any slashes.
            local PATH="$PATH:."
            _comp_compgen_commands
        else
            # otherwise compgen -c contains Bash's built-in commands,
            # functions and aliases. Thus we need to retrieve the program
            # names manually.
            local path_array
            _comp_compgen -Rv path_array split -F : -X '' -S /. -- "$PATH"
            _comp_compgen_split -o plusdirs -- "$(
                # Note: ${v+"$@"} does not work with empty IFS in bash < 4.4
                IFS=$' \t\n'
                find ${path_array[@]+"${path_array[@]}"} . -name . -o \
                    -type d -prune -o -perm -u+x -print 2>/dev/null |
                    command sed 's|^.*/||' | sort -u
            )"
        fi
    elif ((cword == 2)); then
        _comp_compgen_split -- "$(command ps axo comm,pid |
            _comp_awk '{if ($1 ~ /^'"${prev##*/}"'/) print $2}')"
        compopt -o filenames
        _comp_compgen -a -- -f -X '!?(*/)core?(.?*)' -o plusdirs
    fi
} &&
    complete -F _comp_cmd_gdb gdb

# ex: filetype=sh
