import pytest


@pytest.mark.bashcomp(ignore_env=r"^\+ANT_ARGS=")
class TestAnt(object):

    @pytest.mark.complete("ant -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("ant ", cwd="ant")
    def test_2(self, completion):
        assert completion.list == "bashcomp clean init realclean".split()

    @pytest.mark.complete("ant -f build-with-import.xml ", cwd="ant")
    def test_3(self, completion):
        assert completion.list == "build-with-import imported-build".split()

    @pytest.mark.complete("ant ", cwd="ant",
                          env=dict(ANT_ARGS="'-f named-build.xml'"))
    def test_4(self, completion):
        assert completion.list == ["named-build"]
