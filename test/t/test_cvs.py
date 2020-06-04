import pytest


@pytest.mark.bashcomp(pre_cmds=("HOME=$PWD/cvs",))
class TestCvs:
    @pytest.mark.complete("cvs ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("cvs -d ")
    def test_2(self, completion):
        assert [x for x in completion if ":pserver:" in x]

    @pytest.mark.complete("cvs diff foo/", cwd="cvs")
    def test_3(self, completion):
        assert completion == "bar"

    @pytest.mark.complete("cvs -", require_cmd=True)
    def test_4(self, completion):
        assert completion
