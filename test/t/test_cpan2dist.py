import pytest


class TestCpan2dist:
    @pytest.mark.complete("cpan2dist -", require_cmd=True)
    def test_1(self, completion):
        assert completion
