import pytest


class TestCreatedb(object):

    # --help can fail due to missing package dependencies, e.g. on Ubuntu 14
    @pytest.mark.complete("createdb -",
                          skipif="! createdb --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
