import pytest


class TestInotifywait:
    @pytest.mark.complete("inotifywait ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("inotifywait --", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("inotifywait -e ", require_cmd=True)
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete("inotifywait -te ", cwd="_filedir")
    def test_4(self, completion):
        """Test for noargopts. Instead of generating the option argument of
        `-e`, we expect that completion for normal arguments would be
        invoked. This is because `-t` is an option taking an option argument
        and `e` is treated as the option argument of `-t` here.

        """
        assert "ab/" in completion

    @pytest.mark.complete("inotifywait @a", cwd="_filedir")
    def test_5(self, completion):
        """Test for the specification of the exclude filenames, which
        has the form `@filename`.

        """
        assert "@ab/" in completion
