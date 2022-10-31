# test/deprecated/completions

This directory should contain a non-underscore prefixed symlink to
corresponding underscore prefixed, deprecated completions we have in the tree.

The test suite sets up loading of completions so that this dir is preferred
over system install locations, in order to test our deprecated in-tree
completions over possibly installed non-deprecated out-of-tree ones.
