import pytest


@pytest.mark.bashcomp(ignore_env=r"^\+CDPATH=$")
class TestCd(object):

    @pytest.mark.xfail  # TODO: whitespace split issue
    @pytest.mark.complete("cd shared/default/")
    def test_1(self, completion):
        assert completion.list == ["bar bar.d/" "foo.d/"]

    @pytest.mark.complete("cd fo", env=dict(CDPATH="shared/default"))
    def test_2(self, completion):
        assert completion.list == ["foo.d/"]

    @pytest.mark.complete("cd fo")
    def test_3(self, completion):
        assert not completion.list

    @pytest.mark.complete("cd ",
                          cwd="shared/default/foo.d",
                          env=dict(CDPATH=""))
    def test_4(self, completion):
        assert not completion.list  # No subdirs nor CDPATH
