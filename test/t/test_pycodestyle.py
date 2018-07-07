import pytest


class TestPycodestyle(object):

    @pytest.mark.complete("pycodestyle ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("pycodestyle -")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("pycodestyle --doesnt-exist=")
    def test_3(self, completion):
        assert not completion.list
