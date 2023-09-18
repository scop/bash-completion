# bash completion for mdadm                                -*- shell-script -*-

_comp_cmd_mdadm__raid_level()
{
    local mode=""

    local i noargopts='!(-*|*[CB]*)'
    for ((i = 1; i < cword; i++)); do
        # shellcheck disable=SC2254
        case ${words[i]} in
            -${noargopts}C* | --create)
                mode=create
                break
                ;;
            -${noargopts}B* | --build)
                mode=build
                break
                ;;
        esac
    done

    case $mode in
        create)
            _comp_compgen -- -W 'linear raid0 0 stripe raid1 1 mirror raid4 4
                raid5 5 raid6 6 raid10 10 multipath mp faulty'
            ;;
        build)
            _comp_compgen -- -W 'linear stripe raid0 0 raid1 multipath mp
                faulty'
            ;;
    esac
}

_comp_cmd_mdadm__raid_layout()
{
    local i level=""
    for ((i = 1; i < cword; i++)); do
        if [[ ${words[i]} == -@(l|-level) ]]; then
            level=${words[i + 1]}
            break
        fi
    done

    case $level in
        raid5)
            _comp_compgen -- -W 'left-asymmetric left-symmetric
                right-asymmetric right-symmetric la ra ls rs'
            ;;
        raid10)
            _comp_compgen -- -W 'n o p'
            ;;
        faulty)
            _comp_compgen -- -W 'write-transient wt read-transient rt
                write-persistent wp read-persistent rp write-all read-fixable
                rf clear flush none'
            ;;
    esac
}

_comp_cmd_mdadm__auto_flag()
{
    _comp_compgen -- -W 'no yes md mdp part p'
}

_comp_cmd_mdadm__update_flag()
{
    _comp_compgen -- -W 'sparc2.2 summaries uuid name homehost resync byteorder
        super-minor'
}

_comp_cmd_mdadm()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[cblpaU]*)'
    # shellcheck disable=SC2254
    case $prev in
        --config | --bitmap | --backup-file | -${noargopts}[cb])
            _comp_compgen_filedir
            return
            ;;
        --level | -${noargopts}l)
            _comp_cmd_mdadm__raid_level
            return
            ;;
        --layout | --parity | -${noargopts}p)
            _comp_cmd_mdadm__raid_layout
            return
            ;;
        --auto | -${noargopts}a)
            _comp_cmd_mdadm__auto_flag
            return
            ;;
        --update | -${noargopts}U)
            _comp_cmd_mdadm__update_flag
            return
            ;;
    esac

    [[ $was_split ]] && return

    local options='--help --help-options --version --verbose --quiet --brief
        --force --config= --scan --metadata= --homehost='

    if [[ $cur == -* ]]; then
        if ((cword == 1)); then
            _comp_compgen -- -W "$options --assemble --build --create --monitor
                --grow"
        else
            # shellcheck disable=SC2254
            case ${words[cword - 1]} in
                --assemble | -${noargopts}A*)
                    _comp_compgen -- -W "$options --uuid= --super-minor=
                        --name= --force --run --no-degraded --auto= --bitmap=
                        --backup-file= --update= --auto-update-homehost"
                    ;;
                --build | --create | --grow | -${noargopts}[BCG]*)
                    _comp_compgen -- -W "$options --raid-devices=
                        --spare-devices= --size= --chunk= --rounding= --level=
                        --layout= --parity= --bitmap= --bitmap-chunk=
                        --write-mostly --write-behind= --assume-clean
                        --backup-file= --name= --run --force --auto="
                    ;;
                --follow | --monitor | -${noargopts}F)
                    _comp_compgen -- -W "$options --mail --program --alert
                        --syslog --delay --daemonise --pid-file --oneshot
                        --test"

                    ;;
                /dev/* | --add | --fail | --remove)
                    _comp_compgen -- -W "$options --add --re-add --remove
                        --fail --set-faulty"
                    ;;
                *)
                    _comp_compgen -- -W "$options --query --detail --examine
                        --sparc2.2 --examine-bitmap --run --stop --readonly
                        --readwrite --zero-superblock --test"
                    ;;
            esac
        fi
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        _comp_compgen -c "${cur:-/dev/}" filedir
    fi
} &&
    complete -F _comp_cmd_mdadm mdadm

# ex: filetype=sh
