# yum(8) completion                                        -*- shell-script -*-

# Use of this file is deprecated.  Upstream completion is available in
# yum > 3.2.25, use that instead.

_comp_cmd_yum__list()
{
    if [[ $1 == all ]]; then
        # Try to strip in between headings like "Available Packages"
        # This will obviously only work for English :P
        _comp_split COMPREPLY "$(yum -d 0 -C list "$1" "$cur*" 2>/dev/null |
            command sed -ne '/^Available /d' -e '/^Installed /d' \
                -e '/^Updated /d' -e 's/[[:space:]].*//p')"
    else
        # Drop first line (e.g. "Updated Packages")
        _comp_split COMPREPLY "$(yum -d 0 -C list "$1" "$cur*" 2>/dev/null |
            command sed -ne 1d -e 's/[[:space:]].*//p')"
    fi
}

_comp_cmd_yum__compgen_repolist()
{
    # -d 0 causes repolist to output nothing as of yum 3.2.22:
    # http://yum.baseurl.org/ticket/83
    # Drop first ("repo id      repo name") and last ("repolist: ...") rows
    _comp_compgen_split -- "$(
        yum --noplugins -C repolist "$1" 2>/dev/null |
            command sed -ne '/^repo[[:space:]]\{1,\}id/d' -e '/^repolist:/d' \
                -e 's/[[:space:]].*//p'
    )"
}

_comp_cmd_yum__compgen_plugins()
{
    local -a files
    _comp_expand_glob files '/usr/lib/yum-plugins/*.py{,c,o}' || return
    _comp_compgen -U files split -- "$(
        printf '%s\n' "${files[@]}" |
            command sed -ne 's|.*/\([^./]*\)\.py[co]\{0,1\}$|\1|p' | sort -u
    )"
}

_comp_cmd_yum()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local special="" i
    for ((i = 1; i < cword; i++)); do
        if [[ ${words[i]} == @(install|update|upgrade|remove|erase|deplist|info) ]]; then
            special=${words[i]}
            break
        fi
    done

    if [[ $special ]]; then
        # TODO: install|update|upgrade should not match *src.rpm
        if [[ $cur == @(*/|[.~])* &&
            $special == @(deplist|install|update|upgrade) ]]; then
            _comp_compgen_filedir rpm
            return
        fi
        case $special in
            install)
                _comp_cmd_yum__list available
                return
                ;;
            deplist | info)
                _comp_cmd_yum__list all
                return
                ;;
            upgrade | update)
                _comp_cmd_yum__list updates
                return
                ;;
            remove | erase)
                # _comp_xfunc_rpm_installed_packages is not arch-qualified
                _comp_cmd_yum__list installed
                return
                ;;
        esac
    fi

    case $prev in
        list)
            _comp_compgen -- -W 'all available updates installed extras
                obsoletes recent'
            ;;
        clean)
            _comp_compgen -- -W 'packages headers metadata cache dbcache all'
            ;;
        repolist)
            _comp_compgen -- -W 'all enabled disabled'
            ;;
        localinstall | localupdate)
            # TODO: should not match *src.rpm
            _comp_compgen_filedir rpm
            ;;
        -d | -e)
            _comp_compgen -- -W '{0..10}'
            ;;
        -c)
            _comp_compgen_filedir
            ;;
        --installroot)
            _comp_compgen_filedir -d
            ;;
        --enablerepo)
            _comp_cmd_yum__compgen_repolist disabled
            ;;
        --disablerepo)
            _comp_cmd_yum__compgen_repolist enabled
            ;;
        --disableexcludes)
            _comp_cmd_yum__compgen_repolist all
            _comp_compgen -a -- -W "all main"
            ;;
        --enableplugin | --disableplugin)
            _comp_cmd_yum__compgen_plugins
            ;;
        --color)
            _comp_compgen -- -W 'always auto never'
            ;;
        -R | -x | --exclude)
            # argument required but no completions available
            return
            ;;
        -h | --help | --version)
            # no other options useful with these
            return
            ;;
        *)
            _comp_compgen -- -W 'install update check-update upgrade remove
                erase list info provides whatprovides clean makecache
                groupinstall groupupdate grouplist groupremove groupinfo search
                shell resolvedep localinstall localupdate deplist repolist
                help'
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_yum yum

# ex: filetype=sh
