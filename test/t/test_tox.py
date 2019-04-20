import pytest


class TestTox:
    @pytest.mark.complete("tox -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("tox -e ")
    def test_2(self, completion):
        assert completion == "ALL"

    @pytest.mark.complete("tox -e foo,")
    def test_3(self, completion):
        assert completion == "foo,ALL"
