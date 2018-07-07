import pytest


class TestJavadoc(object):

    @pytest.mark.complete("javadoc ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.xfail  # TODO: whitespace split issue
    @pytest.mark.complete("javadoc -linkoffline shared/default/")
    def test_2(self, completion):
        assert completion.list == ["bar bar.d/", "foo.d/"]

    @pytest.mark.xfail  # TODO: whitespace split issue
    @pytest.mark.complete(
        "javadoc -nodeprecated -linkoffline foo shared/default/")
    def test_3(self, completion):
        assert completion.list == ["bar bar.d/", "foo.d/"]
