# pack200(1) completion                                    -*- shell-script -*-

_comp_cmd_pack200()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -S | --segment-limit | -P | --pass-file | -C | --class-attribute | \
            -F | --field-attribute | -M | --method-attribute | -D | \
            --code-attribute | '-?' | -h | --help | -V | --version | -J)
            return
            ;;
        -E | --effort)
            _comp_compgen -- -W '{0..9}'
            return
            ;;
        -H | --deflate-hint)
            _comp_compgen -- -W 'true false keep'
            return
            ;;
        -m | --modification-time)
            _comp_compgen -- -W 'latest keep'
            return
            ;;
        -U | --unknown-attribute)
            _comp_compgen -- -W 'error strip pass'
            return
            ;;
        -f | --config-file)
            _comp_compgen_filedir properties
            return
            ;;
        -l | --log-file)
            _comp_compgen -- -W '-'
            _comp_compgen -a filedir log
            return
            ;;
        -r | --repack)
            _comp_compgen_filedir jar
            return
            ;;
    esac

    [[ $was_split ]] && return

    # Check if a pack or a jar was already given.
    local i pack="" jar=""
    for ((i = 1; i < cword; i++)); do
        case ${words[i]} in
            *.pack | *.pack.gz) pack=set ;;
            *.jar) jar=set ;;
        esac
    done

    if [[ ! $pack ]]; then
        if [[ $cur == -* ]]; then
            _comp_compgen -- -W '--no-gzip --gzip --strip-debug
                --no-keep-file-order --segment-limit= --effort= --deflate-hint=
                --modification-time= --pass-file= --unknown-attribute=
                --class-attribute= --field-attribute= --method-attribute=
                --code-attribute= --config-file= --verbose --quiet --log-file=
                --help --version -J --repack'
            [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        else
            _comp_compgen_filedir 'pack?(.gz)'
        fi
    elif [[ ! $jar ]]; then
        _comp_compgen_filedir jar
    fi
} &&
    complete -F _comp_cmd_pack200 pack200

# ex: filetype=sh
