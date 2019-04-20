import pytest


class TestSbcl:
    @pytest.mark.xfail  # TODO: whitespace split issue
    @pytest.mark.complete("sbcl shared/default/")
    def test_1(self, completion):
        assert completion == ["bar", "bar bar.d/", "foo", "foo foo.d/"]
