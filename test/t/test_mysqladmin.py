import pytest


class TestMysqladmin(object):

    @pytest.mark.complete("mysqladmin -")
    def test_1(self, completion):
        assert completion.list
