# btdownloadheadless(1) completion                         -*- shell-script -*-

_comp_cmd_btdownload()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --responsefile | --saveas)
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--max_uploads --keepalive_interval
            --download_slice_size --request_backlog --max_message_length
            --ip --minport --maxport --responsefile --url --saveas --timeout
            --timeout_check_interval --max_slice_length --max_rate_period
            --bind --upload_rate_fudge --display_interval --rerequest_interval
            --min_peers --http_timeout --max_initiate --max_allow_in
            --check_hashes --max_upload_rate --snub_time --spew
            --rarest_first_cutoff --min_uploads --report_hash_failures'
    else
        _comp_compgen_filedir
    fi
} &&
    complete -F _comp_cmd_btdownload btdownloadheadless.py btdownloadcurses.py \
        btdownloadgui.py

# ex: filetype=sh
