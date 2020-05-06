#!/bin/sh -e

# Post-commit hook for triggering bash-completion Docker Hub test image
# builds at https://hub.docker.com/r/vskytta/bash-completion/
#
# To enable: ln -s ../../extra/git-post-commit.sh .git/hooks/post-commit
#
# The bash-completion.docker-hub-trigger-url config option must be set to
# the full Docker Hub build trigger URL to hit.

url=$(git config bash-completion.docker-hub-trigger-url)

test "$(git symbolic-ref --short HEAD 2>/dev/null)" = master

git diff-tree -r --name-only --no-commit-id HEAD |
    grep -qxE 'test/test-cmd-list\.txt'

curl \
    --silent --show-error \
    --max-time 30 \
    --header Content-Type:application/json \
    --data '{"build":true}' \
    $url >/dev/null
