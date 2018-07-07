import pytest


class TestMontage(object):

    @pytest.mark.complete("montage ")
    def test_1(self, completion):
        assert completion.list
