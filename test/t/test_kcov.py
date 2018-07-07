import pytest


class TestKcov(object):

    @pytest.mark.complete("kcov ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("kcov --exclude-patter")
    def test_2(self, completion):
        assert completion.list == ["--exclude-pattern="]
        assert completion.line.endswith("=")

    @pytest.mark.complete("kcov -l 42,")
    def test_3(self, completion):
        assert completion.list
