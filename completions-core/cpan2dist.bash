# bash completion for cpan2dist                            -*- shell-script -*-

_comp_cmd_cpan2dist()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --format)
            # should remove ":" from COMP_WORDBREAKS, but doesn't work (?)
            _comp_compgen_split -- "$(perl -MCPANPLUS::Dist -e \
                'print map { "$_n" } CPANPLUS::Dist->dist_types')"
            return
            ;;
        --banlist | --ignorelist | --modulelist | --logfile)
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
    else
        local cpandirs=("$HOME/.cpanplus/" "$HOME/.cpan/source/modules/")
        local dir packagelist=
        for dir in "${cpandirs[@]}"; do
            [[ -d $dir && -r "$dir/02packages.details.txt.gz" ]] &&
                packagelist="$dir/02packages.details.txt.gz"
        done
        [[ $packagelist ]] && _comp_split COMPREPLY "$(zgrep "^${cur//-/::}" \
            "$packagelist" 2>/dev/null | _comp_awk '{print $1}' |
            command sed -e 's/::/-/g')"
    fi
} &&
    complete -F _comp_cmd_cpan2dist -o default cpan2dist

# ex: filetype=sh
