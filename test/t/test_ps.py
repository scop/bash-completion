import pytest


def is_int(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True


class TestPs:
    @pytest.mark.complete("ps -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ps --help ")
    def test_2(self, completion):
        assert completion == [
            "all",
            "list",
            "misc",
            "output",
            "simple",
            "threads",
        ]

    @pytest.mark.complete("ps --help all ")
    def test_3(self, completion):
        assert not completion

    @pytest.mark.complete("ps --version ")
    def test_4(self, completion):
        assert not completion

    @pytest.mark.complete("ps --pid ")
    def test_5(self, completion):
        assert completion
        assert all(map(is_int, completion))

    @pytest.mark.complete("ps --format ", require_cmd=True)
    def test_6(self, completion):
        assert completion
        assert all(map(lambda c: not c.startswith(("-", ",")), completion))

    @pytest.mark.complete("ps --format user,", require_cmd=True)
    def test_7(self, completion):
        assert completion
        assert all(map(lambda c: not c.startswith(("-", ",")), completion))
