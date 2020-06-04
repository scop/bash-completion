import pytest


class TestCrontab:
    @pytest.mark.complete("crontab ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("crontab -l -")
    def test_only_u_with_l(self, completion):
        assert completion == "u"

    @pytest.mark.complete("crontab -r -")
    def test_no_l_with_r(self, completion):
        assert completion
        assert "-l" not in completion
