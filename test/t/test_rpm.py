import pytest


class TestRpm:
    @pytest.mark.complete("rpm ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("rpm -q ", skipif='test ! "$(rpm -qa 2>/dev/null)"')
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("rpm -", require_cmd=True)
    def test_3(self, completion):
        assert completion
