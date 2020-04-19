import pytest

from conftest import complete_at_point


@pytest.mark.bashcomp(ignore_env=r"^\+CDPATH=$")
class TestCd:
    @pytest.mark.complete("cd shared/default/")
    def test_1(self, completion):
        assert completion == ["bar bar.d/", "foo.d/"]

    @pytest.mark.complete("cd fo", env=dict(CDPATH="shared/default"))
    def test_2(self, completion):
        assert completion == "foo.d/"

    @pytest.mark.complete("cd fo")
    def test_3(self, completion):
        assert not completion

    @pytest.mark.complete(
        "cd ", cwd="shared/default/foo.d", env=dict(CDPATH="")
    )
    def test_4(self, completion):
        assert not completion  # No subdirs nor CDPATH

    def test_dir_at_point(self, bash):
        assert complete_at_point(
            bash=bash,
            cmd="cd shared/default/",
            trail="foo",
            expected=r"bar bar\.d/\s+foo\.d/",
        )
