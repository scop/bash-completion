import pytest


@pytest.mark.xfail  # TODO: completion doesn't seem to be for ~2018 xfreerdp
class TestXfreerdp(object):

    @pytest.mark.complete("xfreerdp ")
    def test_1(self, completion):
        assert completion.list
