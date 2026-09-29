import pytest


class TestAptitude:
    @pytest.mark.complete("aptitude ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("aptitude -", require_cmd=True)
    def test_options(self, completion):
        assert completion

    @pytest.mark.complete("aptitude --", require_cmd=True)
    def test_long_options(self, completion):
        assert completion

    @pytest.mark.complete("aptitude -u -")
    def test_no_i_with_u(self, completion):
        assert "-i" not in completion

    @pytest.mark.complete("aptitude -i -")
    def test_no_u_with_i(self, completion):
        assert "-u" not in completion
