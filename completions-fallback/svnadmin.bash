# svnadmin completion                                      -*- shell-script -*-

# Use of this file is deprecated.  Upstream completion is available in
# subversion >= 0.12.0, use that instead.

_comp_cmd_svnadmin()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local commands
    commands='create deltify dump help ? hotcopy list-dblogs list-unused-dblogs
        load lslocks lstxns recover rmlocks rmtxns setlog verify'

    if ((cword == 1)); then
        if [[ $cur == -* ]]; then
            _comp_compgen -- -W '--version'
        else
            _comp_compgen -- -W "$commands"
        fi
    else
        case $prev in
            --config-dir)
                _comp_compgen_filedir -d
                return
                ;;
            --fs-type)
                _comp_compgen -- -W 'fsfs bdb'
                return
                ;;
        esac

        local command=${words[1]}

        if [[ $cur == -* ]]; then
            # possible options for the command
            local options
            case $command in
                create)
                    options='--bdb-txn-nosync --bdb-log-keep --config-dir
                        --fs-type'
                    ;;
                deltify)
                    options='--revision --quiet'
                    ;;
                dump)
                    options='--revision --incremental --quiet --deltas'
                    ;;
                hotcopy)
                    options='--clean-logs'
                    ;;
                load)
                    options='--ignore-uuid --force-uuid --parent-dir --quiet
                        --use-pre-commit-hook --use-post-commit-hook'
                    ;;
                rmtxns)
                    options='--quiet'
                    ;;
                setlog)
                    options='--revision --bypass-hooks'
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
    complete -F _comp_cmd_svnadmin -o default svnadmin

# ex: filetype=sh
