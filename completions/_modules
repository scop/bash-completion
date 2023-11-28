# module completion by Ted Stern <stern@cray.com>          -*- shell-script -*-
#
# Use of this file is deprecated, upstream completion is available in
# modules >= 3.2.7, use that instead.
#
# Completion for Environment Modules `module' alias.
#
# See https://sourceforge.net/projects/modules/
#     https://modules.sourceforge.net/
#
# There are several versions of modules that are commonly used.  Older
# Cray UNICOS systems and many other sites use 2.2.2b.  The latest GPL'd
# version is 3.1.6.  But the module alias is somewhat self-documenting
# via the `module help' command, so use that to print the options.
#
# Programmable completion might be more difficult under tcsh since the
# module command is an alias, and the `module avail' command returns
# its output as stderr.

# Test for existence of /etc/profile.d/modules.sh too because we may end up
# being sourced before it and thus before the `module' alias has been defined.
[[ -f /etc/profile.d/modules.sh ]] || return 1

_comp_cmd_module__compgen_list()
{
    local modules="$(command sed 's/:/ /g' <<<"$LOADEDMODULES" | sort)"
    _comp_compgen -- -W "$modules"
}

_comp_cmd_module__compgen_path()
{
    local modules="$(command sed 's/:/ /g' <<<"$MODULEPATH" | sort)"
    _comp_compgen -- -W "$modules"
}

_comp_cmd_module__compgen_avail()
{
    local modules="$(
        module avail 2>&1 |
            command grep -E -v '^(-|$)' |
            xargs printf '%s\n' | command sed -e 's/(default)//g' | sort
    )"
    _comp_compgen -- -W "$modules"
}

# A completion function for the module alias
_comp_cmd_module()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if ((cword == 1)); then
        # First parameter on line -- we expect it to be a mode selection

        local options
        options="$(module help 2>&1 | command grep -E '^[[:space:]]*\+' |
            _comp_awk '{print $2}' | command sed -e 's/|/ /g' | sort)"

        _comp_compgen -- -W "$options"

    elif ((cword == 2)); then
        case $prev in
            add | display | help | load | show | whatis)
                _comp_cmd_module__compgen_avail
                ;;
            rm | switch | swap | unload | update)
                _comp_cmd_module__compgen_list
                ;;
            unuse)
                _comp_cmd_module__compgen_path
                ;;
        esac
    elif ((cword == 3)); then
        case ${words[1]} in
            swap | switch)
                _comp_cmd_module__compgen_avail
                ;;
        esac
    fi

} &&
    complete -F _comp_cmd_module -o default module

# ex: filetype=sh
