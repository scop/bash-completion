# test/fallback/completions

This directory should contain a non-underscore prefixed symlink to
corresponding underscore prefixed, fallback completions we have in the tree.

The test suite sets up loading of completions so that this dir is preferred
over system install locations, in order to test our fallback in-tree
completions over possibly installed non-fallback out-of-tree ones.
