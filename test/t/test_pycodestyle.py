import pytest


class TestPycodestyle:
    @pytest.mark.complete("pycodestyle ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pycodestyle -", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("pycodestyle --doesnt-exist=")
    def test_3(self, completion):
        assert not completion
