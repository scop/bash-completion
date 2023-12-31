# bash completion for aspell                               -*- shell-script -*-

_comp_cmd_aspell__dictionary()
{
    local datadir aspell=$1
    datadir=$("$aspell" config data-dir 2>/dev/null || echo /usr/lib/aspell)
    # First, get aliases (dicts dump does not list them)
    if _comp_expand_glob COMPREPLY '"$datadir"/*.alias'; then
        COMPREPLY=("${COMPREPLY[@]%.alias}")
        COMPREPLY=("${COMPREPLY[@]#$datadir/}")
    fi
    # Then, add the canonical dicts
    _comp_split -a COMPREPLY "$("$aspell" dicts 2>/dev/null)"
    ((${#COMPREPLY[@]})) &&
        _comp_compgen -- -X '\*' -W '"${COMPREPLY[@]}"'
}

_comp_cmd_aspell()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -c | -p | check | --conf | --personal | --repl | --per-conf)
            _comp_compgen_filedir
            return
            ;;
        --conf-dir | --data-dir | --dict-dir | --home-dir | --local-data-dir | --prefix)
            _comp_compgen_filedir -d
            return
            ;;
        dump | create | merge)
            _comp_compgen -- -W 'master personal repl'
            return
            ;;
        --mode)
            _comp_compgen_split -- "$("$1" modes 2>/dev/null |
                _comp_awk '{ print $1 }')"
            return
            ;;
        --sug-mode)
            _comp_compgen -- -W 'ultra fast normal bad-speller'
            return
            ;;
        --keymapping)
            _comp_compgen -- -W 'aspell ispell'
            return
            ;;
        -d | --master)
            _comp_cmd_aspell__dictionary "$1"
            return
            ;;
        --add-filter | --rem-filter)
            _comp_compgen_split -- "$("$1" filters 2>/dev/null |
                _comp_awk '{ print $1 }')"
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--conf= --conf-dir= --data-dir= --dict-dir=
            --encoding= --add-filter= --rem-filter= --mode= --add-extra-dicts=
            --rem-extra-dicts= --home-dir= --ignore= --ignore-accents
            --dont-ignore-accents --ignore-case --dont-ignore-case
            --ignore-repl --dont-ignore-repl --jargon --keyboard= --lang=
            --language-tag --local-data-dir= --master= --module
            --add-module-search-order --rem-module-search-order --per-conf=
            --personal= --prefix= --repl= --run-together --dont-run-together
            --run-together-limit= --run-together-min= --save-repl
            --dont-save-repl --set-prefix --dont-set-prefix --size= --spelling
            --strip-accents --dont-strip-accents --sug-mode=
            --add-word-list-path --rem-word-list-path --backup --dont-backup
            --reverse --dont-reverse --time --dont-time --keymapping=
            --add-email-quote= --rem-email-quote= --email-margin=
            --add-tex-command= --rem-tex-command= --tex-check-comments
            --dont-tex-check-comments --add-tex-extension --rem-tex-extension
            --add-sgml-check= --rem-sgml-check= --add-sgml-extension
            --rem-sgml-extension'
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        _comp_compgen -- -W 'usage help check pipe list config soundslike
            filter version dump create merge'
    fi
} &&
    complete -F _comp_cmd_aspell aspell

# ex: filetype=sh
