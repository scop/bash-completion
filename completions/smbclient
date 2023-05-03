# bash completion for samba                                -*- shell-script -*-

_comp_cmd_smbclient__resolve_order()
{
    _comp_compgen -- -W 'lmhosts host wins bcast'
}

_comp_cmd_smbclient__domains()
{
    if [[ ${BASH_COMPLETION_CMD_SMBTREE_SCAN-${COMP_SAMBA_SCAN-}} ]]; then
        _comp_compgen_split -- "$(smbtree -N -D)"
    fi
}

_comp_cmd_smbclient__hosts()
{
    if [[ ${BASH_COMPLETION_CMD_SMBTREE_SCAN-${COMP_SAMBA_SCAN-}} ]]; then
        _comp_compgen_split -- "$(smbtree -N -S |
            command sed -ne 's/^[[:space:]]*\\\\*\([^[:space:]]*\).*/\1/p')"
    fi
}

_comp_cmd_smbclient__debuglevel()
{
    _comp_compgen -- -W '{0..10}'
}

_comp_cmd_smbclient__sockopts()
{
    _comp_compgen -- -W 'SO_KEEPALIVE SO_REUSEADDR SO_BROADCAST TCP_NODELAY
        IPTOS_LOWDELAY IPTOS_THROUGHPUT SO_SNDBUF SO_RCVBUF SO_SNDLOWAT
        SO_RCVLOWAT'
}

_comp_cmd_smbclient__signing()
{
    _comp_compgen -- -W 'on off required'
}

_comp_cmd_smbclient()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[RtsAlDOTWdLSpMIbUniTcm]*)'
    # shellcheck disable=SC2254
    case $prev in
        --name-resolve | -${noargopts}R)
            _comp_cmd_smbclient__resolve_order
            return
            ;;
        -${noargopts}t)
            _comp_compgen -- -W 'SJIS EUC JIS7 JIS8 JUNET HEX CAP'
            return
            ;;
        --configfile | --authentication-file | -${noargopts}[sA])
            _comp_compgen_filedir
            return
            ;;
        --log-basename | --directory | -${noargopts}[lD])
            _comp_compgen_filedir -d
            return
            ;;
        --socket-options | -${noargopts}O)
            _comp_cmd_smbclient__sockopts
            return
            ;;
        -${noargopts}T)
            _comp_compgen -- -W 'c x I X F b g q r N a'
            return
            ;;
        --workgroup | -${noargopts}W)
            _comp_cmd_smbclient__domains
            return
            ;;
        --debuglevel | -${noargopts}d)
            _comp_cmd_smbclient__debuglevel
            return
            ;;
        --list | -${noargopts}L)
            _comp_cmd_smbclient__hosts
            return
            ;;
        --signing | -${noargopts}S)
            _comp_cmd_smbclient__signing
            return
            ;;
        --port | --message | --ip-address | --send-buffer | --user | \
            --netbiosname | --scope | --tar | --command | --max-protocol | \
            -${noargopts}[pMIbUniTcm])
            return
            ;;
        --help | --version | -${noargopts}[?V])
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_smbclient smbclient

_comp_cmd_smbget()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[ofdwupb]*)'
    # shellcheck disable=SC2254
    case $prev in
        --outputfile | --rcfile | -${noargopts}[of])
            _comp_compgen_filedir
            return
            ;;
        --debuglevel | -${noargopts}d)
            _comp_cmd_smbclient__debuglevel
            return
            ;;
        --workgroup | -${noargopts}w)
            _comp_cmd_smbclient__domains
            return
            ;;
        --username | --password | --blocksize | -${noargopts}[upb])
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_smbget smbget

_comp_cmd_smbcacls()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[AsldOWDMaSCGniU]*)'
    # shellcheck disable=SC2254
    case $prev in
        --configfile | --authentication-file | -${noargopts}[As])
            _comp_compgen_filedir
            return
            ;;
        --log-basename | -${noargopts}l)
            _comp_compgen_filedir -d
            return
            ;;
        --debuglevel | -${noargopts}d)
            _comp_cmd_smbclient__debuglevel
            return
            ;;
        --signing)
            _comp_cmd_smbclient__signing
            return
            ;;
        --socket-options | -${noargopts}O)
            _comp_cmd_smbclient__sockopts
            return
            ;;
        --workgroup | -${noargopts}W)
            _comp_cmd_smbclient__domains
            return
            ;;
        --help | --usage | --delete | --modify | --add | --set | --chown | \
            --chgrp | --netbiosname | --scope | --user | -${noargopts}[?DMaSCGniU])
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_smbcacls smbcacls

_comp_cmd_smbcquotas()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[sAldUuS]*)'
    # shellcheck disable=SC2254
    case $prev in
        --configfile | --authentication-file | -${noargopts}[sA])
            _comp_compgen_filedir
            return
            ;;
        --log-basename | -${noargopts}l)
            _comp_compgen_filedir -d
            return
            ;;
        --debuglevel | -${noargopts}d)
            _comp_cmd_smbclient__debuglevel
            return
            ;;
        --signing)
            _comp_cmd_smbclient__signing
            return
            ;;
        --help | --usage | --user | --set | -${noargopts}[?UuS])
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_smbcquotas smbcquotas

_comp_cmd_smbpasswd()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*r)
            _comp_cmd_smbclient__hosts
            return
            ;;
        -*R)
            _comp_cmd_smbclient__resolve_order
            return
            ;;
        -*c)
            _comp_compgen_filedir
            return
            ;;
        -*D)
            _comp_cmd_smbclient__debuglevel
            return
            ;;
        -*[Uhw])
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -h
    fi
} &&
    complete -F _comp_cmd_smbpasswd smbpasswd

_comp_cmd_smbtar()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*[rt])
            _comp_compgen_filedir tar
            return
            ;;
        -*s)
            _comp_cmd_smbclient__hosts
            return
            ;;
        -*l)
            _comp_cmd_smbclient__debuglevel
            return
            ;;
        -*N)
            _comp_compgen_filedir
            return
            ;;
        -*[pxbdu])
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
    fi
} &&
    complete -F _comp_cmd_smbtar smbtar

_comp_cmd_smbtree()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[sAldSU]*)'
    # shellcheck disable=SC2254
    case $prev in
        --configfile | --authentication-file | -${noargopts}[sA])
            _comp_compgen_filedir
            return
            ;;
        --log-basename | -${noargopts}l)
            _comp_compgen_filedir -d
            return
            ;;
        --debuglevel | -${noargopts}d)
            _comp_cmd_smbclient__debuglevel
            return
            ;;
        --signing | -${noargopts}S)
            _comp_cmd_smbclient__signing
            return
            ;;
        --help | --usage | --user | -${noargopts}[?U])
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_smbtree smbtree

# ex: filetype=sh
