# bash-completion

[![CI](https://github.com/scop/bash-completion/actions/workflows/ci.yaml/badge.svg)](https://github.com/scop/bash-completion/actions/workflows/ci.yaml)

## Introduction

bash-completion is a collection of command line command completions for the
[Bash shell](https://www.gnu.org/software/bash/), collection of helper
functions to assist in creating new completions, and set of facilities for
loading completions automatically on demand, as well as installing them.

## Installation

The easiest way to install this software is to use a package; refer to
[Repology](https://repology.org/project/bash-completion) for a comprehensive
list of operating system distributions, package names, and available versions.

Depending on the package, you may still
need to source it from either `/etc/bashrc` or `~/.bashrc` (or any
other file sourcing those). If you have _only_ bash >= 4.2 installed, you can
do this by simply using:

```shell
# Use bash-completion, if available
[[ $PS1 && -f /usr/share/bash-completion/bash_completion ]] && \
    . /usr/share/bash-completion/bash_completion
```

If you have older bash versions in use, their loading of `bash_completion`
should be prevented. See further for more info.

If you don't have the package readily available for your distribution, or
you simply don't want to use one, you can install bash completion using the
standard commands for GNU autotools packages:

```shell
autoreconf -i      # if not installing from prepared release tarball
./configure
make               # GNU make required
make check         # optional
make install       # as root
make installcheck  # optional, requires python3 with pytest >= 3.6, pexpect
```

These commands install the completions and helpers, as well as a
`profile.d` script that loads `bash_completion` where appropriate.

If your system does not use the `profile.d` directory (usually below
`/etc`) mechanism (i.e., does not automatically source shell scripts in
it), you can source the `$sysconfdir/profile.d/bash_completion.sh`
script in `/etc/bashrc` or `~/.bashrc`.

The `profile.d` script provides a configuration file hook that can be
used to prevent loading `bash_completion` on per user basis when it's
installed system wide. To do this:

1. Turn off programmable completion with `shopt -u progcomp` in
   `$XDG_CONFIG_HOME/bash_completion` (or `~/.config/bash_completion`
   if `$XDG_CONFIG_HOME` is not set)
2. Turn it back on (for example in `~/.bashrc`) if you want to use
   programmable completion for other purposes.

### macOS (OS X)

If you're using macOS (formerly OS X), `/etc/bashrc` is apparently not sourced at
all. In that case, you can put the `bash_completion` file in `/sw/etc`
and add the following code to `~/.bash_profile`:

```shell
if [ -f /sw/etc/bash_completion ]; then
   . /sw/etc/bash_completion
fi
```

## Troubleshooting

If you find that a given function is producing errors or does not work
as it should under certain circumstances when you attempt completion,
try running `set -x` or `set -v` prior to attempting the completion
again. This will produce useful debugging output that will aid us in
fixing the problem if you are unable to do so yourself. Turn off the
trace output by running either `set +x` or `set +v`.

If you are filing an issue, please attach the generated debugging output
in `set -x` mode copy-pasted to a separate, attached file in the report.
Before doing so, be sure to review the output for anything you may not want
to share in public, and redact as appropriate.

To debug dynamic loading of a completion, tracing needs to be turned
on before the debugged completion is attempted the first time. The
easiest way to do this is to start a new shell session, and to turn
tracing on in it before doing anything else there.

## Known problems

1. Many of the completion functions assume GNU versions of the various
   text utilities that they call (e.g. `grep`, `sed`, and `awk`). Your
   mileage may vary.

## FAQ

**Q. The bash completion code inhibits some commands from completing on
   files with extensions that are legitimate in my environment. Do I
   have to disable completion for that command in order to complete on
   the files that I need to?**

A. No. Use `M-/` to (in the words of the bash man page) attempt file
   name completion on the text to the left of the cursor. This will
   circumvent any file type restrictions put in place by the bash
   completion code.

**Q. How can I override a completion shipped by bash-completion?**

A. Install a local completion of your own appropriately for the desired
   command, and it will take precedence over the one shipped by us. See the
   next answer for details where to install it, if you are doing it on per user
   basis. If you want to do it system wide, you can install eagerly loaded
   files in `compatdir` (see a couple of questions further down for more
   info. To get the path of `compatdir` for the current system, the output of
   `pkg-config bash-completion --variable compatdir` can be used) and install a
   completion for the commands to override our completion for in them.

   If you want to use bash's default completion instead of one of ours,
   something like this should work (where `$cmd` is the command to override
   completion for): `complete -o default -o bashdefault $cmd`

**Q. Where should I install my own local completions?**

A. Put them in the `completions` subdir of `$BASH_COMPLETION_USER_DIR`
   (defaults to `$XDG_DATA_HOME/bash-completion` or
    `~/.local/share/bash-completion`
   if `$XDG_DATA_HOME` is not set) to have them loaded automatically
   on demand when the respective command is being completed.
   See also the next question's answer for considerations for these
   files' names, they apply here as well. Alternatively, you can write
   them directly in `~/.bash_completion` which is loaded eagerly by
   our main script.

**Q. I author/maintain package X and would like to maintain my own
   completion code for this package. Where should I put it to be sure
   that interactive bash shells will find it and source it?**

A. [ Disclaimer: Here, how to make the completion code visible to
   bash-completion is explained.  We do not require always making the
   completion code visible to bash-completion.  In what condition the
   completion code is installed should be determined at the author/maintainers'
   own discretion. ]

   Install it in one of the directories pointed to by bash-completion's
   `pkgconfig` file variables. There are two alternatives:

   - The recommended directory is `completionsdir`, which you can get with
     `pkg-config --variable=completionsdir bash-completion`. From this
     directory, completions are automatically loaded on demand based on invoked
     commands' names, so be sure to name your completion file accordingly, and
     to include (for example) symbolic links in case the file provides
     completions for more than one command. The completion filename for
     command `foo` in this directory should be either `foo`, or `foo.bash`.
     (Underscore prefixed `_foo` works too, but is reserved for
     bash-completion internal use as a deprecation/fallback marker.)
   - The other directory which is only present for backwards compatibility,
     its usage is no longer recommended, is `compatdir` (get it with
     `pkg-config --variable=compatdir bash-completion`). From this
     directory, files are loaded eagerly when `bash_completion` is loaded.

   For packages using GNU autotools the installation can be handled
   for example like this in `configure.ac`:

   ```m4
   PKG_CHECK_VAR(bashcompdir, [bash-completion], [completionsdir], ,
     bashcompdir="${sysconfdir}/bash_completion.d")
   AC_SUBST(bashcompdir)
   ```

   ...accompanied by this in `Makefile.am`:

   ```makefile
   bashcompdir = @bashcompdir@
   dist_bashcomp_DATA = your-completion-file # completion files go here
   ```

   For cmake we ship the `bash-completion-config.cmake` and
   `bash-completion-config-version.cmake` files. Example usage:

   ```cmake
   find_package(bash-completion)
   if(BASH_COMPLETION_FOUND)
     message(STATUS
       "Using bash completion dir ${BASH_COMPLETION_COMPLETIONSDIR}")
   else()
     set (BASH_COMPLETION_COMPLETIONSDIR "/etc/bash_completion.d")
     message (STATUS
       "Using fallback bash completion dir ${BASH_COMPLETION_COMPLETIONSDIR}")
   endif()

   install(FILES your-completion-file DESTINATION
     ${BASH_COMPLETION_COMPLETIONSDIR})
   ```

   In bash-completion >= 2.12, we search the data directory of
   `bash-completion` under the installation prefix where the target command is
   installed.  When one can assume that the version of the target
   bash-completion is 2.12 or higher, the completion script can actually be
   installed to `$PREFIX/share/bash-completion/completions/` under the same
   installation prefix as the target program installed under `$PREFIX/bin/` or
   `$PREFIX/sbin/`.  For the detailed search order, see also "Q. What is the
   search order for the completion file of each target command?" below.

   Example for `Makefile.am`:

   ```makefile
   bashcompdir = $(datarootdir)/bash-completion/completions
   dist_bashcomp_DATA = your-completion-file
   ```

   Example for `CMakeLists.txt`:

   ```cmake
   install(FILES your-completion-file DESTINATION "${CMAKE_INSTALL_DATAROOTDIR}/bash-completion/completions")
   ```

**Q. When completing on a symlink to a directory, bash does not append
   the trailing `/` and I have to hit <kbd>&lt;Tab></kbd> again.
   I don't like this.**

A. This has nothing to do with `bash_completion`. It's the default for
   completing symlinks to directories since bash 2.05a, and was added
   because sometimes you want to operate on the symlink itself, rather
   than what it points to.

   You can get the pre-2.05a behaviour back by putting `set
   mark-symlinked-directories on` in your `/etc/inputrc` or
   `~/.inputrc` file.

**Q. Completion goes awry when I try to complete on something that contains
   a colon.**

A. This is actually a 'feature' of bash. bash recognises a colon as
   starting a new completion token, which is often what you want when
   completing something like a `PATH` variable:

   ```shell
   export PATH=/bin:/sbin:/usr<Tab>
   ```

   Without the special treatment of the colon, the above wouldn't work
   without programmable completion, so it has long been a feature of
   the shell.

   Unfortunately, you don't want the colon to be treated as a special
   case when doing something like:

   ```shell
   man File::B<Tab>
   ```

   Here, the colons make bash think that it's completing a new token
   that begins with 'B'.

   Unfortunately, there's no way to turn this off. The only thing you
   can do is escape the colons with a backslash.

**Q. Why is `rpm` completion so slow with `-q`?**

A. Probably because the database is being queried every time and this uses a
   lot of memory.

   You can make this faster by pregenerating the list of installed
   packages on the system. Make sure you have a readable file called
   `/var/log/rpmpkgs`. It's generated by `/etc/cron.daily/rpm` on
   some Red Hat and Mandrake and derivative Linux systems.

   If you don't have such a cron job, make one:

   ```shell
   #!/bin/sh

   rpm -qa --qf '%{name}-%{version}-%{release}.%{arch}.rpm\n' 2>&1 \
           | sort >/var/log/rpmpkgs
   ```

   rpm completion will use this flat text file instead of the RPM database,
   unless it detects that the database has changed since the file was created,
   in which case it will still use the database to ensure accuracy.

**Q. bash-completion interferes with my `command_not_found_handle` function
   (or the other way around)!**

A. If your `command_not_found_handle` function is not intended to
   address (possibly missing) commands invoked during bash
   programmable completion functions, you can account for this
   in the function by, for example, testing if the `$COMP_LINE`
   variable is set and taking appropriate action, typically returning
   early and silently with success.

**Q. Can tab completion be made even easier?**

A. The `readline(3)` library offers a few settings that can make tab
   completion easier (or at least different) to use.

   For example, try putting the following in either `/etc/inputrc` or
   `~/.inputrc`:

   ```inputrc
   set show-all-if-ambiguous on
   ```

   This will allow single tab completion as opposed to requiring a
   double tab. This makes things much more pleasant, in our opinion.

   ```inputrc
   set visible-stats on
   ```

   This will suffix each returned file completion with a character
   denoting its type, in a similar way to `ls(1)` with `-F` or `--classify`.

   ```inputrc
   set page-completions off
   ```

   This turns off the use of the internal pager when returning long
   completion lists.

**Q. Is bash the be-all-and-end-all of completion as far as shells go?**

A. Absolutely not. zsh has an extremely sophisticated completion system
   that offers many features absent from the bash implementation. Its
   users often cannot resist pointing this out. More information can
   be found at <https://www.zsh.org/>.

**Q. What is the search order for the completion file of each target command?**

A. The completion files of commands are looked up by the shell function
  `__load_completion`.  Here, the search order in bash-completion >= 2.12 is
  explained.

  1. `BASH_COMPLETION_USER_DIR`. The subdirectory `completions` of each paths
     in `BASH_COMPLETION_USER_DIR` separated by colons is considered for a
     completion directory.
  2. The location of the main `bash_completion` file. The subdirectory
     `completions` in the same directory as `bash_completion` is considered.
  3. The location of the target command.  When the real location of the command
     is in the directory `<prefix>/bin` or `<prefix>/sbin`, the directory
     `<prefix>/share/bash-completion/completions` is considered.
  4. `XDG_DATA_DIRS` (or the system directories `/usr/local/share:/usr/share`
     if empty).  The subdirectory `bash-completion/completions` of each paths
     in `XDG_DATA_DIRS` separated by colons is considered.

  The completion files of the name `<cmd>` or `<cmd>.bash`, where `<cmd>` is
  the name of the target command, are searched in the above completion
  directories in order.  The file that is found first is used.  When no
  completion file is found in any completion directories in this process, the
  completion files of the name `_<cmd>` is next searched in the completion
  directories in order.
