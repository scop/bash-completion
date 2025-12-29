# bash completion for gpg                                  -*- shell-script -*-

_comp_cmd_gpg()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[skKr]*)'
    # shellcheck disable=SC2254
    case $prev in
        --sign | --clear-sign | --clearsign | --decrypt-files | \
            --load-extension | -${noargopts}s)
            _comp_compgen_filedir
            return
            ;;
        --list-keys | --list-public-keys | --locate-keys | \
            --locate-external-keys | --fingerprint | --delete-keys | \
            --delete-secret-and-public-keys | --export | --refresh-keys | \
            --search-keys | --edit-key | --sign-key | --lsign-key | \
            --nrsign-key | --nrlsign-key | --try-secret-key | -${noargopts}k)
            # return list of public keys
            _comp_compgen_split -- "$("$1" --list-keys 2>/dev/null |
                command sed -ne \
                    's@^pub.*/\([^ ]*\).*$@\1@p' -ne \
                    's@^.*\(<\([^>]*\)>\).*$@\2@p')"
            return
            ;;
        --list-secret-keys | --delete-secret-keys | --export-secret-keys | \
            --export-secret-subkeys | -${noargopts}K)
            # return list of secret keys
            _comp_compgen_split -- "$("$1" --list-secret-keys 2>/dev/null |
                command sed -ne 's@^.*<\([^>]*\)>.*$@\1@p')"
            return
            ;;
        --recipient | -${noargopts}r)
            _comp_compgen_split -- "$("$1" --list-keys 2>/dev/null |
                command sed -ne 's@^.*<\([^>]*\)>.*$@\1@p')"
            if [[ -e ~/.gnupg/gpg.conf ]]; then
                _comp_compgen -a split -- "$(command sed -ne \
                    's@^[ \t]*group[ \t][ \t]*\([^=]*\).*$@\1@p' \
                    ~/.gnupg/gpg.conf)"
            fi
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_split -- "$("$1" --dump-options)"
    fi
} &&
    complete -F _comp_cmd_gpg -o default gpg

# ex: filetype=sh
