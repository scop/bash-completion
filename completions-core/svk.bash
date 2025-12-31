# svk(1) completion                                        -*- shell-script -*-

_comp_cmd_svk()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local commands options command

    commands='add admin annotate ann blame praise cat checkout co cleanup
        cmerge cm commit ci copy cp delete del remove rm depotmap depot
        describe desc diff di help h ? import info list ls log merge mirror mi
        mkdir move mv ren rename patch propdel pd pdel propedit pe pedit
        propget pg pget proplist pl plist propset ps pset pull push resolved
        revert smerge sm status st stat switch sw sync sy update up verify'

    if ((cword == 1)); then
        if [[ $cur == -* ]]; then
            _comp_compgen -- -W '--version'
        else
            _comp_compgen -- -W "$commands"
        fi
    else
        case $prev in
            -F | --file | --targets)
                _comp_compgen_filedir
                return
                ;;
            --encoding)
                _comp_compgen -x iconv charsets
                return
                ;;
        esac

        command=${words[1]}

        if [[ $cur == -* ]]; then
            # possible options for the command
            case $command in
                add)
                    options=' --non-recursive -N -q --quiet'
                    ;;
                blame | annotate | ann | praise)
                    options='-r --revisions -x --cross'
                    ;;
                cat)
                    options='-r --revision'
                    ;;
                checkout | co)
                    options='-r --revision -q --quiet -N --non-recursive -l
                        --list -d --detach --export --relocate --purge'
                    ;;
                cleanup)
                    options='-a --all'
                    ;;
                cmerge | cm)
                    options='-c --change -l --log -r --revision -a --auto
                        --verbatim --no-ticket -m --message -F --file
                        --template --encoding -P --patch -S --sign -C
                        --check-only --direct'
                    ;;
                commit | ci)
                    options='--import -m --message -F --file --encoding
                        --template -P --patch -S --sign -C --check-only -N
                        --non-recursive --direct'
                    ;;
                copy | cp)
                    options='-r --revision -p --parent -q --quiet -m --message
                        -F --file --template --encoding -P --patch -S --sign -C
                        --check-only --direct'
                    ;;
                delete | del | remove | rm)
                    options='-k --keep-local -m --message -F --file --encoding
                        --template -P --patch -S --sign -C --check-only
                        --direct'
                    ;;
                depotmap | depot)
                    options='-i --init -l --list -d --detach --relocate'
                    ;;
                diff | di)
                    options='-r --revision -s --summarize -b --verbose -N
                        --non-recursive'
                    ;;
                import)
                    options='-f --from-checkout -t --to-checkout -m --message
                        -F --file --template --encoding -P --patch -S --sign -C
                        --check-only -N --non-recursive --direct'
                    ;;
                list | ls)
                    options='-r --revision -v --verbose -R --recursive -d
                        --depth -f --full-path'
                    ;;
                log)
                    options='-r --revision -l --limit -q --quiet -x --cross -v
                        --verbose'
                    ;;
                merge)
                    options='-r --revision -c --change -I --incremental -a
                        --auto -l --log -s --sync -t --to -f --from --verbatim
                        --no-ticket --track-rename -m --message -F --file
                        --template --encoding -P --patch -S --sign -C
                        --check-only --direct'
                    ;;
                mirror | mi)
                    options='-l --list -d --detach --relocate --recover
                        --unlock --upgrade'
                    ;;
                mkdir)
                    options='-p --parent -m --message -F --file --template
                        --encoding -P --patch -S --sign -C --check-only
                        --direct'
                    ;;
                move | mv | rename | ren)
                    options='-r --revision -p --parent -q --quiet -m --message
                        -F --file --encoding --template -P --patch -S --sign -C
                        --check-only --direct'
                    ;;
                patch)
                    options='--depot'
                    ;;
                propdel | propset | pdel | pset | pd | ps)
                    options='-R --recursive -r --revision --revprop -m
                        --message -F --file --template --encoding -P --patch -S
                        --sign -C --check-only -q --quiet --direct'
                    ;;
                propedit | pedit | pe)
                    options='-R --recursive -r --revision --revprop -m
                        --message -F --file --template --encoding -P --patch
                        -S --sign -C --check-only --direct'
                    ;;
                propget | pget | pg)
                    options='-R --recursive -r --revision --revprop --strict'
                    ;;
                proplist | plist | pl)
                    options='-R --recursive -v --verbose -r --revision
                        --revprop'
                    ;;
                pull)
                    options='-a --all -l --lump'
                    ;;
                push)
                    options='-f --from -l --lump -C --check -P --patch -S
                        --sign --verbatim'
                    ;;
                resolved)
                    options='-R --recursive'
                    ;;
                revert)
                    options='-R --recursive -q --quiet'
                    ;;
                smerge | sm)
                    options='-I --incremental -l --log -B --baseless -b --base
                        -s --sync -t --to -f --from --verbatim --no-ticket
                        --track-rename --host --remoterev -m --message -F
                        --file --template --encoding -P --patch -S --sign -C
                        --check-only --direct'
                    ;;
                status | stat | st)
                    options='-q --quiet --no-ignore -N --non-recursive -v
                        --verbose'
                    ;;
                switch | sw)
                    options='-r --revision -d --detach -q --quiet'
                    ;;
                sync | sy)
                    options='-a --all -s --skipto -t --torev'
                    ;;
                update | up)
                    options='-r --revision -N --non-recursive -C --check-only
                        -s --sync -m --merge -q --quiet'
                    ;;
            esac
            options+=" --help -h"

            _comp_compgen -- -W "$options"
        else
            case $command in
                help | h | \?)
                    _comp_compgen -- -W "$commands environment commands intro"
                    ;;
                admin)
                    _comp_compgen -- -W 'help deltify dump hotcopy list-dblogs
                        list-unused-dblogs load lstxns recover rmtxns setlog
                        verify rmcache'
                    ;;
                patch)
                    _comp_compgen -- -W '--ls --list --cat --view --regen
                        --regenerate --up --update --apply --rm --delete'
                    ;;
                sync)
                    _comp_compgen_split -- "$("$1" mirror --list \
                        2>/dev/null | _comp_awk '/^\//{print $1}')"
                    ;;
                co | checkout | push | pull)
                    if [[ $cur == //*/* ]]; then
                        path=${cur%/*}/
                    else
                        path=//
                    fi
                    _comp_compgen_split -- "$("$1" list "$path" 2>/dev/null |
                        command sed -e 's|\(.*\)|'"$path"'\1|')"
                    ;;
                *)
                    _comp_compgen_filedir
                    ;;
            esac
        fi
    fi
} &&
    complete -F _comp_cmd_svk svk

# ex: filetype=sh
