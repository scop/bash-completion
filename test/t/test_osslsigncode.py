import pytest


class TestOsslsigncode:
    @pytest.mark.complete("osslsigncode ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("osslsigncode -", require_cmd=True)
    def test_2(self, completion):
        assert completion
