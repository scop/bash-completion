import pytest


class Test(object):

    @pytest.mark.complete("reportbug --m")
    def test_m(self, completion):
        assert completion.list
