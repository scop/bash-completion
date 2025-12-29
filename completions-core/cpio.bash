# bash completion for cpio                                 -*- shell-script -*-

_comp_cmd_cpio()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -n : -- "$@" || return

    # --name value style option
    local noargopts='!(-*|*[HEFIR]*)'
    # shellcheck disable=SC2254
    case $prev in
        --format | -${noargopts}H)
            _comp_compgen -- -W 'bin odc newc crc tar ustar hpbin hpodc'
            return
            ;;
        --file | --pattern-file | -${noargopts}[EFI])
            _comp_compgen_filedir
            return
            ;;
        --owner | -${noargopts}R)
            _comp_compgen_usergroups
            return
            ;;
        --rsh-command)
            _comp_compgen_commands
            return
            ;;
    esac

    [[ $was_split ]] && return

    if ((cword == 1)); then
        _comp_compgen -- -W '-o --create -i --extract -p --pass-through -?
            --help --license --usage --version'
    else
        case ${words[1]} in
            -o | --create)
                if [[ $cur == -* ]]; then
                    _comp_compgen -- -W '-0 -a -c -v -A -B -L -V -C -H -M -O -F
                        --file --format --message --null --reset-access-time
                        --verbose --dot --append --block-size --dereference
                        --io-size --quiet --force-local --rsh-command --help
                        --version'
                fi
                ;;
            -i | --extract)
                if [[ $cur == -* ]]; then
                    _comp_compgen -- -W '-b -c -d -f -m -n -r -t -s -u -v -B -S
                        -V -C -E -H -M -R -I -F --file --make-directories
                        --nonmatching --preserve-modification-time
                        --numeric-uid-gid --rename --list --swap-bytes --swap
                        --dot --unconditional --verbose --block-size
                        --swap-halfwords --io-size --pattern-file --format
                        --owner --no-preserve-owner --message --force-local
                        --no-absolute-filenames --sparse --only-verify-crc
                        --quiet --rsh-command --help --to-stdout --version'
                fi
                ;;
            -p* | --pass-through)
                if [[ $cur == -* ]]; then
                    _comp_compgen -- -W '-0 -a -d -l -m -u -v -L -V -R --null
                        --reset-access-time --make-directories --link --quiet
                        --preserve-modification-time --unconditional --verbose
                        --dot --dereference --owner --no-preserve-owner
                        --sparse --help --version'
                else
                    _comp_compgen_filedir -d
                fi
                ;;
        esac
    fi
} &&
    complete -F _comp_cmd_cpio cpio

# ex: filetype=sh
