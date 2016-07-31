# Completion functions called by other functions

## _userland()
Check if we're running on the given userland

### Parameters
| param | description |
| --- | --- |
| $1 | userland to check for |


## _sysvdirs()
This function sets correct SysV init directories


## _have()
This function checks whether we have a given program on the system.


## have()
**@deprecated** should no longer be used; generally not needed with dynamically loaded completions, and `_have` is suitable for runtime use.  
Backwards compatibility for compat completions that use `have()`.


## _rl_enabled()
This function checks whether a given readline variable is 'on'.


## quote()
This function shell-quotes the argument


## quote_readline()
See `_quote_readline_by_ref()`


## dequote()
This function shell-dequotes the argument


## _upvar()
Assign variable one scope above the caller

### Usage
```
local "$1" && _upvar $1 "value(s)"
```

### Parameters
| param | description |
| --- | --- |
| $1 | Variable name to assign value to |
| $* | Value(s) to assign.  If multiple values, an array is assigned, otherwise a single value is assigned. |

### Note
For assigning multiple variables, use `_upvars`.  
Do **NOT** use multiple `_upvar` calls, since one `_upvar` call might reassign a variable to be used by another `_upvar` call.

### See
[http://fvue.nl/wiki/Bash:_Passing_variables_by_reference](http://fvue.nl/wiki/Bash:_Passing_variables_by_reference)


## _upvars()
Assign variables one scope above the caller

### Usage
```
local varname [varname ...] && _upvars [-v varname value] | [-aN varname [value ...]] ...
```

### Available OPTIONS
| param | description |
| --- | --- |
| -aN | Assign next N values to varname as array |
| -v | Assign single value to varname |

### Return
`1` if error occurs

### See
[http://fvue.nl/wiki/Bash:_Passing_variables_by_reference](http://fvue.nl/wiki/Bash:_Passing_variables_by_reference)


## __reassemble_comp_words_by_ref()
Reassemble command line words, excluding specified characters from the list of word completion separators (`COMP_WORDBREAKS`).

### Parameters
| param | description |
| --- | --- |
| $1 | chars - Characters out of `$COMP_WORDBREAKS` which should **NOT** be considered word breaks. <br/>This is useful for things like `scp` where we want to return `host:path` and not only `path`, so we would pass the colon (`:`) as `$1` here.
| $2 | words - Name of variable to return words to |
| $3 | cword - Name of variable to return cword to |


## __get_cword_at_cursor_by_ref()

### Parameters
| param | description |
| --- | --- |
| $1 | exclude  Characters out of `$COMP_WORDBREAKS` which should **NOT** be considered word breaks. <br/>This is useful for things like `scp` where we want to return `host:path` and not only `path|, so we would pass the colon (`:`) as `$1` in this case.
| $2 | words - Name of variable to return words to |
| $3 | cword - Name of variable to return cword to |
| $4 | cur - Name of variable to return current word to complete to |

### See
`__reassemble_comp_words_by_ref()`


## _get_comp_words_by_ref()
Get the word to complete and optional previous words.  
This is nicer than `${COMP_WORDS[$COMP_CWORD]}`, since it handles cases where the user is completing in the middle of a word.  
For example, if the line is following with cursor as shown:
```
ls foobar
     ^
```
Also one is able to cross over possible wordbreak characters.

### Usage
```
_get_comp_words_by_ref [OPTIONS] [VARNAMES]
```

### Available VARNAMES
| VARNAME | description |
| --- | --- |
| cur | Return cur via `$cur` |
| prev | Return prev via `$prev` |
| words | Return words via `$words` |
| cword | Return cword via `$cword` |

### Available OPTIONS
| OPTION | description |
| --- | --- |
| -n EXCLUDE | Characters out of `$COMP_WORDBREAKS` which should **NOT** be considered word breaks. <br/>This is useful for things like `scp` where we want to return `host:path` and not only `path`, so we would pass the colon (`:`) as `-n` option in this case.
| -c VARNAME | Return cur via $VARNAME |
| -p VARNAME | Return prev via $VARNAME |
| -w VARNAME | Return words via $VARNAME |
| -i VARNAME | Return cword via $VARNAME |

### Example usage
```
_get_comp_words_by_ref -n : cur prev
```


## _get_cword()
**@deprecated** Use `_get_comp_words_by_ref cur` instead.  
Get the word to complete.  
This is nicer than `${COMP_WORDS[$COMP_CWORD]}`, since it handles cases where the user is completing in the middle of a word.  
For example, if the line is following with cursor as shown:
```
ls foobar
     ^
```

### Parameters
| param | description |
| --- | --- |
| $1 string | Characters out of `$COMP_WORDBREAKS` which should **NOT** be considered word breaks. <br/>This is useful for things like `scp` where we want to return `host:path` and not only `path`, so we would pass the colon (`:`) as `$1` in this case.
| $2 integer | Index number of word to return, negatively offset to the current word (default is 0, previous is 1), respecting the exclusions given at `$1`. <br>For example, `_get_cword "=:" 1` returns the word left of the current word, respecting the exclusions `=:`.


### See
`_get_comp_words_by_ref()`


## _get_pword()
**@deprecated** Use `_get_comp_words_by_ref cur prev` instead.  
Get word previous to the current word.  
This is a good alternative to `prev=${COMP_WORDS[COMP_CWORD-1]}` because `bash4` will properly return the previous word with respect to any given exclusions to `COMP_WORDBREAKS`.  

### See
`_get_comp_words_by_ref()`


## __ltrim_colon_completions()
**@modifies** global array `$COMPREPLY`  
If the word-to-complete contains a colon (`:`), left-trim `COMPREPLY` items with word-to-complete.  
With a colon in `COMP_WORDBREAKS`, words containing colons are always completed as entire words if the word to complete contains a colon. This function fixes this, by removing the colon-containing-prefix from `COMPREPLY` items.  
The preferred solution is to remove the colon (`:`) from `COMP_WORDBREAKS` in your `.bashrc`:
```
# Remove colon (:) from list of word completion separators
COMP_WORDBREAKS=${COMP_WORDBREAKS//:}
```

### See also
Bash FAQ - E13) Why does filename completion misbehave if a colon appears in the filename?  
[http://tiswww.case.edu/php/chet/bash/FAQ](http://tiswww.case.edu/php/chet/bash/FAQ)

### Parameters
| param | description |
| --- | --- |
| $1 | current word to complete (cur) |


## _quote_readline_by_ref()
This function quotes the argument in a way so that readline dequoting results in the original argument.  
This is necessary for at least `compgen` which requires its arguments quoted/escaped:
```
$ ls "a'b/"
c
$ compgen -f "a'b/"       # Wrong, doesn't return output
$ compgen -f "a\'b/"      # Good
a\'b/c
```

### See also
[http://lists.gnu.org/archive/html/bug-bash/2009-03/msg00155.html](http://lists.gnu.org/archive/html/bug-bash/2009-03/msg00155.html)  
[http://www.mail-archive.com/bash-completion-devel@lists.alioth.debian.org/msg01944.html](http://www.mail-archive.com/bash-completion-devel@lists.alioth.debian.org/msg01944.html)

### Parameters
| param | description |
| --- | --- |
| $1 | Argument to quote
| $2 | Name of variable to return result to


## _filedir()
This function performs file and directory completion. It's better than simply using `compgen -f`, because it honours spaces in filenames.

### Parameters
| param | description |
| --- | --- |
| $1 | If `-d`, complete only on directories. Otherwise filter/pick only completions with `.$1` and the uppercase version of it as file extension. |


## _split_longopt()
This function splits `$cur=--foo=bar` into `$prev=--foo` and `$cur=bar`, making it easier to support both `--foo bar` and `--foo=bar` style completions.  
`=` should have been removed from `COMP_WORDBREAKS` when setting `$cur` for this to be useful.

### Returns
0 if current option was split  
1 otherwise


## _variables()
Complete variables.

### Returns
True (0) if variables were completed,  
False (> 0) if not.


## _init_completion()
Initialize completion and deal with various general things: do file and variable completion where appropriate, and adjust `prev`, `words`, and `cword` as if no redirections exist so that completions do not need to deal with them.  
Before calling this function, make sure `cur`, `prev`, `words`, and `cword` are `local`, ditto split if you use `-s`.

### Options

### Available OPTIONS
| option | description |
| --- | --- |
| -n EXCLUDE | Passed to `_get_comp_words_by_ref -n` with redirection chars |
| -e XSPEC   | Passed to `_filedir` as first arg for `stderr` redirections |
| -o XSPEC   | Passed to `_filedir` as first arg for other output redirections |
| -i XSPEC   | Passed to `_filedir` as first arg for `stdin` redirections |
| -s         | Split long options with `_split_longopt`, implies `-n =` |

### Returns
True (0) if completion needs further processing,  
False (> 0) no further processing is necessary.


## __parse_options()
Helper function for `_parse_help` and `_parse_usage`.


## _parse_help()
Parse GNU style help output of the given command.

### Parameters
| param | description |
| --- | --- |
| $1 | command; if `-`, read from `stdin` and ignore rest of args |
| $2 | command options (default: `--help`) |


## _parse_usage()
Parse BSD style usage output (options in brackets) of the given command.

### Parameters
| param | description |
| --- | --- |
| $1 | command; if `-`, read from `stdin` and ignore rest of args |
| $2 | command options (default: `--usage`) |


## _signals()
This function completes on signal names (minus the `SIG` prefix)

### Parameters
| param | description |
| --- | --- |
| $1 | prefix |


## _mac_addresses()
This function completes on known mac addresses


## _configured_interfaces()
This function completes on configured network interfaces


## _ip_addresses()
Local IP addresses.


## _kernel_versions()
This function completes on available kernels


## _available_interfaces()
This function completes on all available network interfaces

### Options
| option | description |
| --- | --- |
| -a | restrict to active interfaces only |
| -w | restrict to wireless interfaces only |


## _ncpus()
Echo number of CPUs, falling back to 1 on failure.


## _tilde()
Perform tilde (`~`) completion

### Returns
True (0) if completion needs further processing,  
False (> 0) if tilde is followed by a valid username, completions are put in `COMPREPLY` and no further processing is necessary.


## __expand_tilde_by_ref()
Expand variable starting with tilde (`~`)  
We want to expand `~foo/...` to `/home/foo/...` to avoid problems when word-to-complete starting with a tilde is fed to commands and ending up quoted instead of expanded.  
Only the first portion of the variable from the tilde up to the first slash (`~../`) is expanded.  
The remainder of the variable, containing for example a dollar sign variable (`$`) or asterisk (`*`) is not expanded.  

### Example usage
```
v="~"; __expand_tilde_by_ref v; echo "$v"  
```

### Example output
```
       v                  output
    --------         ----------------
    ~                /home/user
    ~foo/bar         /home/foo/bar
    ~foo/$HOME       /home/foo/$HOME
    ~foo/a  b        /home/foo/a  b
    ~foo/*           /home/foo/*
```

### Parameters
| param | description |
| --- | --- |
| $1 | Name of variable (not the value of the variable) to expand |


## _expand()
This function expands tildes in pathnames


## _uids()
This function completes on user IDs


## _gids()
This function completes on group IDs


## _xinetd_services()
Complete on xinetd services


## _services()
This function completes on services


## _service()
This completes on a list of all available service scripts for the `service` command and/or the SysV `init.d` directory, followed by that script's available commands


## _modules()
This function completes on modules


## _installed_modules()
This function completes on installed modules


## _usergroup()
This function completes on `user` or `user:group` format; as for `chown` and `cpio`.  
The `:` must be added manually; it will only complete usernames initially.  
The legacy `user.group` format is not supported.

### Parameters
| param | description |
| --- | --- |
| $1 | If `-u`, only return users/groups the user has access to in context of current completion. |


## _shells()
This function completes on valid shells


## _fstypes()
This function completes on valid filesystem types


## _realcommand()
Get real command.

### Parameters
| param | description |
| --- | --- |
| $1 | command |

### stdout
Filename of command in `PATH` with possible symbolic links resolved.  
Empty string if command not found.

### Return
True (0) if command found,  
False (> 0) if not.


## _get_first_arg()
This function returns the first argument, excluding options

### Parameters
| param | description |
| --- | --- |
| $1 | chars - Characters out of `$COMP_WORDBREAKS` which should **NOT** be considered word breaks. |

### See
`__reassemble_comp_words_by_ref`


## _count_args()
This function counts the number of args, excluding options

### Parameters
| param | description |
| --- | --- |
| $1 | chars - Characters out of $COMP_WORDBREAKS which should **NOT** be considered word breaks. |

### See
`__reassemble_comp_words_by_ref`


## _pci_ids()
This function completes on PCI IDs


## _usb_ids()
This function completes on USB IDs


## _cd_devices()
CD device names


## _dvd_devices()
DVD device names


## _terms()
`TERM` environment variable values


## _user_at_host()
This function provides simple `user@host` completion


## _known_hosts()
**@deprecated** Using this function as a helper function is deprecated. Use `_known_hosts_real` instead.


## _known_hosts_real()
Helper function for completing _known_hosts.  
This function performs host completion based on ssh's `config` and `known_hosts` files, as well as hostnames reported by `avahi-browse` if `COMP_KNOWN_HOSTS_WITH_AVAHI` is set to a non-empty value.  
Also hosts from `HOSTFILE` (`compgen -A hostname`) are added, unless `COMP_KNOWN_HOSTS_WITH_HOSTFILE` is set to an empty value.

### Usage
```
_known_hosts_real [OPTIONS] CWORD
```

### Options
| option | description |
| --- | --- |
| -a | Use aliases |
| -c | Use `:` suffix |
| -F configfile | Use `configfile` for configuration settings |
| -p PREFIX | Use PREFIX |

### Return
Completions, starting with `CWORD`, are added to `COMPREPLY[]`


## _cd()
This meta-cd function observes the `CDPATH` variable, so that `cd` additionally completes on directories under those specified in `CDPATH`.


## _command()
A wrapper method for the `_command_offset()`, when the offset is unknown


## _command_offset()
A meta-command completion function for commands like `sudo(8)`, which need to first complete on a command, then complete according to that command's own completion definition.


## _complete_as_root()
Return true if the completion should be treated as running as root


## _minimal()
Minimal completion to use as fallback in `_completion_loader`.


## _completion_loader()
Set up dynamic completion loading


## _xfunc()
Function for loading and calling functions from dynamically loaded completion files that may not have been sourced yet.

### Parameters
| param | description |
| --- | --- |
| $1 | completion file to load function from in case it is missing |
| $2... | function and its arguments |
