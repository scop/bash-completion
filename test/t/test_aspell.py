import pytest


class TestAspell(object):

    @pytest.mark.complete("aspell ")
    def test_1(self, completion):
        assert completion.list
