import pytest


class Test(object):

    @pytest.mark.complete("cppcheck ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("cppcheck -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("cppcheck -DFOO=BAR ")
    def test_d_foo_bar(self, completion):
        assert completion.list

    @pytest.mark.complete("cppcheck -D ")
    def test_d(self, completion):
        assert not completion.list

    @pytest.mark.complete("cppcheck --enable=al")
    def test_enable1(self, completion):
        assert completion.list == ["--enable=all"]

    @pytest.mark.complete("cppcheck --enable=xx,styl")
    def test_enable2(self, completion):
        assert completion.list == ["--enable=xx,style"]

    @pytest.mark.complete("cppcheck --enable=xx,yy,styl")
    def test_enable3(self, completion):
        assert completion.list == ["--enable=xx,yy,style"]
