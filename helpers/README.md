# Third-party helpers directory - bash-completion

This directory `helpers` is the place to put **third-party helper scripts**
that are used by third-party completion files in the `completions` directory,
written for [bash-completion](https://github.com/scop/bash-completion).

> [!NOTE]
>
> The core `bash-completion` framework (<= 2.17) has provided also *helper
> scripts included in the bash-completion framework itself* in this directory,
> but we separated those files into `helpers-core`.  However, external
> completion provider should continue to install their helper scripts in
> `helpers`.  The new directory `helpers-core` is an internal directory
> intended to be used by the core `bash-completion`.

The helper script may be referenced by a completion script in `completions`
with `${BASH_COMPLETION[0]%/*}/../helpers/<helper>`.
