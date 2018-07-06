import pytest


class Test(object):

    @pytest.mark.complete("curl --h")
    def test_h(self, completion):
        assert completion.list

    @pytest.mark.complete("curl -o f", cwd="shared/default/foo.d")
    def test_o_f(self, completion):
        assert completion.list == ["foo"]

    @pytest.mark.complete("curl -LRo f", cwd="shared/default/foo.d")
    def test_lro_f(self, completion):
        assert completion.list == ["foo"]

    @pytest.mark.complete("curl --o f")
    def test__o_f(self, completion):
        assert not completion.list
