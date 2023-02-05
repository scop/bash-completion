import pytest


class TestCreateuser:
    # --help can fail due to missing package dependencies, e.g. on Ubuntu 14
    @pytest.mark.complete(
        "createuser -", xfail="! createuser --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
