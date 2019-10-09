import pytest


class TestP11Kit:
    @pytest.mark.complete("p11-kit l")
    def test_1(self, completion):
        assert completion == "list-modules"

    @pytest.mark.complete("p11-kit -v l")
    def test_1(self, completion):
        assert completion == "list-modules"

    @pytest.mark.complete("p11-kit e")
    def test_2(self, completion):
        assert completion == "extract"

    @pytest.mark.complete("p11-kit ")
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete("p11-kit -", require_cmd=True)
    def test_4(self, completion):
        assert completion
