import pytest


@pytest.mark.bashcomp(
    pre_cmds=(
        "INFOPATH+=:$PWD/info:",
    ),
)
class TestPinfo(object):

    @pytest.mark.complete("pinfo -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("pinfo bash")
    def test_2(self, completion):
        assert completion.list
