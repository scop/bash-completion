import pytest


class TestHciattach(object):

    @pytest.mark.complete("hciattach ")
    def test_1(self, completion):
        assert completion.list
