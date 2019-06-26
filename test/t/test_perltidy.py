import pytest


class TestPerltidy:
    @pytest.mark.complete("perltidy ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("perltidy -h", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("perltidy -ole=", require_cmd=True)
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete("perltidy -doesntexist=", require_cmd=True)
    def test_4(self, completion):
        assert not completion
