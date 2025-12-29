# helper AWK script for GNU make                                    -*- awk -*-

# This AWK script is used by the function `_comp_cmd_make__extract_targets` in
# `completions/make`.  This script receives the output of `make -npq' as the
# input file or stdin and outputs the list of targets matching the prefix.
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
/^# +Not a target/, /^$/     { next; }

# The stuff above here describes lines that are not
#  explicit targets or not targets other than special ones
# The stuff below here decides whether an explicit target
#  should be output.

# only process the targets the user wants.
starts_with($0, prefix) { is_target_block = 1; }
is_target_block == 0 { next; }

/^# +File is an intermediate prerequisite/ { # cancel the block
  is_target_block = 0;
  target = "";
  next;
}

# end of target block
/^$/ {
  is_target_block = 0;
  if (target != "") {
    print target;
    target = "";
  }
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

# ex: filetype=awk
