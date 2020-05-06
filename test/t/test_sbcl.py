import pytest


class TestSbcl:
    @pytest.mark.complete("sbcl shared/default/")
    def test_1(self, completion):
        assert completion == ["bar", "bar bar.d/", "foo", "foo.d/"]
