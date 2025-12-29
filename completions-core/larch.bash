# larch(1) completion                                      -*- shell-script -*-
# by Alex Shinn <foof@synthcode.com>

_comp_cmd_larch()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cword -eq 1 || $prev == -* ]]; then
        _comp_compgen -- -W ' \
            my-id my-default-archive register-archive whereis-archive archives \
            init-tree tree-root tree-version set-tree-version inventory \
            tagging-method tree-lint missing-tags add delete \
            move explicit-default set-manifest manifest check-manifest mkpatch \
            dopatch patch-report empty-patch make-archive make-category \
            make-branch make-version categories branches versions revisions \
            cat-archive-log archive-cache-revision archive-cached-revisions \
            archive-uncache-revision category-readme branch-readme \
            version-readme make-log logs add-log log-ls cat-log \
            log-header-field changelog log-for-merge merge-points \
            new-on-branch import commit get get-patch lock-branch \
            lock-revision push-mirror build-config update-config replay-config \
            record-config show-config config-history update replay delta-patch \
            star-merge tag prepare-branch finish-branch join-branch \
            whats-missing what-changed file-diffs pristines lock-pristine \
            my-revision-library library-find library-add library-remove \
            library-archives library-categories library-branches \
            library-versions library-revisions library-log library-file \
            touched-files-prereqs patch-set-web update-distributions \
            distribution-name notify my-notifier mail-new-categories \
            mail-new-branches mail-new-versions mail-new-revisions \
            notify-library notify-browser push-new-revisions sendmail-mailx'
    fi

} &&
    complete -F _comp_cmd_larch -o default larch

# ex: filetype=sh
