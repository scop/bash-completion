# jq(1) completion                                         -*- shell-script -*-

_comp_cmd_jq()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[fL]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | --arg | --argjson | --slurpfile | --argfile)
            return
            ;;
        --indent)
            _comp_compgen -- -W '{1..8}'
            return
            ;;
        --from-file | --run-tests | -${noargopts}f)
            _comp_compgen_filedir
            return
            ;;
        -${noargopts}L)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    ((cword > 2)) &&
        case ${words[cword - 2]} in
            --arg | --argjson)
                return
                ;;
            --slurpfile | --argfile)
                _comp_compgen_filedir 'json?(l)'
                return
                ;;
        esac

    if [[ $cur == -* ]]; then
        # Get jq's --help output and see whether it mentions --help
        # jq's --help only shows some of its command-line options; some are not
        # even listed in the man page!
        local help_output=$("$1" --help 2>/dev/null)

        if [[ $help_output == *--help* ]]; then
            # If the output of --help seems complete, use it
            _comp_compgen_help - <<<"$help_output"
        else
            # Otherwise, use a hard-coded list of known flags, some of which do
            # not appear in the output of --help as of jq 1.6.
            _comp_compgen -- -W '--version --seq --stream --slurp --raw-input
                --null-input --compact-output --tab --indent --color-output
                -monochrome-output --ascii-output --unbuffered --sort-keys
                --raw-output --join-output --from-file --exit-status --arg
                --argjson --slurpfile --rawfile --argfile --args --jsonargs
                --run-tests --help'
        fi
        return
    fi

    local word
    for word in "${words[@]}"; do
        [[ $word != --?(json)args ]] || return
    done

    local REPLY
    # TODO: DTRT with args taking 2 options
    # -f|--from-file are not counted here because they supply the filter
    _comp_count_args -a "@(--arg|--arg?(json|file)|--slurpfile|--indent|--run-tests|-${noargopts}L)"

    # 1st arg is filter
    ((REPLY == 1)) && return
    # 2... are input files
    _comp_compgen_filedir 'json?(l)'

} &&
    complete -F _comp_cmd_jq jq

# ex: filetype=sh
