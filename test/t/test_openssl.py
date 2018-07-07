import pytest


class Test(object):

    @pytest.mark.complete("openssl ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("openssl pkey -cipher ")
    def test_pkey_cipher(self, completion):
        assert completion.list

    @pytest.mark.complete("openssl dgst -s")
    def test_dgst_s(self, completion):
        assert completion.list
