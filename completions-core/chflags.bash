# chflags(1) completion                                      -*- shell-script -*-

[[ $OSTYPE == *@(bsd|darwin)* ]] || return 1

# References
#
# [1] FreeBSD - https://man.freebsd.org/cgi/man.cgi?chflags(1)
# [2] NetBSD - https://man.netbsd.org/NetBSD-9.0/chflags.1
# [3] OpenBSD - https://man.openbsd.org/chflags.1

_comp_cmd_chflags()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        # Complete -options
        local w opts=""
        for w in "${words[@]}"; do
            [[ $w == -R ]] && opts="-H -L -P" && break
        done
        [[ $OSTYPE == *freebsd* ]] && opts="$opts -x"
        _comp_compgen -- -W '-f -h -v -R $opts'
    else
        local REPLY
        # The first argument is a list of flags; the rest are filedir.
        _comp_count_args
        if ((REPLY == 1)); then
            case "$OSTYPE" in
                *netbsd*)
                    _comp_delimited , -W '
                        arch opaque nodump sappnd schg uappnd uchg'
                    ;;
                *openbsd*)
                    _comp_delimited , -W 'arch nodump sappnd schg uappnd uchg'
                    ;;
                *)
                    _comp_delimited , -W '
                        simmutable nosimmutable sappend nosappend archived
                        noarchived sunlink nosunlink opaque noopaque nodump
                        dump uimmutable nouimmutable uappend nouappend hidden
                        nohidden uunlink nouunlink'
                    ;;
            esac
        else
            _comp_compgen_filedir
        fi
    fi
} &&
    complete -F _comp_cmd_chflags chflags

# ex: filetype=sh
