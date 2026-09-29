import pytest


@pytest.mark.bashcomp(
    ignore_env=r"^-declare -f _comp_cmd_vncviewer__bootstrap$"
)
class TestVncviewer:
    @pytest.mark.complete("vncviewer ")
    def test_1(self, completion):
        assert completion
