import pytest


class TestDesktopFileValidate(object):

    @pytest.mark.complete("desktop-file-validate ")
    def test_1(self, completion):
        assert completion.list
