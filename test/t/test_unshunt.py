import pytest


class TestUnshunt(object):

    @pytest.mark.complete("unshunt --")
    def test_1(self, completion):
        assert completion.list
