import pytest


class TestPostcat(object):

    @pytest.mark.complete("postcat ")
    def test_1(self, completion):
        assert completion.list
