import pytest


class Test(object):

    @pytest.mark.complete("pkg_info ")
    def test_(self, completion):
        assert completion.list
