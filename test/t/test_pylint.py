import pytest


class Test(object):

    @pytest.mark.complete("pylint --v")
    def test_v(self, completion):
        assert completion.list

    @pytest.mark.complete("pylint --confidence=HIGH,")
    def test_confidence(self, completion):
        assert completion.list
