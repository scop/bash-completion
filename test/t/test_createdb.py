import pytest


class TestCreatedb:
    # --help can fail due to missing package dependencies, e.g. on Ubuntu 14
    @pytest.mark.complete(
        "createdb -", require_cmd=True, xfail="! createdb --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
