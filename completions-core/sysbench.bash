# bash completion for sysbench                             -*- shell-script -*-

_comp_cmd_sysbench()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        --num-threads | --max-requests | --max-time | --thread-stack-size | \
            --help | --version | help | version)
            return
            ;;
        --init-rng | --debug | --validate)
            _comp_compgen -- -W 'on off'
            return
            ;;
        --test)
            _comp_compgen -- -W 'fileio cpu memory threads mutex oltp'
            return
            ;;
        --cpu-max-prime)
            return
            ;;
        --file-test-mode)
            _comp_compgen -- -W 'seqwr seqrewr seqrd rndrd rndwr rndrw'
            return
            ;;
        --file-io-mode)
            _comp_compgen -- -W 'sync async fastmmap slowmmap'
            return
            ;;
        --file-extra-flags)
            _comp_compgen -- -W 'sync dsync direct'
            return
            ;;
        --file-fsync-all | --file-fsync-end)
            _comp_compgen -- -W 'on off'
            return
            ;;
        --file-fsync-mode)
            _comp_compgen -- -W 'fsync fdatasync'
            return
            ;;
        --memory-scope)
            _comp_compgen -- -W 'global local'
            return
            ;;
        --memory-hugetlb)
            _comp_compgen -- -W 'on off'
            return
            ;;
        --memory-oper)
            _comp_compgen -- -W 'read write none'
            return
            ;;
        --memory-access-mode)
            _comp_compgen -- -W 'seq rnd'
            return
            ;;
        --oltp-test-mode)
            _comp_compgen -- -W 'simple complex nontrx sp'
            return
            ;;
        --oltp-read-only | --oltp-skip-trx | --oltp-quto-inc | --mysql-ssl)
            _comp_compgen -- -W 'on off'
            return
            ;;
        --oltp-nontrx-mode)
            _comp_compgen -- -W 'select update_key update_nokey insert delete'
            return
            ;;
        --oltp-dist-type)
            _comp_compgen -- -W 'uniform gaussian special'
            return
            ;;
        --db-driver)
            _comp_compgen_split -- "$("$1" --test=oltp help 2>/dev/null |
                command sed -e '/^.*database drivers:/,/^$/!d' \
                    -ne 's/^  *\([^ ]*\) .*/\1/p')"
            return
            ;;
        --db-ps-mode)
            _comp_compgen -- -W 'auto disable'
            return
            ;;
        --mysql-socket)
            _comp_compgen_filedir sock
            return
            ;;
        --mysql-table-engine)
            _comp_compgen -- -W 'myisam innodb bdb heap ndbcluster federated'
            return
            ;;
        --mysql-engine-trx)
            _comp_compgen -- -W 'yes no auto'
            return
            ;;
        --*)
            [[ $was_split ]] && return
            ;;
    esac

    # find out which test we're running
    local i test="" has_test=""
    for ((i = 1; i < ${#words[@]} - 1; i++)); do
        # TODO --test= is deprecated, bare test name preferred
        if [[ ${words[i]} == --test=* ]]; then
            test=${words[i]#*=}
            has_test=set
            break
        fi
    done

    local opts
    _comp_compgen -v opts help
    if [[ $has_test ]]; then
        opts=("${opts[@]/#--test=/}")
        _comp_compgen -aRv opts help -- --test="$test" help
        opts+=(prepare run cleanup help version)
    fi

    if [[ $cur == -* || ! $has_test ]]; then
        _comp_compgen -- -W '"${opts[@]}"'
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        _comp_compgen -- -W "prepare run cleanup help version"
    fi
} &&
    complete -F _comp_cmd_sysbench sysbench

# ex: filetype=sh
