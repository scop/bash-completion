# Third-party startup directory - bash-completion

This directory `startup` is the place to put **third-party startup scripts**
for initializing [bash-completion](https://github.com/scop/bash-completion).

The `bash-completion` framework has been providing `/etc/bash_completion.d` as
a directory to put scripts that are eagerly loaded on the initialization stage
of `bash-completion`.  However, the historical purpose of
`/etc/bash_completion.d` has been the place to put completion files for
`bash-completion < 2.0`, which did not support the dynamic loading through
`complete -D` (`bash >= 4.1`).  This original usage was already deprecated.
Apart from that, there are scripts that need to be loaded on the initialization
stage of `bash-completion`, such as `/etc/bash_completion.d/fzf` and
`/etc/bash_completion.d/_python-argcomplete`, which want to set up a custom
default completion with `complete -D`.

In `bash-completion >= 2.18`, we started to provide the `startup` directory as
a dedicated directory for such scripts that need to be loaded on the
initialization stage.

* Eagerly loaded scripts should be placed in this directory instead of
  `/etc/bash_completion.d`.
* External completion files of API v1 should be updated to use API v2 or v3 and
  should be moved to `completions/<cmd>.bash`.  Although we recommend to update
  the completion file to use newer API, the completion file relying on API v1
  should continue to be placed in `/etc/bash_completion.d`.
