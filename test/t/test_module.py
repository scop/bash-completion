import pytest


class TestModule(object):

    @pytest.mark.complete("module ")
    def test_1(self, completion):
        assert completion.list
