import pytest


class TestMkdir:

    @pytest.mark.complete("mkdir ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.xfail  # TODO: whitespace split issue
    @pytest.mark.complete("mkdir ", cwd="shared/default")
    def test_2(self, completion):
        assert completion.list == ["bar bar.d/", "foo", "foo.d/"]

    @pytest.mark.xfail  # TODO: why path in completion.list, basename in .line?
    @pytest.mark.complete("mkdir shared/default/foo.d/")
    def test_3(self, completion):
        assert completion.line == "foo"
        assert completion.list == [completion.line]
