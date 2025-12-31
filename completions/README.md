# External completions directory - bash-completion

This directory `completions` is the place to put *external* completion files,
i.e., ones not shipped with the bash-completion project.  They are loaded by
[bash-completion](https://github.com/scop/bash-completion) on demand.

> [!NOTE]
>
> The core `bash-completion` framework (<= 2.17) has provided also *completion
> files bundled with the bash-completion framework itself* in this directory,
> but we separated those files into `completions-core` and
> `completions-fallback`.  However, external completion providers should
> continue to install their completion files in `completions`.  The new
> directories `completions-core` and `completions-fallback` are internal
> directories intended to be used by the core bash-completion only.

The programmable completion for the command `<cmd>` is supposed to be provided
in the file `completions/<cmd>.bash`.  The implementation examples are found in
`completions-core`, which uses the latest bash-completion API (v3).  If you
want to make the completion file to work also with an older version of
`bash-completion`, you need to use the previous API of v2, which is contiuned
to be supported for now.  For examples with API v2, please reference the
completion files in `completions` of
[bash-completion-2.11](https://github.com/scop/bash-completion/releases/tag/2.11).
