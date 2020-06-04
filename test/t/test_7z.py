import pytest


class Test7z:
    @pytest.mark.complete("7z ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("7z a ar -tzi")
    def test_2(self, completion):
        assert completion == "p"

    @pytest.mark.complete(r"7z x -wa\ ", cwd="_filedir")
    def test_3(self, completion):
        assert completion == "b/"
        assert not completion.endswith(" ")

    @pytest.mark.complete("7z x ", cwd="7z")
    def test_4(self, completion):
        assert completion == "a.7z"

    @pytest.mark.complete("7z d a.7z ", cwd="7z", require_cmd=True)
    def test_5(self, completion):
        assert completion == "abc"

    @pytest.mark.complete("7z a -air@", cwd="7z")
    def test_6(self, completion):
        assert completion == sorted("-air@a.7z -air@f.txt".split())

    @pytest.mark.complete("7z a -o")
    def test_7(self, completion):
        assert "-o7z/" in completion
        assert all(x.endswith("/") for x in completion)
