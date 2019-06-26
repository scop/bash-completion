import pytest


@pytest.mark.bashcomp(cmd="pylint-3")
class TestPylint3:
    @pytest.mark.complete("pylint-3 --v", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pylint-3 http.clien")
    def test_2(self, completion):
        assert completion
