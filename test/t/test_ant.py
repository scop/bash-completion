import pytest


@pytest.mark.bashcomp(ignore_env=r"^\+ANT_ARGS=")
class TestAnt:
    @pytest.mark.complete("ant -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ant ", cwd="ant")
    def test_2(self, completion):
        assert completion == "bashcomp clean init realclean".split()

    @pytest.mark.complete("ant -f build-with-import.xml ", cwd="ant")
    def test_3(self, completion):
        assert completion == "build-with-import imported-build".split()

    @pytest.mark.complete(
        "ant ", cwd="ant", env=dict(ANT_ARGS="'-f named-build.xml'")
    )
    def test_4(self, completion):
        assert completion == "named-build"

    @pytest.mark.complete("ant -l ")
    def test_5(self, completion):
        assert completion
