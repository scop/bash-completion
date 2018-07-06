import pytest


class Test(object):

    # --help can fail due to missing package dependencies, e.g. on Ubuntu 14
    @pytest.mark.complete("createuser -",
                          skipif="! createuser --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
