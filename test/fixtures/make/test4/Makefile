# Non-phony targets whose names contain `/' really are file paths, so the
# completion keeps collapsing shared prefixes into `dir/' (issues #544/#858).
# Crucially, a non-phony target that is *also* a directory prefix of others
# -- here `sub', a real directory created by a recipe, with children `sub/a'
# and `sub/b' -- must STAY collapsed to `sub/', never surfaced as a plain
# runnable `sub'.  Only `.PHONY' logical labels are offered as-is.

sub/a sub/b: | sub
	@echo $@

sub:
	@mkdir -p sub

# `dir' is NOT itself a target, only a shared path prefix, so completion still
# collapses to `dir/'.
dir/all dir/rule:
	@echo $@
