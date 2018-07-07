import pytest


class TestGpg(object):

    @pytest.mark.complete("gpg ")
    def test_1(self, completion):
        assert completion.list
