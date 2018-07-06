import pytest


class Test(object):

    @pytest.mark.complete("declare -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("declare +")
    def test_plus(self, completion):
        assert completion.list

    @pytest.mark.complete("declare -p BASH_ARG")
    def test_p(self, completion):
        assert completion.list == "BASH_ARGC BASH_ARGV".split()

    @pytest.mark.complete("declare -f _parse_")
    def test_f(self, completion):
        assert "_parse_help" in completion.list
