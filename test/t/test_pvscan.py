import pytest


class TestPvscan:
    @pytest.mark.complete(
        "pvscan --", require_cmd=True, xfail="! pvscan --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
