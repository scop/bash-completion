# svn completion                                           -*- shell-script -*-

# Use of this file is deprecated.  Upstream completion is available in
# subversion >= 0.12.0, use that instead.

_comp_cmd_svn()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local commands
    commands='add blame praise annotate ann cat checkout co cleanup commit \
                ci copy cp delete del remove rm diff di export help ? h import \
                info list ls lock log merge mkdir move mv rename ren \
                propdel pdel pd propedit pedit pe propget pget pg \
                proplist plist pl propset pset ps resolved revert \
                status stat st switch sw unlock update up'

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
            -F | --file | --targets)
                _comp_compgen_filedir
                return
                ;;
            --encoding)
                _comp_compgen -x iconv charsets
                return
                ;;
            --editor-cmd | --diff-cmd | --diff3-cmd)
                _comp_compgen_commands
                return
                ;;
        esac

        local command=${words[1]}

        if [[ $cur == -* ]]; then
            # possible options for the command
            local options
            case $command in
                add)
                    options='--auto-props --no-auto-props --force --targets
                        --no-ignore --non-recursive --quiet'
                    ;;
                blame | annotate | ann | praise)
                    options='--revision --username --password --no-auth-cache
                        --non-interactive --verbose --incremental --xml'
                    ;;
                cat)
                    options='--revision --username --password --no-auth-cache
                        --non-interactive'
                    ;;
                checkout | co)
                    options='--revision --quiet --non-recursive --username
                        --password --no-auth-cache --non-interactive
                        --ignore-externals'
                    ;;
                cleanup)
                    options='--diff3-cmd'
                    ;;
                commit | ci)
                    options='--message --file --encoding --force-log --quiet
                        --non-recursive --targets --editor-cmd --username
                        --password --no-auth-cache --non-interactive
                        --no-unlock'
                    ;;
                copy | cp)
                    options='--message --file --encoding --force-log --revision
                        --quiet --editor-cmd -username --password
                        --no-auth-cache --non-interactive'
                    ;;
                delete | del | remove | rm)
                    options='--force --message --file --encoding --force-log
                        --quiet --targets --editor-cmd --username
                        --password --no-auth-cache --non-interactive'
                    ;;
                diff | di)
                    options='--revision --extensions --diff-cmd
                        --no-diff-deleted --non-recursive --username
                        --password --no-auth-cache --non-interactive
                        --force --old --new --notice-ancestry'
                    ;;
                export)
                    options='--revision --quiet --username --password
                        --no-auth-cache --non-interactive --non-recursive
                        --force --native-eol --ignore-externals'
                    ;;
                import)
                    options='--auto-props --no-auto-props --message --file
                        --encoding --force-log --quiet --non-recursive
                        --no-ignore --editor-cmd --username --password
                        --no-auth-cache --non-interactive'
                    ;;
                info)
                    options='--username --password --no-auth-cache
                        --non-interactive --revision --xml --targets
                        --recursive --incremental'
                    ;;
                list | ls)
                    options='--revision --verbose --recursive --username
                        --password --no-auth-cache --non-interactive
                        --incremental --xml'
                    ;;
                lock)
                    options='--message --file --encoding --force-log --targets
                        --force --username --password --no-auth-cache
                        --non-interactive'
                    ;;
                log)
                    options='--revision --verbose --targets --username
                        --password --no-auth-cache --non-interactive
                        --stop-on-copy --incremental --xml --quiet
                        --limit'
                    ;;
                merge)
                    options='--revision --non-recursive --quiet --force
                        --dry-run --diff3-cmd --username --password
                        --no-auth-cache --non-interactive
                        --ignore-ancestry'
                    ;;
                mkdir)
                    options='--message --file --encoding --force-log --quiet
                        --editor-cmd --username --password --no-auth-cache
                        --non-interactive'
                    ;;
                move | mv | rename | ren)
                    options='--message --file --encoding --force-log --revision
                        --quiet --force --editor-cmd --username --password
                        --no-auth-cache --non-interactive'
                    ;;
                propdel | pdel | pd)
                    options='--quiet --recursive --revision --revprop
                        --username --password --no-auth-cache
                        --non-interactive'
                    ;;
                propedit | pedit | pe)
                    options='--revision --revprop --encoding --editor-cmd
                        --username --password --no-auth-cache
                        --non-interactive --force'
                    ;;
                propget | pget | pg)
                    options='--recursive --revision --revprop --strict
                        --username --password --no-auth-cache
                        --non-interactive'
                    ;;
                proplist | plist | pl)
                    options='--verbose --recursive --revision --revprop --quiet
                        --username --password --no-auth-cache
                        --non-interactive'
                    ;;
                propset | pset | ps)
                    options='--file --quiet --targets --recursive --revprop
                        --encoding --username --password --no-auth-cache
                        --non-interactive --revision --force'
                    ;;
                resolved)
                    options='--targets --recursive --quiet'
                    ;;
                revert)
                    options='--targets --recursive --quiet'
                    ;;
                status | stat | st)
                    options='--show-updates --verbose --non-recursive --quiet
                        --username --password --no-auth-cache
                        --non-interactive --no-ignore --ignore-externals
                        --incremental --xml'
                    ;;
                switch | sw)
                    options='--relocate --revision --non-recursive --quiet
                        --username --password --no-auth-cache
                        --non-interactive --diff3-cmd'
                    ;;
                unlock)
                    options='--targets --force --username --password
                        --no-auth-cache --non-interactive'
                    ;;
                update | up)
                    options='--revision --non-recursive --quiet --username
                        --password --no-auth-cache --non-interactive
                        --diff3-cmd --ignore-externals'
                    ;;
            esac
            options+=" --help --config-dir"

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
    complete -F _comp_cmd_svn svn

# ex: filetype=sh
