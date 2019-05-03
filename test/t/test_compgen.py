import pytest


class TestCompgen:
    @pytest.mark.complete(r"compgen -f a\'b/", cwd="compgen")
    def test_1(self, completion):
        assert not completion
