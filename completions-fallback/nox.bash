# 3rd party completion loader for argcomplete commands     -*- shell-script -*-
# sourced using no args to `register-python-argcomplete`.
#
# This serves as a fallback in case the completion is not installed otherwise.

eval -- "$(
    pathcmd=$(type -P -- "$1" 2>/dev/null | command sed 's,/[^/]*$,,')
    [[ $pathcmd ]] && PATH=$pathcmd${PATH:+:$PATH}
    register-python-argcomplete --shell bash "$1" 2>/dev/null ||
        register-python-argcomplete3 --shell bash "$1" 2>/dev/null
)"

# ex: filetype=sh
