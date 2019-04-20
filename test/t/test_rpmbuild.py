import pytest


class TestRpmbuild:
    @pytest.mark.complete("rpmbuild -")
    def test_1(self, completion):
        assert completion
