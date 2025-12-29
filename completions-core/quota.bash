# bash completion for quota-tools                          -*- shell-script -*-

_comp_cmd_quota__user_or_group()
{
    local i

    # complete on groups if -g was given
    for ((i = 1; i < cword; i++)); do
        if [[ ${words[i]} == -@(g|-group) ]]; then
            _comp_compgen -- -g
            return
        fi
    done

    # otherwise complete on users
    _comp_compgen -- -u
}

_comp_cmd_quota__parse_help()
{
    _comp_compgen_help || _comp_compgen_usage
    [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
}

_comp_cmd_quota__formats()
{
    _comp_compgen -- -W 'vfsold vfsv0 rpc xfs'
}

_comp_cmd_quota__filesystems()
{
    #  Only list filesystems starting with "/", otherwise we also get
    #+ "binfmt_misc", "proc", "tmpfs", ...
    _comp_compgen_split -- "$(_comp_awk '/^\// {print $1}' /etc/mtab)"
}

_comp_cmd_quota()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -F | --format)
            _comp_cmd_quota__formats
            return
            ;;
        -h | --help | -V | --version)
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_cmd_quota__parse_help "$1"
    else
        _comp_cmd_quota__user_or_group
    fi
} &&
    complete -F _comp_cmd_quota -o default quota

_comp_cmd_setquota()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -F | --format)
            _comp_cmd_quota__formats
            return
            ;;
        -p | --prototype)
            _comp_cmd_quota__user_or_group
            return
            ;;
        -h | --help | -V | --version)
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_cmd_quota__parse_help "$1"
    else
        local REPLY
        _comp_count_args

        case $REPLY in
            1)
                _comp_cmd_quota__user_or_group
                ;;
            2)
                _comp_cmd_quota__filesystems
                ;;
        esac

    fi
} &&
    complete -F _comp_cmd_setquota -o default setquota

_comp_cmd_edquota()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -F | --format)
            _comp_cmd_quota__formats
            return
            ;;
        -f | --filesystem)
            _comp_cmd_quota__filesystems
            return
            ;;
        -p | --prototype)
            _comp_cmd_quota__user_or_group
            return
            ;;
        -h | --help | -V | --version)
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_cmd_quota__parse_help "$1"
    else
        _comp_cmd_quota__user_or_group
    fi
} &&
    complete -F _comp_cmd_edquota -o default edquota

_comp_cmd_quotacheck()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -F | --format)
            _comp_cmd_quota__formats
            return
            ;;
        -h | --help | -V | --version)
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_cmd_quota__parse_help "$1"
    else
        _comp_cmd_quota__filesystems
    fi
} &&
    complete -F _comp_cmd_quotacheck -o default quotacheck repquota

_comp_cmd_quotaon()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -F | --format)
            _comp_cmd_quota__formats
            return
            ;;
        -x | --xfs-command)
            _comp_compgen -- -W 'delete enforce'
            return
            ;;
        -h | --help | -V | --version)
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_cmd_quota__parse_help "$1"
    else
        _comp_cmd_quota__filesystems
    fi
} &&
    complete -F _comp_cmd_quotaon -o default quotaon quotaoff

# ex: filetype=sh
