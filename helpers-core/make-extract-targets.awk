# helper AWK script for GNU make

# This AWK script is used by the function `_comp_cmd_make__extract_targets` in
# `completions-core/make`.  This script receives the output of `make -npq' as
# the input file or stdin and outputs the list of targets matching the prefix.
# The phony targets are prefixed by "phony:", and the others are prefixed by
# "file:".
#
# @env prefix         Specifies the prefix to match.
# @env prefix_replace Specifies the string that replaces the prefix in the
#   output.  This is used when we want to omit the directory name in showing
#   the list of the completions.
#

BEGIN {
  prefix = ENVIRON["prefix"];
  prefix_replace = ENVIRON["prefix_replace"];
  is_target_block = 0;
  is_phony_target = 0;
  target = "";
}

function starts_with(str, prefix) {
  return substr(str, 1, length(prefix)) == prefix;
}

# skip any makefile outputs
NR == 1, /^# +Make data base/ { next; }
/^# +Finished Make data base/,/^# +Make data base/ { next; }

# skip until files section
/^# +Variables/, /^# +Files/ { next; }

# skip not-target blocks
/^# +Not a target/, /^$/ {
  # We need to manually clear the state.  Without it, the cleanup associated
  # with the present block would be skipped because /^$/ on the above line also
  # consumes the empty line.  This would become an issue with the case where
  # the "Not a target" line appears in the middle of a block, e.g., for the
  # case with "foobar: OUCH = glitch" without the actual rule for "foobar".
  # The leftover information would be associated with the next target block
  # unexpectedly.
  #
  # https://github.com/scop/bash-completion/pull/1577
  is_target_block = 0;
  is_phony_target = 0;
  target = "";
  next;
}

# The stuff above here describes lines that are not
#  explicit targets or not targets other than special ones
# The stuff below here decides whether an explicit target
#  should be output.

# only process the targets the user wants.
starts_with($0, prefix) { is_target_block = 1; }
is_target_block == 0 { next; }

/^# +File is an intermediate prerequisite/ { # cancel the block
  is_target_block = 0;
  is_phony_target = 0;
  target = "";
  next;
}

# The comment sections after the .PHONY targets include the following line,
# which was confirmed in make-3.80 (2002) and make-4.4.90 (master b380278,
# 2026):
#
# #  Phony target (prerequisite of .PHONY).
#
/^# +Phony target/ {
  is_phony_target = 1;
  next;
}

# end of target block
/^$/ {
  if (target != "") {
    if (is_phony_target) {
      print "phony:" target;
    } else {
      print "file:" target;
    }
    target = "";
  }
  is_target_block = 0;
  is_phony_target = 0;
  next;
}

# found target block
/^[^#\t:%]+:/ {
  # special targets
  if (/^\.PHONY:/               ) next;
  if (/^\.SUFFIXES:/            ) next;
  if (/^\.DEFAULT:/             ) next;
  if (/^\.PRECIOUS:/            ) next;
  if (/^\.INTERMEDIATE:/        ) next;
  if (/^\.SECONDARY:/           ) next;
  if (/^\.SECONDEXPANSION:/     ) next;
  if (/^\.DELETE_ON_ERROR:/     ) next;
  if (/^\.IGNORE:/              ) next;
  if (/^\.LOW_RESOLUTION_TIME:/ ) next;
  if (/^\.SILENT:/              ) next;
  if (/^\.EXPORT_ALL_VARIABLES:/) next;
  if (/^\.NOTPARALLEL:/         ) next;
  if (/^\.ONESHELL:/            ) next;
  if (/^\.POSIX:/               ) next;
  if (/^\.NOEXPORT:/            ) next;
  if (/^\.MAKE:/                ) next;

  # dont complete with hidden targets unless we are doing a partial completion
  if (prefix == "" || prefix ~ /\/$/)
    if (substr($0, length(prefix) + 1, 1) ~ /[^a-zA-Z0-9]/)
      next;

  target = $0;
  sub(/:.*/, "", target);
  if (prefix_replace != prefix)
    target = prefix_replace substr(target, 1 + length(prefix));

  next;
}
