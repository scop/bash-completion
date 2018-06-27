import pytest


@pytest.mark.command("update-rc.d")
class Test(object):

    @pytest.mark.complete("update-rc.d -")
    def test_dash(self, completion):
        assert completion.list
