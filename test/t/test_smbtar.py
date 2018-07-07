import pytest


class TestSmbtar(object):

    @pytest.mark.complete("smbtar -")
    def test_1(self, completion):
        assert completion.list
