import pytest


class TestRpmbuild:
    @pytest.mark.complete("rpmbuild -", require_cmd=True)
    def test_1(self, completion):
        assert completion
