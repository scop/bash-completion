# pylint(1) completion                                     -*- shell-script -*-

_comp_cmd_pylint__message_ids()
{
    local filter=p
    [[ ${2-} ]] && filter="/^$2 messages/,/^$/p"
    # 6: arbitrary, assumed no ids shorter than that
    # TODO(scop): The fallback here is slow, maybe memoize whether
    #   --list-msgs-enabled worked (>= 2.4.0) and avoid unnecessary tries
    #   again later?
    local msgs="$(
        set -o pipefail
        "$1" --list-msgs-enabled 2>/dev/null |
            command sed -ne "$filter" |
            command sed -ne 's/^[[:space:]]\{1,\}\([a-z-]\{6,\}\).*/\1/p' ||
            "$1" --list-msgs 2>/dev/null |
            command sed -ne 's/^:\([a-z-]\{6,\}\).*/\1/p'
    )"
    _comp_delimited , -W "$msgs"
}

_comp_cmd_pylint()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local python=python
    [[ ${1##*/} == *3* ]] && python=python3

    local noargopts='!(-*|*[edisrjf]*)'
    # shellcheck disable=SC2254
    case $prev in
        --version | --help | --long-help | --init-hook | \
            --ignore | --evaluation | --max-line-length | \
            --max-module-lines | --indent-string | --min-similarity-lines | \
            --max-args | --ignored-argument-names | --max-locals | \
            --max-returns | --max-branches | --max-statements | --max-parents | \
            --max-attributes | --min-public-methods | --max-public-methods | \
            --required-attributes | --bad-functions | --module-rgx | \
            --const-rgx | --class-rgx | --function-rgx | --method-rgx | \
            --attr-rgx | --argument-rgx | --variable-rgx | --inlinevar-rgx | \
            --good-names | --bad-names | --no-docstring-rgx | \
            --dummy-variables-rgx | --additional-builtins | --notes | \
            --ignored-classes | --generated-members | \
            --overgeneral-exceptions | --ignore-iface-methods | \
            --defining-attr-methods | --valid-classmethod-first-arg | \
            --valid-metaclass-classmethod-first-arg | -${noargopts}[h])
            return
            ;;
        --fail-on | --help-msg)
            _comp_cmd_pylint__message_ids "$1"
            return
            ;;
        --enable | -${noargopts}e)
            _comp_cmd_pylint__message_ids "$1" Disabled
            return
            ;;
        --disable | -${noargopts}d)
            _comp_cmd_pylint__message_ids "$1" Enabled
            _comp_compgen -a -- -W 'all'
            return
            ;;
        --rcfile)
            _comp_compgen_filedir
            return
            ;;
        --persistent | --include-ids | --symbols | --files-output | \
            --reports | --comment | --ignore-comments | --ignore-docstrings | \
            --ignore-imports | --init-import | --ignore-mixin-members | \
            --zope | --suggestion-mode | -${noargopts}[isr])
            _comp_compgen -- -W 'yes no'
            return
            ;;
        --load-plugins | --deprecated-modules)
            _comp_compgen -c "${cur##*,}" -x python modules $python
            ((${#COMPREPLY[@]})) &&
                _comp_delimited , -W '"${COMPREPLY[@]}"'
            return
            ;;
        --jobs | -${noargopts}j)
            local REPLY
            _comp_get_ncpus
            _comp_compgen -- -W "{1..$REPLY}"
            return
            ;;
        --confidence)
            local prefix=
            [[ $cur == *,* ]] && prefix="${cur%,*},"
            _comp_compgen -c "${cur##*,}" -- -W "HIGH INFERENCE
                INFERENCE_FAILURE UNDEFINED"
            ((${#COMPREPLY[@]} == 1)) &&
                _comp_compgen -Rv COMPREPLY -- -P "$prefix" -W '"$COMPREPLY"'
            return
            ;;
        --format | -${noargopts}f)
            _comp_compgen -- -W 'text parseable colorized json msvs'
            return
            ;;
        --import-graph | --ext-import-graph | --int-import-graph)
            _comp_compgen_filedir dot
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- --long-help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_set
    _comp_looks_like_path "$cur" || _comp_compgen -x python modules $python
    _comp_compgen -a filedir py
} &&
    complete -F _comp_cmd_pylint pylint pylint-2 pylint-3

# ex: filetype=sh
