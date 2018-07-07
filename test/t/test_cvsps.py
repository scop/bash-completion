import pytest


@pytest.mark.pre_commands(
    "HOME=$PWD/cvs",
)
class TestCvsps(object):

    @pytest.mark.complete("cvsps -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("cvsps ")
    def test_2(self, completion):
        assert [x for x in completion.list if ":pserver:" in x]
