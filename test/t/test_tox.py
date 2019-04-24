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

    @pytest.mark.complete("tox -e foo -- ")
    def test_4(self, completion):
        """Test that ending in '-- ' triggers filename completion."""
        assert completion

    @pytest.mark.complete("tox -e foo -- -foo -bar ")
    def test_5(self, completion):
        """Test that arguments after '--' trigger filename completion."""
        assert completion

    @pytest.mark.complete("tox -e foo --")
    def test_6(self, completion):
        """Test that ending in '--' does not trigger filename completion."""
        for c in completion:
            assert c.startswith("--")
