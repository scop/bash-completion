import pytest


class TestTox:
    @pytest.mark.complete("tox -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("tox -e ", cwd="tox")
    def test_2(self, completion):
        assert all(x in completion for x in "py37 ALL".split())

    @pytest.mark.complete("tox -e foo,", cwd="tox")
    def test_3(self, completion):
        assert all(x in completion for x in "py37 ALL".split())

    @pytest.mark.complete("tox -e foo -- ", cwd="tox")
    def test_4(self, completion):
        """Test that ending in '-- ' triggers filename completion."""
        assert completion

    @pytest.mark.complete("tox -e foo -- -foo -bar ", cwd="tox")
    def test_5(self, completion):
        """Test that arguments after '--' trigger filename completion."""
        assert completion

    @pytest.mark.complete("tox -e foo --", cwd="tox")
    def test_6(self, completion):
        """Test that ending in '--' does not trigger filename completion."""
        for c in completion:
            assert c.startswith("--")
