import pytest


class TestOpenssl:
    @pytest.mark.complete("openssl ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("openssl pkey -cipher ", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("openssl dgst -s", require_cmd=True)
    def test_3(self, completion):
        assert completion
        assert any(x.startswith("-sha") for x in completion)
