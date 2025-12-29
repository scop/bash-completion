# svnlook completion                                       -*- shell-script -*-

# Use of this file is deprecated.  Upstream completion is available in
# subversion >= 0.12.0, use that instead.

_comp_cmd_svnlook()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local commands
    commands='author cat changed date diff dirs-changed help ? h history info
        lock log propget pget pg proplist plist pl tree uuid youngest'

    if ((cword == 1)); then
        if [[ $cur == -* ]]; then
            _comp_compgen -- -W '--version'
        else
            _comp_compgen -- -W "$commands"
        fi
    else
        local command=${words[1]}

        if [[ $cur == -* ]]; then
            # possible options for the command
            local options
            case $command in
                author | cat | date | dirs-changed | info | log)
                    options='--revision --transaction'
                    ;;
                changed)
                    options='--revision --transaction --copy-info'
                    ;;
                diff)
                    options='--revision --transaction --no-diff-deleted
                        --no-diff-added --diff-copy-from'
                    ;;
                history)
                    options='--revision --show-ids'
                    ;;
                propget | proplist)
                    options='--revision --transaction --revprop'
                    ;;
                tree)
                    options='--revision --transaction --show-ids --full-paths'
                    ;;
            esac

            options+=" --help"
            _comp_compgen -- -W "$options"
        else
            if [[ $command == @(help|[h?]) ]]; then
                _comp_compgen -- -W "$commands"
            else
                _comp_compgen_filedir
            fi
        fi
    fi

} &&
    complete -F _comp_cmd_svnlook -o default svnlook

# ex: filetype=sh
