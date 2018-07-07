import pytest


class TestMogrify(object):

    @pytest.mark.complete("mogrify ")
    def test_1(self, completion):
        assert completion.list
