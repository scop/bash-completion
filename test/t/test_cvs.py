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

    @pytest.mark.complete("cvs update -AdP foo/", cwd="cvs")
    def test_5(self, completion):
        assert completion == "bar"

    @pytest.mark.complete("cvs log -v foo/", cwd="cvs")
    def test_6(self, completion):
        assert completion == "bar"

    @pytest.mark.complete("cvs diff foo/", cwd="cvs")
    def test_7(self, completion):
        assert completion == "bar"

    @pytest.mark.complete("cvs status -v foo/", cwd="cvs")
    def test_8(self, completion):
        assert completion == "bar"

    @pytest.mark.complete("cvs status foo/", cwd="cvs")
    def test_9(self, completion):
        assert completion == "bar"
