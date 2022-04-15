# Coding style guide

## Introduction

This document attempts to explain the basic styles and patterns that
are used in the bash completion. New code should try to conform to
these standards so that it is as easy to maintain as existing code.
Of course every rule has an exception, but it's important to know
the rules nonetheless!

This is particularly directed at people new to the bash completion
codebase, who are in the process of getting their code reviewed.
Before getting a review, please read over this document and make
sure your code conforms to the recommendations here.

## Indentation

Indent step should be 4 spaces, no tabs.

## Globbing in case labels

Avoid "fancy" globbing in case labels, just use traditional style when
possible. For example, do `--foo|--bar)` instead of `--@(foo|bar))`.
Rationale: the former is easier to read, often easier to grep, and
doesn't confuse editors as bad as the latter, and is concise enough.

## `[[ ]]` vs `[ ]`

Always use `[[ ]]` instead of `[ ]`. Rationale: the former is less error
prone, more featureful, and slightly faster.

## `$x` and `! $x` vs `-n $x` and `-z $x`

Use `[[ $x ]]` and `[[ ! $x ]]` instead of `[[ -n $x ]]` and `[[ -z $x ]]`,
and similarly with the `test` builtin.
Rationale: no strong technical reasons to prefer either style, but the former
is subjectively slightly more readable and it was traditionally more common in
the codebase before this style item was standardized.

## Line wrapping

Try to wrap lines at 79 characters. Never go past this limit, unless
you absolutely need to (example: a long sed regular expression, or the
like). This also holds true for the documentation and the testsuite.
Other files, like ChangeLog, or COPYING, are exempt from this rule.

## `$( )` vs backticks

When you need to do some code substitution in your completion script,
you _MUST_ use the `$(...)` construct, rather than backticks. The former
is preferable because anyone, with any keyboard layout, is able to
type it. Backticks aren't always available, without doing strange
key combinations.

## `-o filenames`

As a rule of thumb, do not use `complete -o filenames`. Doing it makes
it take effect for all completions from the affected function, which
may break things if some completions from the function must not be
escaped as filenames. Instead, use `compopt -o filenames` to turn on
`-o filenames` behavior dynamically when returning completions that
need that kind of processing (e.g. file and command names). The
`_filedir` and `_filedir_xspec` helpers do this automatically whenever
they return some completions.

## `[[ ${COMPREPLY-} == *= ]] && compopt -o nospace`

The above is functionally a shorthand for:

```bash
if [[ ${#COMPREPLY[@]} -eq 1 && ${COMPREPLY[0]} == *= ]]; then
    compopt -o nospace
fi
```

It is used to ensure that long options' name won't get a space
appended after the equal sign. Calling `compopt -o nospace` makes sense
in case completion actually occurs: when only one completion is
available in `COMPREPLY`.

## `$split && return`

Should be used in completions using the `-s` flag of `_init_completion`,
or other similar cases where `_split_longopt` has been invoked, after
`$prev` has been managed but before `$cur` is considered. If `$cur` of the
form `--foo=bar` was split into `prev=--foo` and `cur=bar`, and the `$prev`
block did not process the option argument completion, it makes sense to return
immediately after the $prev block because`--foo` obviously
takes an argument and the remainder of the completion function is
unlikely to provide meaningful results for the required argument.
Think of this as a catch-all for unknown options requiring an
argument.

Note that even when using this, options that are known to require an
argument but for which we don't have argument completion should be
explicitly handled (non-completed) in the `$prev` handling block because
`--foo=bar` options can often be written without the equals sign, and in
that case the long option splitting does not occur.

## Use arithmetic evaluation

When dealing with numeric data, take advantage of arithmetic evaluation.
In essence, use `(( ... ))` whenever it can replace `[[ ... ]]` because the
syntax is more readable; no need for `$`-prefixes, numeric comparison etc
operators are more familiar and easier on the eye.

## Array subscript access

Array subscripts are arithmetic expressions, take advantage of that.
E.g. write `${foo[bar]}`, not `${foo[$bar]}`, and similarly `${foo[bar+1]}`
vs `${foo[((bar+1))]}` or `${foo[$((bar+1))]}`, `${foo[--i]}` vs
`${foo[((--i))]}`.

## Loop variable names

Use `i`, `j`, `k` for loop-local indices; `n` and `m` for lengths; some other
descriptive name typically based on array name but in singular when looping
over actual values. If an index or value is to be accessed later on instead of
being just locally for looping, use a more descriptive and specific name for
it.

## Function names

Use the `_comp_` prefix for all function names, and `_comp_cmd_` for functions
defined in per command completion files and not anywhere else. Prefixing with
an underscore helps keep the functions out of the way for most command name
completions (except obviously ones starting with an underscore or ones that have
nothing typed in yet), and having a consistent prefix helps avoid some clashes
and gives a hint where a function originates from.

It is known that a lot of functions in the tree do not follow this practice.
This is due to backwards compatibility reasons, but all functions introduced
after version 2.11 should follow this name prefix rule.

## Variable naming

To be written.
