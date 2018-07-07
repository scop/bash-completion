import pytest


class TestGendiff(object):

    @pytest.mark.complete("gendiff ")
    def test_1(self, completion):
        assert completion.list
