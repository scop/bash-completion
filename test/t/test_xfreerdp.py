import pytest


class TestXfreerdp(object):

    @pytest.mark.complete("xfreerdp ")
    def test_1(self, completion):
        assert completion.list
