import pytest


@pytest.mark.bashcomp(
    pre_cmds=(
        "INFOPATH+=:$PWD/info:",
    ),
)
class TestInfo:

    @pytest.mark.complete("info bash")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("info -")
    def test_2(self, completion):
        assert completion.list
