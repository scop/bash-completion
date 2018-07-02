import pytest


class Test(object):

    @pytest.mark.complete("cdrecord -d")
    def test_d(self, completion):
        assert completion.list
