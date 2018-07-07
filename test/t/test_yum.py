import pytest


class TestYum(object):

    @pytest.mark.complete("yum -")
    def test_1(self, completion):
        assert completion.list
