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

## `[[ $was_split ]] && return`

Should be used in completions using the `-s` flag of `_comp_initialize`,
or other similar cases where `_comp__split_longopt` has been invoked, after
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

## Function and variable names

See [API and naming](api-and-naming.md).

## Quoting of words

To avoid unexpected word splitting and pathname expansions, an argument of
commands needs to be properly quoted when it contains shell expansions such as
`$var`, `$(cmd)`, and `$((expr))`.

When one intentionally wants word splitting and pathname expansions, one should
consider using the utility functions provided by bash-completion.  To safely
split a string without being affected by non-standard `IFS` and pathname
expansions, use the shell function `_comp_split`.  To safely obtain filenames
by pathname expansions without being affected by `failglob`, etc., use the
shell function `_comp_expand_glob`.  Note that `_comp_expand_glob` should be
always used for the pathname patterns even if the pattern does not contain
shell expansions.

In the following contexts, the quoting to suppress word splitting and pathname
expansions are not needed.

- The right-hand sides of variable assignments ... `v=WORD` (e.g. `v=$var`)
- The arguments of conditional commands ... `[[ WORD ]]` (e.g. `[[ $var ]]`)
- The argument specified to `case` statement ... `case WORD in foo) ;; esac`
  (e.g. `case $var in foo) ;; esac`)

In bash-completion, we do not quote them by default.  However, there are
exceptions where the quoting is still needed for other reasons.

- When the word *directly* contains shell special characters (space, tab,
  newline, or a character from ``;|&()<>\\$`'"#!~{``), these characters need to
  be quoted.  The "*directly*" means that the special characters produced by
  shell expansions are excluded here.  For example, when one wants to include a
  whitespace as a part of the value of the word, the right-hand side can be
  quoted as `v="a b"`.
- An empty word (i.e., the word whose value is an empty string) is specified by
  `""`.  The right-hand side of an assignment technically can be an empty
  string as `var=`, but we still use `var=""` there because `shellcheck`
  suggests that e.g. `var= cmd` is confusing with `var=cmd`.
- `$*` and `${array[*]}` need to be always quoted because they can be affected
  by the word splitting in bash <= 4.2 even in the above contexts.
- In the following contexts, double-quoting of shell expansions is needed
  unless the result of expansions is intentionally treated as glob patterns or
  regular expressions.
  - The right-hand sides of `==`, `!=`, and `=~` in the conditional commands
    ... `[[ word == "$var" ]]`
  - The case patterns ... `case word in "$var") ;; esac`

Note: Here strings `cat <<<$var` are also supposed to be safe against word
splitting and pathname expansions without quoting, but bash <= 4.3 has a bug
[1], so they need to be quoted for as long as we support bash 4.3.

- [koalaman/shellcheck#1009 (comment)](https://github.com/koalaman/shellcheck/issues/1009#issuecomment-488395630)

There are also preferences on the type of quoting, which are though not too
strict.  We prefer to use double quotes over single quotes by default.  When
the value contains `$`, `` ` ``, `\`, and `"`, we can use single quotes to
avoid backslash escaping or use the one that minimizes the use of backslash
escaping.  When the value contains control characters such as a tab and a
newline, we do not directly include them but we use backslash escape sequences
such as `\t` and `\n` in the escape string `$'...'`.

### `patsub_replacement` for array elements

There is a subtlety in quoting of the array expansions with a pattern
replacement when `shopt -s patsub_replacement` (Bash >= 5.2) is
enabled (which is the default of Bash >= 5.2).

For example, the array expansions with a pattern replacement may be
used to add a prefix to every element in an array:

```bash
# problem in bash >= 5.2
arr=("${arr[@]/#/$prefix}")
```

However, this has the problem.  The characters `&` contained in
`$prefix`, if any, will be replaced with the matched string.  The
unexpected `patsub_replacement` may be suppressed by quoting the
replacement as

```bash
# problem with bash <= 4.2 or "shopt -s compat42"
arr=("${arr[@]/#/"$prefix"}")
```

However, this has another problem in bash < 4.3 or when `shopt -s
compat42` is turned on.  The inner double quotations are treated
literally so that the `PREFIX` instead of ``"PREFIX"` is prefixed to
elements.  To avoid this situation, the outer double quotations might
be removed, but this has even another problem of the pathname
expansions and `IFS`.

Specifically for prefixing and suffixing, we may instead use
`_comp_compgen -- -P prefix` and `_comp_compgen -- -S suffix`.

```bash
# solution for prefixing
_comp_compgen -Rv arr -- -P "$prefix" -W '"${arr[@]}"'
```

In a general case, one needs to modify each array element in a loop,
where only the replacement is quoted.

```bash
# general solution
for i in "${!arr[@]}"; do
    arr[i]=${arr[i]//pat/"$rep"}
done
```
