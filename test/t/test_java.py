import pytest

from conftest import assert_bash_exec, bash_env_saved, is_bash_type


@pytest.mark.bashcomp(
    pre_cmds=("CLASSPATH=$PWD/java/a:$PWD/java/bashcomp.jar",)
)
class TestJava:
    @pytest.fixture(scope="class")
    def can_list_jar(self, bash):
        return (
            is_bash_type(bash, "zipinfo")
            or is_bash_type(bash, "unzip")
            or is_bash_type(bash, "jar")
        )

    @pytest.mark.complete("java -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("java ")
    def test_2(self, completion, can_list_jar):
        if can_list_jar:
            assert completion == "b bashcomp.jarred c. toplevel".split()
        else:
            assert completion == "b c.".split()

    @pytest.mark.complete("java -classpath java/bashcomp.jar ")
    def test_3(self, completion, can_list_jar):
        if can_list_jar:
            assert completion == "bashcomp.jarred toplevel".split()
        else:
            assert not completion

    @pytest.mark.complete("java -cp java/bashcomp.jar:java/a/c ")
    def test_4(self, completion, can_list_jar):
        if can_list_jar:
            assert completion == "bashcomp.jarred d toplevel".split()
        else:
            assert completion == ["d"]

    @pytest.mark.complete("java -cp '' ")
    def test_5(self, completion):
        assert not completion

    @pytest.mark.complete("java -jar java/")
    def test_6(self, completion):
        assert completion == "a/ bashcomp.jar bashcomp.war".split()

    @pytest.mark.complete("javadoc -sourcepath java/a:java/a/c ")
    def test_sourcepath_1(self, completion):
        """sourcepath should be split by `:`"""
        assert completion == "c"

    @pytest.mark.complete("javadoc -sourcepath java/?:java/x ")
    def test_sourcepath_2(self, completion):
        """pathname expansion should not happen after splitting the argument by
        `:`"""
        assert not completion

    @pytest.mark.complete("javadoc -sourcepath java/a ")
    def test_packages_1(self, completion):
        assert completion == "c"

    @pytest.mark.complete("javadoc -sourcepath java/a x")
    def test_packages_2(self, completion):
        assert not completion

    @pytest.mark.complete(
        "javadoc -sourcepath java/a x", shopt=dict(failglob=True)
    )
    def test_packages_3(self, completion):
        assert not completion

    @pytest.mark.complete("javadoc -sourcepath java/a ", env=dict(IFS="a"))
    def test_packages_4(self, completion):
        assert completion == "c"

    def test_packages_5(self, bash):
        """_comp_cmd_java__packages should not modify the outerscope `cur`"""
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable("cur", "a.b.c")
            assert_bash_exec(
                bash,
                "_comp_test_f() { local cword=3 words=(javadoc -sourcepath java/a a.b.c); COMPREPLY+=(); _comp_cmd_java__packages; }; _comp_test_f",
            )

    @pytest.mark.complete("javadoc -sourcepath java a.")
    def test_packages_6(self, completion):
        """A period in package names should not be converted to slash."""
        assert completion == "c"
