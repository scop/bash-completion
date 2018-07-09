import pytest


class TestDpkg(object):

    @pytest.mark.complete("dpkg --c")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("dpkg -L ",
                          skipif='test -z "$(dpkg -l 2>/dev/null)"')
    def test_2(self, bash, completion):
        assert completion.list

    @pytest.mark.complete("dpkg -i ~")
    def test_3(self, completion):
        assert completion.list
