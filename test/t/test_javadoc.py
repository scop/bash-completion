import pytest


class TestJavadoc:
    @pytest.mark.complete("javadoc ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("javadoc -linkoffline shared/default/")
    def test_2(self, completion):
        assert completion == ["bar bar.d/", "foo.d/"]

    @pytest.mark.complete(
        "javadoc -nodeprecated -linkoffline foo shared/default/"
    )
    def test_3(self, completion):
        assert completion == ["bar bar.d/", "foo.d/"]
