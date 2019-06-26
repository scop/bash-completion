import pytest


class TestDpkg:
    @pytest.mark.complete("dpkg --c", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("dpkg -L ", xfail='test -z "$(dpkg -l 2>/dev/null)"')
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("dpkg -i ~")
    def test_3(self, completion):
        assert completion
