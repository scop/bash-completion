import pytest


class TestMr(object):

    @pytest.mark.complete("mr ")
    def test_1(self, completion):
        assert completion.list

    # man -h tests below: Some mr versions require man to be around in order
    # to provide useful output.

    @pytest.mark.complete("mr --", skipif="! man -h &>/dev/null")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("mr -c shared/default/foo.d/",
                          skipif="! man -h &>/dev/null")
    def test_3(self, completion):
        assert completion.list == ["shared/default/foo.d/foo"]

    @pytest.mark.xfail  # TODO: whitespace split issue
    @pytest.mark.complete("mr bootstrap shared/default/",
                          skipif="! man -h &>/dev/null")
    def test_4(self, completion):
        assert completion.list == ["bar", "bar bar.d/", "foo", "foo.d/"]

    @pytest.mark.xfail  # "clean" doesn't exist before mr 1.20141023
    @pytest.mark.complete("mr clean -", skipif="! man -h &>/dev/null")
    def test_5(self, completion):
        assert completion.list == ["-f"]

    @pytest.mark.complete("mr commit -", skipif="! man -h &>/dev/null")
    def test_6(self, completion):
        assert completion.list == ["-m"]

    @pytest.mark.complete("mr status ", skipif="! man -h &>/dev/null")
    def test_7(self, completion):
        assert not completion.list

    @pytest.mark.complete("mr run ", skipif="! man -h &>/dev/null")
    def test_8(self, completion):
        assert completion.list
