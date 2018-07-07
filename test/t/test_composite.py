import pytest


class TestComposite(object):

    @pytest.mark.complete("composite ")
    def test_1(self, completion):
        assert completion.list
