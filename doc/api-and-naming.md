# API and naming

## General API conventions

Most of the functions in bash-completion generate completions and directly
inject them to the `COMPREPLY` array variable, as required for completions to
work.

Most other functions make use of "output" variables, i.e. assign values to
them. The most common one of these is named `ret`. Consult the commentary
before each function in the source to find out the specific names.
`local`izing output variables before invoking a function that populates them
is the caller's responsibility.
Note that if calling multiple functions that assign output to the same variable
during one completion function run, each result should be copied to another
variable between the calls to avoid it possibly being overwritten and lost on
the next call. Also, the variables should also be ensured to be clear before
each call that references the value, variable name, or their existence,
typically by `unset -v`ing them when multiple such calls are used,
to avoid them interfering with each other.

Everything in fallback completion files (ones starting with an underscore)
is considered private and is to be named accordingly. Fallback files are not
intended to be explicitly used with `_comp_xfunc`, and completion files having
precedence over them may have a different API.

## Availability

All public API functions and variables are marked with a `@since VERSION`
comment, where `VERSION` is the bash-completion version the thing was
introduced in.

Similarly, deprecated functions and variables are either marked with a
`@deprecated VERSION ...` comment, or deprecated using the
`_comp_deprecate_func VERSION OLD_NAME NEW_NAME` function.
`VERSION` in both cases is the bash-completion version the thing was
deprecated in.

## Naming

Due to its nature, bash-completion adds a number of functions and variables in
the shell's environment.

|                                     | `bash_completion`   | `completions/*`                                                            |
|:------------------------------------|:--------------------|:---------------------------------------------------------------------------|
| public configuration variables      | `BASH_COMPLETION_*` | `BASH_COMPLETION_CMD_${Command^^}_${Config^^}`                             |
| private non-local variables         | `_comp__*`          | `_comp_cmd_${Command}__${Data}`                                            |
| private non-local mutable variables | `_comp__*_mut_*`    | `_comp_cmd_${Command}__mut_${Data}`                                        |
| exporter function local variables   | `_*` (not `_comp*`) | `_*` (not `_comp*`)                                                        |
| public/exported functions           | `_comp_*`           | `_comp_cmd_${Command}` (functions for `complete -F`)                       |
|                                     |                     | `_comp_xfunc_${Command}_${Utility}` (functions for use with `_comp_xfunc`) |
| private/internal functions          | `_comp__*`          | `_comp_cmd_${Command}__${Utility}` (utility functions)                     |

`${Command}` refers to a command name (with characters not allowed in POSIX
function or variable names replaced by an underscore), `${Config}` the name of
a configurable thing, `^^` means uppercase, `${Data}` is an identifier for the
data contained in the variable, and `${Utility}` describes the typical usage of
the function.

Variables and functions affecting multiple completions are usually defined
in the main `bash_completion` file and do not require any additional files to
be sourced. Variables and functions in command specific completion files in
`completions/*` follow a slightly different naming scheme; they include
`cmd` in their name as well as the name of the command.

Public configuration variables are shell ones that affect the runtime behavior
of various completions. As a rule of thumb, we lean towards not providing
customizability but rather strive to provide great completion behavior out of
the box. But there are some, see [configuration](configuration.md).

Variables and functions whose name contains a double underscore (`__`) anywhere
in their name are private implementation details, not part of the stable API,
and not intended to be used outside of their defining context. Internally, the
double underscores serve as privacy scope delimiters; there can be more than one
pair of them in a name, and functions and variables are intended to reference
and call other functions and variables within that scope, one level deep,
sharing a common prefix. For example, a function named `_comp_foo` is "allowed"
to access `_comp_foo__*` where `*` does not contain any double underscores,
i.e. it should not access `_comp_foo__something__*` despite the common prefix.

Private non-local variables are considered readonly by default.  When a
completion function needs to change variables for e.g. caching purposes, the
variables should contain the infix `*_mut_*` anywhere in their names.  This is
needed to tell the test framework to allow these variables changing.
Nevertheless, the completion results should be consistent among different calls
and unaffected by the state of the cache variables when it is called.

Internal local variables of functions that "export" their results using a
variable name that is passed in start with an underscore and do not start with
`_comp`. The variable names that are passed in for this purpose must not start
with an underscore.

Functions with names prefixed with `_comp_xfunc_` are intended to be used
through the `_comp_xfunc` function from files other than the one they are
defined in. From the same file they can be used directly using their complete
name.

Function names start with an underscore in order to avoid them being
included in completions of command names. (Except naturally when a command
starting with an underscore is being completed.) The underscore prefix does
not have anything to do with whether the thing is considered public or
private in the API, nor anything else really.

The `BASH_COMPLETION_` prefix provides a namespace and makes it clear what
these variables relate to. The `_comp` in other names serves a similar purpose,
but because these are used a lot in the code (unlike the public configuration
variables), using something shorter is beneficial. We hope and believe this is
distinctive and clash free enough.

It is known that a lot of functions and variables in the tree do not follow
these naming rules yet. Things introduced after version 2.11 should, and we are
evaluating our options for handling older ones.
