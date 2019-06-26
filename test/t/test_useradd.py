import pytest


class TestUseradd:
    @pytest.mark.complete("useradd ")
    def test_1(self, completion):
        assert not completion

    @pytest.mark.complete("useradd -", require_cmd=True)
    def test_2(self, completion):
        assert completion
