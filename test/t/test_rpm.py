import pytest


class TestRpm:

    @pytest.mark.complete("rpm ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("rpm -q ",
                          skipif='test -z "$(rpm -qa 2>/dev/null)"')
    def test_2(self, completion):
        assert completion.list
