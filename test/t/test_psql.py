import pytest


class TestPsql:
    # --help can fail due to missing package dependencies, e.g. on Ubuntu 14
    @pytest.mark.complete(
        "psql -", require_cmd=True, xfail="! psql --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
