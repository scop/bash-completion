import pytest


class TestGroupadd:
    @pytest.mark.complete("groupadd ")
    def test_1(self, completion):
        assert not completion

    @pytest.mark.complete("groupadd -", require_cmd=True)
    def test_2(self, completion):
        assert completion
