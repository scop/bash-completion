import pytest


@pytest.mark.command("invoke-rc.d")
class Test(object):

    @pytest.mark.complete("invoke-rc.d ")
    def test_(self, completion):
        assert completion.list
