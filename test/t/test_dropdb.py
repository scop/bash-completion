import pytest


class TestDropdb:
    # --help can fail due to missing package dependencies, e.g. on Ubuntu 14
    @pytest.mark.complete(
        "dropdb -", require_cmd=True, xfail="! dropdb --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
