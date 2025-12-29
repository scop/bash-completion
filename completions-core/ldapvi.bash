# bash completion for ldapvi                               -*- shell-script -*-

_comp_cmd_ldapvi()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[Y]*)'
    # shellcheck disable=SC2254
    case $prev in
        --host | -${noargopts}h)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        --sasl-mech | -${noargopts}Y)
            _comp_compgen -- -W 'EXTERNAL GSSAPI DIGEST-MD5 CRAM-MD5 PLAIN
                ANONYMOUS'
            return
            ;;
        --bind)
            _comp_compgen -- -W 'simple sasl'
            return
            ;;
        --bind-dialog)
            _comp_compgen -- -W 'never auto always'
            return
            ;;
        --scope)
            _comp_compgen -- -W 'base one sub'
            return
            ;;
        --deref)
            _comp_compgen -- -W 'never searching finding always'
            return
            ;;
        --encoding)
            _comp_compgen -- -W 'ASCII UTF-8 binary'
            return
            ;;
        --tls)
            _comp_compgen -- -W 'never allow try strict'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
    fi
} &&
    complete -F _comp_cmd_ldapvi ldapvi

# ex: filetype=sh
