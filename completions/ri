# ri completion for Ruby documentation                     -*- shell-script -*-
# by Ian Macdonald <ian@caliban.org>

# @var[in] ri_version
# @var[in] prefix
# @var[in] classes
_comp_cmd_ri__compgen_methods()
{
    local _regex
    local IFS=$' \t\n' # needed for ${classes[@]+"${classes[@]}"} in bash-5.2

    local _methods
    if [[ $ri_version == integrated ]]; then
        if [[ ! $separator ]]; then
            _regex="(Instance|Class)"
        elif [[ $separator == "#" ]]; then
            _regex=Instance
        else
            _regex=Class
        fi

        _comp_split -la _methods \
            "$(ri ${classes[@]+"${classes[@]}"} 2>/dev/null | ruby -ane \
                'if /^'"$_regex"' methods:/.../^------------------|^$/ and \
            /^ / then print $_.split(/, |,$/).grep(/^[^\[]*$/).join("\n"); \
            end' 2>/dev/null | sort -u)"
    else
        # older versions of ri didn't distinguish between class/module and
        # instance methods
        _comp_split -la _methods \
            "$(ruby -W0 "$ri_path" ${classes[@]+"${classes[@]}"} 2>/dev/null | ruby -ane \
                'if /^-/.../^-/ and ! /^-/ and ! /^ +(class|module): / then \
            print $_.split(/, |,$| +/).grep(/^[^\[]*$/).join("\n"); \
            end' | sort -u)"
    fi &&
        _comp_compgen -- -P "$prefix" -W '"${_methods[@]}"'
}

# needs at least Ruby 1.8.0 in order to use -W0
_comp_cmd_ri()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -n : -- "$@" || return

    local noargopts='!(-*|*[wfd]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --width | -${noargopts}[hw])
            return
            ;;
        --format | -${noargopts}f)
            _comp_compgen -- -W 'ansi bs html rdoc'
            return
            ;;
        --doc-dir | -${noargopts}d)
            _comp_compgen_filedir -d
            return
            ;;
        --dump)
            _comp_compgen_filedir ri
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    local class method prefix="" ri_path ri_version ri_major="" separator
    local -a classes

    ri_path=$(type -p ri)
    # which version of ri are we using?
    # -W0 is required here to stop warnings from older versions of ri
    # from being captured when used with Ruby 1.8.1 and later
    ri_version="$(ruby -W0 "$ri_path" -v 2>&1)" || ri_version=integrated
    [[ $ri_version != "${ri_version%200*}" ]] && ri_version=integrated
    [[ $ri_version =~ ri[[:space:]]v?([0-9]+) ]] && ri_major=${BASH_REMATCH[1]}

    # need to also split on commas
    if [[ $cur == [A-Z]*[#.]* ]]; then
        [[ $cur == *#* ]] && separator=# || separator=.
        # we're completing on class and method
        class=${cur%"$separator"*}
        method=${cur#*"$separator"}
        _comp_split -F $', \n\t' classes "$class"
        prefix=$class$separator
        _comp_compgen -c "$method" -i ri methods
        return
    fi

    if [[ $ri_version == integrated ]]; then
        # integrated ri from Ruby 1.9
        _comp_split -F $', \n\t' classes \
            "$(ri -c 2>/dev/null | ruby -ne 'if /^\s*$/..$stdin.eof then \
            if /^ +[A-Z]/ then print; end; end' 2>/dev/null)"
    elif [[ $ri_major && $ri_major -ge 3 ]]; then
        _comp_split -F $', \n\t' classes "$(ri -l 2>/dev/null)"
    elif [[ $ri_version == "ri 1.8a" ]]; then
        _comp_split -F $', \n\t' classes "$(ruby -W0 "$ri_path" |
            ruby -ne 'if /^'"'"'ri'"'"' has/..$stdin.eof then \
            if /^ .*[A-Z]/ then print; end; end')"
    else
        _comp_split -F $', \n\t' classes "$(ruby -W0 "$ri_path" |
            ruby -ne 'if /^I have/..$stdin.eof then \
                if /^ .*[A-Z]/ then print; end; end')"
    fi &&
        _comp_compgen -- -W '"${classes[@]}"'
    _comp_ltrim_colon_completions "$cur"

    if [[ $cur == [A-Z]* ]]; then
        # we're completing on class or module alone
        return
    fi

    # we're completing on methods
    _comp_cmd_ri__compgen_methods
} &&
    complete -F _comp_cmd_ri ri

# ex: filetype=sh
