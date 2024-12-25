# mfiutil completion                                       -*- shell-script -*-

[[ $OSTYPE == *@(freebsd|dragonflybsd|darwin|linux|solaris)* ]] || return 1

_comp_cmd_mfiutil()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        # Complete global options
        local options="-u -d -e"
        case "$OSTYPE" in
            *freebsd*)
                options+=" -D -t"
                ;;
            *dragonflybsd* | *solaris*)
                options+=" -t"
                ;;
        esac
        local end_of_options=
        local w
        for w in "${words[@]:1:cword-1}"; do
            case "$w" in
                --)
                    end_of_options=set
                    break
                    ;;
                -*) ;;
                *)
                    end_of_options=set
                    break
                    ;;
            esac
        done
        if [[ ! $end_of_options ]]; then
            _comp_compgen -- -W '$options'
            return
        fi
    fi

    local REPLY
    _comp_count_args -a "-*[Dtu]"
    case $REPLY in
        0)
            # Complete argument to global options
            case "$prev" in
                -D)
                    _comp_compgen_filedir
                    ;;
                -t)
                    case "$OSTYPE" in
                        *freebsd* | *dragonflybsd*)
                            _comp_compgen -- -W 'mfi mrsas'
                            ;;
                    esac
                    ;;
            esac
            ;;
        1)
            _comp_compgen -- -W '
                version show fail good rebuild syspd drive start abort locate
                cache name volume clear create delete add remove patrol stop
                foreign flash bbu ctrlprop'
            ;;
        2)
            case "$prev" in
                show)
                    _comp_compgen -- -W '
                        adapter battery config drives events firmware foreign
                        logstate volumes patrol progress'
                    ;;
                drive)
                    _comp_compgen -- -W 'progress clear'
                    ;;
                start)
                    _comp_compgen -- -W 'rebuild patrol learn'
                    ;;
                abort)
                    _comp_compgen -- -W 'rebuild'
                    ;;
                volume)
                    _comp_compgen -- -W 'progress'
                    ;;
                create)
                    _comp_compgen -- -W '
                        jbod raid0 raid1 raid5 raid6 raid10 raid50 raid60 concat'
                    ;;
                patrol)
                    _comp_compgen -- -W 'disable auto manual'
                    ;;
                stop)
                    _comp_compgen -- -W 'patrol'
                    ;;
                foreign)
                    _comp_compgen -- -W 'scan clear diag preview import'
                    ;;
                flash)
                    _comp_compgen_filedir
                    ;;
                bbu)
                    _comp_compgen -- -W 'learn-delay autolearn-mode bbu-mode'
                    ;;
                ctrlprop)
                    _comp_compgen -- -W 'rebuild alarm'
                    ;;
            esac
            ;;
        3)
            case "${words[cword - 2]}.$prev" in
                locate.*)
                    _comp_compgen -- -W 'on off'
                    ;;
                cache.*)
                    _comp_compgen -- -W '
                        enable disable reads writes write-back write-through
                        read-ahead bad-bbu-write-cache write-cache'
                    ;;
                ctrlprop.alarm)
                    _comp_compgen -- -W 'on off 1 0'
                    ;;
            esac
            ;;
    esac
} &&
    complete -F _comp_cmd_mfiutil mfiutil mrsasutil
