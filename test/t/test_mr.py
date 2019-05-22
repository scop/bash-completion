import pytest


class TestMr:
    @pytest.mark.complete("mr ")
    def test_1(self, completion):
        assert completion

    # man -h tests below: Some mr versions require man to be around in order
    # to provide useful output.

    @pytest.mark.complete("mr --", xfail="! man -h &>/dev/null")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete(
        "mr -c shared/default/foo.d/", xfail="! man -h &>/dev/null"
    )
    def test_3(self, completion):
        assert completion == "shared/default/foo.d/foo"

    @pytest.mark.complete(
        "mr bootstrap shared/default/", xfail="! man -h &>/dev/null"
    )
    def test_4(self, completion):
        assert completion == ["bar", "bar bar.d/", "foo", "foo.d/"]

    @pytest.mark.xfail  # "clean" doesn't exist before mr 1.20141023
    @pytest.mark.complete("mr clean -", xfail="! man -h &>/dev/null")
    def test_5(self, completion):
        assert completion == "-f"

    @pytest.mark.complete("mr commit -", xfail="! man -h &>/dev/null")
    def test_6(self, completion):
        assert completion == "-m"

    @pytest.mark.complete("mr status ", xfail="! man -h &>/dev/null")
    def test_7(self, completion):
        assert not completion

    @pytest.mark.complete("mr run ", xfail="! man -h &>/dev/null")
    def test_8(self, completion):
        assert completion
