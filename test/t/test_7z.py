import pytest


class Test7z:

    @pytest.mark.complete("7z ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("7z a ar -tzi")
    def test_2(self, completion):
        assert completion.list == ["-tzip"]

    @pytest.mark.xfail  # TODO: whitespace split issue
    @pytest.mark.complete(r"7z x -wa\ ", cwd="_filedir")
    def test_3(self, completion):
        assert completion.list == [r"-wa\ b/"]
        assert not completion.output.endswith(" ")

    @pytest.mark.complete("7z x ", cwd="7z")
    def test_4(self, completion):
        assert completion.list == ["a.7z"]

    @pytest.mark.complete("7z d a.7z ", cwd="7z")
    def test_5(self, completion):
        assert completion.list == ["abc"]
