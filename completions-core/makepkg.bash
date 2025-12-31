# makepkg completion                                       -*- shell-script -*-

# Slackware Linux variant
_comp_cmd_makepkg__slackware()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case "$prev" in
        -l | --linkadd | -c | --chown)
            _comp_compgen -- -W 'y n'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help - <<<"$("$1" | command sed -e "s/^options://")"
        return
    fi

    _comp_compgen_filedir
}

_comp_cmd_makepkg__bootstrap()
{
    local fname help

    # Use --help to detect variant; the Slackware one starts making
    # a package for unknown args, including --version :P
    help=$("$1" --help 2>&1)
    case ${help,,} in
        *slackware*)
            fname=_comp_cmd_makepkg__slackware
            ;;
        *)
            fname=_comp_complete_minimal
            ;;
    esac

    unset -f "$FUNCNAME"
    complete -F $fname makepkg
    $fname "$@"
} &&
    complete -F _comp_cmd_makepkg__bootstrap makepkg

# ex: filetype=sh
