import pytest

from conftest import assert_complete, bash_env_saved


@pytest.mark.bashcomp(ignore_env=r"^\+CDPATH=$")
class TestCd:
    @pytest.mark.complete("cd shared/default/")
    def test_1(self, completion):
        assert completion == ["bar bar.d/", "foo.d/"]

    @pytest.mark.complete("cd foo", env=dict(CDPATH="shared/default"))
    def test_2(self, completion):
        assert completion == ".d/"

    @pytest.mark.complete("cd foo")
    def test_3(self, completion):
        assert not completion

    @pytest.mark.complete(
        "cd ", cwd="shared/default/foo.d", env=dict(CDPATH="")
    )
    def test_4(self, completion):
        assert not completion  # No subdirs nor CDPATH

    @pytest.mark.complete("cd shared/default/", trail="foo")
    def test_dir_at_point(self, completion):
        assert completion == ["bar bar.d/", "foo.d/"]

    @pytest.mark.complete("cd -")
    def test_options(self, completion):
        assert completion

    def test_cdable_vars(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("cdable_vars", True)
            bash_env.write_variable("foo1", "shared")
            bash_env.write_variable("foo2", "shared/default")
            bash_env.write_variable("foo3", "nonexistent")
            bash_env.write_variable("foo4", "nonexistent")
            bash_env.write_variable("foo5", "shared/default/foo")
            bash_env.write_variable("foo6", "shared/default/bar")
            completion = assert_complete(bash, "cd f")
            assert completion == ["foo1", "foo2"]
