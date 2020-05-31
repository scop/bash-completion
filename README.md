# bash-completion

[![Build Status](https://travis-ci.org/scop/bash-completion.svg?branch=master)](https://travis-ci.org/scop/bash-completion)

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
other file sourcing those). You can do this by simply using:

```shell
# Use bash-completion, if available
[[ $PS1 && -f /usr/share/bash-completion/bash_completion ]] && \
    . /usr/share/bash-completion/bash_completion
```

(if you happen to have *only* bash >= 4.2 installed, see further if not)

If you don't have the package readily available for your distribution, or
you simply don't want to use one, you can install bash completion using the
standard commands for GNU autotools packages:

```shell
autoreconf -i  # if not installing from prepared release tarball
./configure
make           # GNU make required
make check     # optional, requires python3 with pytest >= 3.6, pexpect
make install   # as root
```

These commands install the completions and helpers, as well as a
`profile.d` script that loads `bash_completion` where appropriate.

If your system does not use the `profile.d` directory (usually below
`/etc`) mechanism—i.e. does not automatically source shell scripts in
it—you can source the `$sysconfdir/profile.d/bash_completion.sh`
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
try running `set -v` or `set -x` prior to attempting the completion
again. This will produce useful debugging output that will aid us in
fixing the problem if you are unable to do so yourself. Turn off the
trace output by running either `set +v` or `set +x`.

To debug dynamic loading of a completion, tracing needs to be turned
on before the debugged completion is attempted the first time. The
easiest way to do this is to start a new shell session, and to turn
tracing on in it before doing anything else there.

## Known problems

1. There seems to be some issue with using the bash built-in `cd` within
   Makefiles. When invoked as `/bin/sh` within `Makefile`s, bash seems
   to have a problem changing directory via the `cd` command. A
   work-around for this is to define `SHELL=/bin/bash` within your
   `Makefile`. This is believed to be a bug in bash.

2. Many of the completion functions assume GNU versions of the various
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
   next answer for details where to install it, if you are doing it on per
   user basis. If you want to do it system wide, you can install eagerly
   loaded files in `compatdir` (see a couple of questions further down for
   more info) and install a completion for the commands to override our
   completion for in them.

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

A. Install it in one of the directories pointed to by
   bash-completion's `pkgconfig` file variables. There are two
   alternatives:

   - The recommended directory is `completionsdir`, which you can get with
     `pkg-config --variable=completionsdir bash-completion`. From this
     directory, completions are automatically loaded on demand based on invoked
     commands' names, so be sure to name your completion file accordingly, and
     to include (for example) symbolic links in case the file provides
     completions for more than one command.
   - The other directory (which only present for backwards compatibility)
     is `compatdir` (get it with
     `pkg-config --variable=compatdir bash-completion`) from which files
     are loaded when `bash_completion` is loaded.

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
   dist_bashcomp_DATA = # completion files go here
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

**Q. I use CVS in combination with passwordless SSH access to my remote
   repository. How can I have the `cvs` command complete on remotely
   checked-out files where relevant?**

A. Define `$COMP_CVS_REMOTE`. Setting this to anything will result in
   the behaviour you would like.

**Q. When I'm running a `./configure` script and completion returns a list
   of long options to me, some of these take a parameter,
   e.g. `--this-option=DESCRIPTION`.**

   **Running `./configure --help` lists these descriptions, but
   everything after the `=` is stripped when returning completions, so
   I don't know what kind of data is expected as a given option's
   parameter.**

   **Is there a way of getting `./configure` completion to return the
   entire option string, so that I can see what kind of data is
   required and then simply delete the descriptive text and add my own
   data?**

A. Define `$COMP_CONFIGURE_HINTS`. Setting this to anything will
   result in the behaviour you would like.

**Q. When doing tar completion on a file within a tar file like this:**

   ```shell
   tar tzvf foo.tar.gz <Tab>
   ```

   **the pathnames contained in the tar file are not displayed
   correctly. The slashes are removed, and everything looks like it's
   in a single directory. Why is this?**

A. It's a choice we had to make. bash's programmable completion is
   limited in how it handles the list of possible completions it
   returns.

   Because the paths returned from within the tar file are likely not
   existing paths on the file system, `-o dirnames` must be passed to
   the `complete` built-in to make it treat them as such. However,
   then bash will append a space when completing on directories during
   pathname completion to the tar files themselves.

   It's more important to have proper completion of paths to tar files
   than it is to have completion for their contents, so this sacrifice
   was made and `-o filenames` is used with complete instead.

   If you would rather have correct path completion for tar file
   contents, define `$COMP_TAR_INTERNAL_PATHS` *before* sourcing
   `bash_completion`.

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
   `/var/log/rpmpkgs`.  It's generated by `/etc/cron.daily/rpm` on
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

**Q. bash-completion interferes with my `command_not_found_handler` function!**

A. If your `command_not_found_handler` function is not intended to
   address (possibly missing) commands invoked during bash
   programmable completion functions, you can account for this
   by, for example, testing if the `$COMP_`\* variables are set and
   taking appropriate bypass or other action.

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
