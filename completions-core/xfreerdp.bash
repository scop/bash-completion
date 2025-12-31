# xfreerdp completion                                      -*- shell-script -*-

_comp_cmd_xfreerdp__kbd_list()
{
    local kbd_list
    # Trying non deprecated /list:kbd first
    kbd_list=$("$1" /list:kbd 2>/dev/null) ||
        # Old syntax, deprecated in 2022-10-19
        # See https://github.com/FreeRDP/FreeRDP/commit/119b8d4474ab8578101f86226e0d20a53460dd51
        kbd_list=$("$1" /kbd-list 2>/dev/null) ||
        # This seems to have broken in 2020 by commit
        # https://github.com/FreeRDP/FreeRDP/commit/30275e7ac3eedf4db1b8fb1c0cb81f03e630ee8a,
        # see https://github.com/scop/bash-completion/pull/1380#issuecomment-2870229302
        # but is seemingly the only way to list the keyboard layout in 1.0.2, which is
        # the version in ubuntu 14.04.6
        kbd_list=$("$1" --kbd-list 2>/dev/null)
    _comp_awk '/^0x/ { print $1 }' <<<"$kbd_list"
}

_comp_cmd_xfreerdp()
{
    local cur prev words cword comp_args
    _comp_initialize -n : -- "$@" || return

    case $prev in
        -k)
            _comp_compgen_split -- "$(_comp_cmd_xfreerdp__kbd_list "$1")"
            return
            ;;
        -a)
            _comp_compgen -- -W '8 15 16 24 32'
            return
            ;;
        -x)
            _comp_compgen -- -W 'broadband modem lan'
            return
            ;;
        --plugin)
            _comp_compgen -- -W 'cliprdr rdpsnd rdpdr'
            return
            ;;
        /help | /version | -h | --help | --version)
            return
            ;;
    esac

    case $cur in
        /kbd:*)
            _comp_compgen -c "${cur#/kbd:}" split -- "$(_comp_cmd_xfreerdp__kbd_list "$1")"
            return
            ;;
        /bpp:*)
            _comp_compgen -c "${cur#/bpp:}" -- -W '8 15 16 24 32'
            return
            ;;
        /*:*)
            return
            ;;
    esac

    if [[ $cur == /* ]]; then
        _comp_compgen_filedir rdp
        _comp_compgen -a split -- "$(
            "$1" --help | _comp_awk '$1 ~ /^\// && $1 !~ /^.(flag$|option:)/ {
                sub(":.*",":",$1); print $1 }'
        )"
        [[ ${COMPREPLY-} == *: ]] && compopt -o nospace
    elif [[ $cur == [+-]* ]]; then
        local char=${cur:0:1}
        local help="$("$1" --help)"
        if [[ $help == */help* ]]; then # new/slash syntax
            _comp_compgen_split -- "$(_comp_awk '$1 ~ /^[+-]/ && $1 !~ /^.toggle$/ {
                    sub("^.","'"$char"'",$1); print $1 }' <<<"$help")"
        else # old/dash syntax
            _comp_compgen -R help - <<<"$help"
            ((${#COMPREPLY[@]})) &&
                _comp_compgen -- -W '"${COMPREPLY[@]%:}"'
        fi
    else
        _comp_compgen_filedir rdp
        _comp_compgen -a split -- "$(
            _comp_awk '{print $1}' ~/.freerdp/known_hosts 2>/dev/null
        )"
    fi

} &&
    complete -F _comp_cmd_xfreerdp xfreerdp

# ex: filetype=sh
