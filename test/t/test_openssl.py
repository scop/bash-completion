import pytest


class TestOpenssl:
    @pytest.mark.complete("openssl ", require_cmd=True)
    def test_1(self, completion):
        assert completion
        assert all(x in completion for x in "x509 dgst enc pkey".split())

    @pytest.mark.complete("openssl pkey -cipher ", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("openssl dgst -s", require_cmd=True)
    def test_3(self, completion):
        assert completion
        assert any(x.startswith("-sha") for x in completion)

    @pytest.mark.complete("openssl enc -a", require_cmd=True)
    def test_4(self, completion):
        assert completion
        assert any(x.startswith("-aes") for x in completion)
