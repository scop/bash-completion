import pytest


@pytest.mark.bashcomp(ignore_env=r"^-declare -f _vncviewer_bootstrap$")
class TestVncviewer:
    @pytest.mark.complete("vncviewer ")
    def test_1(self, completion):
        assert completion
