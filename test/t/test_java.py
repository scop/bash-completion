import pytest


@pytest.mark.bashcomp(
    pre_cmds=("CLASSPATH=$PWD/java/a:$PWD/java/bashcomp.jar",)
)
class TestJava:
    @pytest.mark.complete("java -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("java ")
    def test_2(self, completion):
        assert completion == "b bashcomp.jarred c. toplevel".split()

    @pytest.mark.complete("java -classpath java/bashcomp.jar ")
    def test_3(self, completion):
        assert completion == "bashcomp.jarred toplevel".split()

    @pytest.mark.complete("java -cp java/bashcomp.jar:java/a/c ")
    def test_4(self, completion):
        assert completion == "bashcomp.jarred d toplevel".split()

    @pytest.mark.complete("java -cp '' ")
    def test_5(self, completion):
        assert not completion

    @pytest.mark.complete("java -jar java/")
    def test_6(self, completion):
        assert completion == "a/ bashcomp.jar bashcomp.war".split()
