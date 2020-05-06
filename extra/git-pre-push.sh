#!/bin/sh -e

# Pre-push hook for triggering bash-completion Docker Hub test image
# builds at https://hub.docker.com/r/vskytta/bash-completion/
#
# To enable: ln -s ../../extra/git-pre-push.sh .git/hooks/pre-push
#
# The bash-completion.docker-hub-trigger-url config option must be set to
# the full Docker Hub build trigger URL to hit.

url=$(git config bash-completion.docker-hub-trigger-url) || exit 0

branch=master
files="test/test-cmd-list\.txt"

trigger=false
z40=0000000000000000000000000000000000000000

while read local_ref local_sha remote_ref remote_sha; do
    case $remote_ref in */$branch) ;; *) continue ;; esac
    [ $local_sha != $z40 ] || continue # delete not handled (yet?)
    if [ $remote_sha = $z40 ]; then
        list_files="git ls-tree -r --name-only $local_sha"
    else
        list_files="git diff --name-only $remote_sha..$local_sha"
    fi
    ! $list_files | grep -qEx $files || {
        trigger=true
        break
    }
done

if $trigger; then
    cat <<EOF | at -M now
        sleep 15
        curl \
             --silent --show-error \
             --max-time 30 \
             --header Content-Type:application/json \
             --data '{"build":true}' \
             $url 2>&1 \
        | logger -e --tag bash-completion-pre-push
EOF
fi
