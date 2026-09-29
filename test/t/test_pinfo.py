import pytest


@pytest.mark.bashcomp(pre_cmds=("INFOPATH+=:$PWD/info:",))
class TestPinfo:
    @pytest.mark.complete("pinfo -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pinfo bash")
    def test_2(self, completion):
        assert completion
