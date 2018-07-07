import pytest


@pytest.mark.pre_commands(
    "INFOPATH+=:info:",
)
class TestPinfo(object):

    @pytest.mark.complete("pinfo -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("pinfo bash")
    def test_2(self, completion):
        assert completion.list
