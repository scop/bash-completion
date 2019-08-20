import pytest

from conftest import is_bash_type


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
