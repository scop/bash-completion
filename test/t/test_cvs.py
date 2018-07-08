import pytest


@pytest.mark.bashcomp(
    pre_cmds=(
        "HOME=$PWD/cvs",
    ),
)
class TestCvs(object):

    @pytest.mark.complete("cvs ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("cvs -d ")
    def test_2(self, completion):
        assert [x for x in completion.list if ":pserver:" in x]

    @pytest.mark.complete("cvs diff foo/", cwd="cvs")
    def test_3(self, completion):
        assert completion.list == ["foo/bar"]
