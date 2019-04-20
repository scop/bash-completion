import pytest


class TestCurl:
    @pytest.mark.complete("curl --h")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("curl -o f", cwd="shared/default/foo.d")
    def test_2(self, completion):
        assert completion == "foo"

    @pytest.mark.complete("curl -LRo f", cwd="shared/default/foo.d")
    def test_3(self, completion):
        assert completion == "foo"

    @pytest.mark.complete("curl --o f")
    def test_4(self, completion):
        assert not completion
