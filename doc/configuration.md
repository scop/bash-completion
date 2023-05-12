# Configuration

## Files

### `$BASH_COMPLETION_USER_FILE`

Sourced late by `bash_completion`, pretty much after everything else.
Use this file for example to load additional completions, and to remove
and override ones installed by bash_completion. Defaults to
`~/.bash_completion` if unset or null.

Available since version 2.7.

### `$XDG_CONFIG_HOME/bash_completion`

Sourced by the `bash_completion.sh` `profile.d` script. This file is
suitable for definitions of all `COMP*` shell variables below.
If `$XDG_CONFIG_HOME` is unset or null,`~/.config` is
used instead of it.

Available since version 1.90.

## Shell variables

### `BASH_COMPLETION_COMPAT_DIR`

Directory for pre-dynamic loading era (pre-2.0) and other backwards
compatibility completion files that are loaded eagerly from `bash_completion`
when it is loaded. If unset or null, the default compatibility directories to
use are `/etc/bash_completion.d`, and `bash_completion.d` relative to
`bash_completion` location.

Available since version 1.1.

### `BASH_COMPLETION_FILEDIR_FALLBACK`

If set and not null, completions that look for filenames based on their
"extensions" will fall back to suggesting all files if there are none
matching the sought ones.

Available since version 2.12.
Deprecated alias: `COMP_FILEDIR_FALLBACK`

### `BASH_COMPLETION_KNOWN_HOSTS_WITH_AVAHI`

If set and not null, known hosts completion will try to use `avahi-browse`
for additional completions. This may be a slow operation in some setups.
Default is unset.

Available since version 2.12.
Deprecated alias: `COMP_KNOWN_HOSTS_WITH_AVAHI`

### `BASH_COMPLETION_KNOWN_HOSTS_WITH_HOSTFILE`

If set and not null (default), known hosts completion will complement
hostnames from ssh's known_hosts files with hostnames taken from the file
specified by the `HOSTFILE` shell variable (`compgen -A hostname`). If null,
known hosts completion will omit hostnames from `HOSTFILE`. Omitting
hostnames from `HOSTFILE` is useful if `HOSTFILE` contains many entries for
local web development or ad-blocking.

Available since version 2.12.
Deprecated alias: `COMP_KNOWN_HOSTS_WITH_HOSTFILE`

### `BASH_COMPLETION_COMPAT_IGNORE`

Files in `BASH_COMPLETION_COMPAT_DIR` (the compat dir) to ignore, specified by
a glob pattern.  The completion files in the compat dir whose basename matches
with this pattern will not be sourced by `bash_completion` at its load time.
This variable can be used to suppress the problematic completions.  Note that
backup files and Makefiles in the compat dir are by default ignored regardless
of this setting.

One example is `acroread.sh` which is installed by some versions of Adobe
Reader, overrides `_filedir` with an incompatible version, and causes
various problems.  To recover this `_filedir`, another completion file
`redefine_filedir` had been placed in the compat dir, which could also
cause another incompatibility when the user uses their own version of
bash-completion instead of the systemwide version.  To suppress these files
one can set the following value:

```bash
export BASH_COMPLETION_COMPAT_IGNORE='@(acroread.sh|redefine_filedir)'
```

- <https://bugzilla.redhat.com/677446>
- <http://forums.adobe.com/thread/745833>
- <https://bugzilla.redhat.com/show_bug.cgi?id=1171396#c27>
- <https://github.com/scop/bash-completion/pull/667>

Available since version 2.12.

### `BASH_COMPLETION_CMD_CONFIGURE_HINTS`

If set and not null, `configure` completion will return the entire option
string (e.g. `--this-option=DESCRIPTION`) so one can see what kind of data
is required and then simply delete the descriptive text and add one's own
data. If unset or null (default), `configure` completion will strip
everything after the `=` when returning completions.

Available since version 2.12.
Deprecated alias: `COMP_CONFIGURE_HINTS`

### `BASH_COMPLETION_CMD_CVS_REMOTE`

If set and not null, `cvs commit` completion will try to complete on
remotely checked-out files. This requires passwordless access to the
remote repository. Default is unset.

Available since version 2.12.
Deprecated alias: `COMP_CVS_REMOTE`

### `BASH_COMPLETION_CMD_IWCONFIG_SCAN`

If set and not null, `iwconfig` completion will try to complete on
available wireless networks identifiers. Default is unset.

Available since version 2.12.
Deprecated alias: `COMP_IWLIST_SCAN`

### `BASH_COMPLETION_CMD_SMBTREE_SCAN`

If set and not null, various samba related tool completions perform
a network scan to complete domains and hosts. Default is unset.

Available since version 2.12.
Deprecated alias: `COMP_SAMBA_SCAN`

### `BASH_COMPLETION_CMD_TAR_INTERNAL_PATHS`

If set and not null _before sourcing_ the `tar` completion, it will do
correct path completion for tar file _contents_. If unset or null,
_paths to_ tar files will be correctly completed. Unfortunately we do not
have a way to make both Just Work properly at the moment. We consider it
more important to have proper completion of paths to tar files than it is
to have completion for their contents, so the default is unset.

Available since version 2.12.
Deprecated alias: `COMP_TAR_INTERNAL_PATHS`

## Shell options

### `no_empty_cmd_completion`

If on, completions producing command names do not do anything if the command to
be completed is empty. This can be useful on systems where generating the
entire list of commands takes a long time.

Available since version 2.12.
