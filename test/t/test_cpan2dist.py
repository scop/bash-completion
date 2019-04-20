import pytest


class TestCpan2dist:
    @pytest.mark.complete("cpan2dist -")
    def test_1(self, completion):
        assert completion
