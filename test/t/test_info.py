import pytest


@pytest.mark.pre_commands(
    "INFOPATH+=:info:",
)
class TestInfo(object):

    @pytest.mark.complete("info bash")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("info -")
    def test_2(self, completion):
        assert completion.list
