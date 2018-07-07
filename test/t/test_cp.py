import pytest


class TestCp(object):

    @pytest.mark.complete("cp ")
    def test_1(self, completion):
        assert completion.list
