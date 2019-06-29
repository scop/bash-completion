import pytest


class TestPvscan:
    @pytest.mark.complete("pvscan --", xfail="! pvscan --help &>/dev/null")
    def test_1(self, completion):
        assert completion
