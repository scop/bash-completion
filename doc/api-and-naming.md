# API and naming

Due to its nature, bash-completion adds a number of functions and variables in
the shell's environment.

|                                   | `bash_completion`   | `completions/*`                                                            |
| :-------------------------------- | :------------------ | :------------------------------------------------------------------------- |
| public configuration variables    | `BASH_COMPLETION_*` | `BASH_COMPLETION_CMD_${Command^^}_${Config^^}`                             |
| non-local internal variables      | `_comp__*`          | `_comp_cmd_${Command}__${Data}`                                            |
| exporter function local variables | `_*` (not `_comp*`) | `_*` (not `_comp*`)                                                        |
| public/exported functions         | `_comp_*`           | `_comp_cmd_${Command}` (functions for `complete -F`)                       |
|                                   |                     | `_comp_xfunc_${Command}_${Utility}` (functions for use with `_comp_xfunc`) |
| private/internal functions        | `_comp__*`          | `_comp_cmd_${Command}__${Utility}` (utility functions)                     |

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
