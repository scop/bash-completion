import pytest


class TestPaste(object):

    @pytest.mark.complete("paste ")
    def test_1(self, completion):
        assert completion.list
