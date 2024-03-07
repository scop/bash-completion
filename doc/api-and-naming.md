# API and naming

## General API conventions

Most of the functions in bash-completion generate completions and directly
inject them to the `COMPREPLY` array variable, as required for completions to
work.

Most other functions make use of "output" variables, i.e. assign values to
them.  The name of an output variable should be basically in lowercase.
Consult the commentary before each function in the source to find out the
specific names. `local`izing output variables before invoking a function that
populates them is the caller's responsibility.  Note that if calling multiple
functions that assign output to the same variable during one completion
function run, each result should be copied to another variable between the
calls to avoid it possibly being overwritten and lost on the next call.
The variables should also be ensured to be clear before each call that
references the value, variable name, or their existence, typically by `unset
-v`ing them when multiple such calls are used, to avoid them interfering with
each other.

The most common output variable is named `REPLY`.  The use of the uppercase is
unconventional, but this choice of the name is intended to be consistent with
the value substitutions `${| func; }`, which is originally supported by mksh
and will be supported by Bash >= 5.3.  The value substitutions are replaced by
the contents of the output variable `REPLY` set by `func`.  Although we cannot
currently assume Bash 5.3 in the codebase, we can switch to the value
substitutions at the point Bash <= 5.2 disappears from the market.

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

|                                     | `bash_completion`   | `completions/*`                                                                       |
|:------------------------------------|:--------------------|:--------------------------------------------------------------------------------------|
| public configuration variables      | `BASH_COMPLETION_*` | `BASH_COMPLETION_CMD_${Command^^}_${Config^^}`                                        |
| private non-local variables         | `_comp__*`          | `_comp_cmd_${Command}__${Data}`                                                       |
| private non-local mutable variables | `_comp__*_mut_*`    | `_comp_cmd_${Command}__mut_${Data}`                                                   |
| exporter function local variables   | `_*` (not `_comp*`) | `_*` (not `_comp*`)                                                                   |
| public/exported functions           | `_comp_*`           | `_comp_xfunc_${Command}_${Utility}` (functions for use with `_comp_xfunc`)            |
| - completers (for `complete -F`)    | `_comp_complete_*`  | `_comp_cmd_${Command}`                                                                |
| - generators                        | `_comp_compgen_*`   | `_comp_xfunc_${Command}_compgen_${Name}` (generators for use with `_comp_compgen -x`) |
| private/internal functions          | `_comp__*`          | `_comp_cmd_${Command}__${Utility}` (utility functions)                                |
| - generators                        |                     | `_comp_cmd_${Command}__compgen_${Name}` (generators for use with `_comp_compgen -i`)  |

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

## Exported functions (xfunc)

Exported functions (xfunc) are the functions defined in completion files for
specific commands but exposed to other completion files.  The xfuncs have the
name `_comp_xfunc_CMD_NAME` where `CMD` is the name of the associated command,
and `NAME` is the name of the utility.  The other functions defined in specific
completion files are considered private and should not be called outside the
file.

The xfuncs can be called by `_comp_xfunc CMD NAME ARGS` from external files.
The xfuncs are supposed to be directly called as `_comp_xfunc_CMD_NAME ARGS`
from the same file where they are defined, or if they wrap a `_comp_cmd_NAME__*`
function, that one should be called directly instead.

Note: The name `xfunc` was initially the name of a utility function, `_xfunc`,
to call "eXternal FUNCtions" that are defined in other completion files.  The
concept is later extended to also mean "eXported".

## Generator functions

The generator functions, which have names of the form `_comp_compgen_NAME`, are
used to generate completion candidates.  A generator function is supposed to be
called by `_comp_compgen [OPTS] NAME ARGS` where `OPTS = -aRl|-v var|-c cur|-C
dir|-F sep` are the options to modify the behavior (see the code comment of
`_comp_compgen` for details).  When there are no `opts`, the generator function
is supposed to be directly called as `_comp_compgen_NAME ARGS`.  The result is
stored in the target variable (which is `COMPREPLY` by default but can be
specified by `-v var` in `OPTS`).

### Implementing a generator function

To implement a generator function, one should generate completion candidates by
calling `_comp_compgen` or other generators.

To avoid conflicts with the options specified to `_comp_compgen`, one should
not directly modify or reference the target variable.  When post-filtering is
needed, store them in a local array, filter them, and finally append them by
`_comp_compgen -- -W '"${_arr[@]}"'`.  To split the output of commands and
append the results to the target variable, use `_comp_compgen_split -- "$(cmd
...)"` instead of using `_comp_split COMPREPLY "$(cmd ...)"`.

A generator function should replace the existing content of the variable by
default.  When the appending behavior is favored, the caller should specify it
through `_comp_compgen -a NAME`.  The generator function does not need to
process it because internal `_comp_compgen` calls automatically reflect the
option `-a` specified to the outer calls of `_comp_compgen`.

The exit status is implementation-defined.

- The `_comp_compgen -- COMPGEN_ARGS` returns whether there is at least one
  completion.  This is useful when one wants to reuse the array content with
  `"${tmp[@]}"` avoiding `nounset` error.
- Some use other rules for the exit status. E.g., `help` and `usage` return
  whether there were options *before* filtering by cur. This is used for
  `_comp_compgen_help || _comp_compgen_usage`.

Whether to clear the target variable on runtime error (when `-a` is not
specified in `OPTS`) is implementation-defined.  On the other hand, the
generator function should not leave any side effects in the target variable on
usage error.  Note that the target variable might be cleared by the internal
calls of `_comp_compgen`.  To explicitly clear the target variable,
`_comp_compgen_set` can be called without arguments.

Exported generators are defined with the names `_comp_xfunc_CMD_compgen_NAME`
and called by `_comp_compgen [opts] -x CMD NAME args`.  Internal generators are
defined with the names `_comp_cmd_CMD__compgen_NAME` and called by
`_comp_compgen [opts] -i CMD NAME args`.

#### Local variables of generator and `_comp_compgen -U var`

A generator should basically define local variables with the names starting
with `_`.  However, a generator sometimes needs to use local variable names
that do not start with `_`.  When the child generator call with a variable name
(such as `local var; _comp_compgen -v var`) is used within the generator, the
local variable can unexpectedly mask a local variable of the upper call.

For example, the following call fails to obtain the result of generator
`mygen1` because the array `arr` is masked by the same name of a local variable
in `_comp_compgen_mygen1`.

```bash
# generator with a problem
_comp_compgen_mygen1()
{
    local -a arr=(1 2 3)
    _comp_compgen -av arr -- -W '4 5 6'
    _comp_compgen_set "${arr[@]/#p}"
}

_comp_compgen -v arr mygen1 # fails to get the result in array `arr`
```

To avoid this, a generator that defines a local variable with its name not
starting with `_` can use the option `-U var` to unlocalize the variable on
assigning the final result.

```bash
# properly designed generator
_comp_compgen_mygen1()
{
    local -a arr=(1 2 3)
    _comp_compgen -av arr -- -W '4 5 6'
    _comp_compgen -U arr set "${arr[@]/#p}"
}
```

To avoid unexpected unlocalization of previous-scope variables, a generator
should specify `-U var` to a child generator (that attempts to store results to
the current target variable) at most once.
