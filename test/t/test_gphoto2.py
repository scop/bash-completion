import pytest


class Test(object):

    @pytest.mark.complete("gphoto2 --")
    def test_dash(self, completion):
        assert completion.list
