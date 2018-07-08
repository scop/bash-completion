import pytest


@pytest.mark.bashcomp(
    skipif="! flake8 --help &>/dev/null",
)
class TestFlake8(object):

    @pytest.mark.complete("flake8 ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("flake8 -")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("flake8 --doesnt-exist=")
    def test_3(self, completion):
        assert not completion.list
