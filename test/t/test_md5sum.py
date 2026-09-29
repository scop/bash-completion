import pytest


class TestMd5sum:
    @pytest.mark.complete("md5sum ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("md5sum --", require_longopt=True)
    def test_options(self, completion):
        assert completion
