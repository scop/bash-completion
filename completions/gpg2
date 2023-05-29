# gpg2(1) completion                                       -*- shell-script -*-

_comp_cmd_gpg2()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[sr]*)'
    # shellcheck disable=SC2254
    case $prev in
        --homedir)
            _comp_compgen_filedir -d
            return
            ;;
        --sign | --clearsign | --options | --decrypt | -${noargopts}s)
            _comp_compgen_filedir
            return
            ;;
        --export | --sign-key | --lsign-key | --nrsign-key | --nrlsign-key | \
            --edit-key | --delete-keys | --delete-secret-and-public-keys | \
            --locate-keys | --refresh-keys)
            # return list of public keys
            _comp_compgen_split -- "$("$1" --list-keys 2>/dev/null |
                command sed -ne \
                    's@^pub.*/\([^ ]*\).*$@\1@p' -ne \
                    's@^.*\(<\([^>]*\)>\).*$@\2@p')"
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
    complete -F _comp_cmd_gpg2 -o default gpg2

# ex: filetype=sh
