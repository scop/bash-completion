import pytest


class Test(object):

    @pytest.mark.complete("write root")
    def test_root(self, completion):
        assert "root" in completion.list
