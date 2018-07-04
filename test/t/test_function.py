import pytest


class Test(object):

    @pytest.mark.complete("function _parse_")
    def test_parse(self, completion):
        assert completion.list
