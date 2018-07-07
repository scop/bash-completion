import pytest


class TestK3b(object):

    @pytest.mark.complete("k3b ")
    def test_1(self, completion):
        assert completion.list
