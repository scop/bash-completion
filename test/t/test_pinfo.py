import pytest


@pytest.mark.pre_commands(
    "INFOPATH+=:info:",
)
class Test(object):

    @pytest.mark.complete("pinfo -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("pinfo bash")
    def test_bash(self, completion):
        assert completion.list
