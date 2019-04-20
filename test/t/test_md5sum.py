import pytest


class TestMd5sum:
    @pytest.mark.complete("md5sum ")
    def test_1(self, completion):
        assert completion
