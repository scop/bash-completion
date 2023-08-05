# tune2fs(8) completion                                    -*- shell-script -*-

_comp_cmd_tune2fs()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*[cCEiJLmrT])
            return
            ;;
        -*e)
            _comp_compgen -- -W 'continue remount-ro panic'
            return
            ;;
        -*g)
            _comp_compgen_gids
            _comp_compgen -a -- -g
            return
            ;;
        -*M)
            _comp_compgen_filedir -d
            return
            ;;
        -*o)
            local -a opts=(^debug ^bsdgroups ^user_xattr ^acl ^uid16
                ^journal_data ^journal_data_ordered ^journal_data_writeback
                ^nobarrier ^block_validity ^discard ^nodelalloc)
            _comp_compgen -- -W '"${opts[@]}" "${opts[@]#^}"'
            return
            ;;
        -*O)
            local -a opts=(^dir_index ^dir_nlink ^encrypt ^extent ^extra_isize
                ^filetype ^flex_bg ^has_journal ^huge_file ^large_file
                ^metadata_csum ^mmp ^project ^quota ^read-only ^resize_inode
                ^sparse_super ^uninit_bg)
            _comp_compgen -- -W '"${opts[@]}" "${opts[@]#^}"'
            return
            ;;
        -*u)
            _comp_compgen_uids
            _comp_compgen -a -- -u
            return
            ;;
        -*U)
            _comp_compgen -- -W 'clear random time'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
        return
    fi

    _comp_compgen -c "${cur:-/dev/}" filedir
} &&
    complete -F _comp_cmd_tune2fs tune2fs

# ex: filetype=sh
