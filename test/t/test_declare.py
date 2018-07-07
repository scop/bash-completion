import pytest


class TestDeclare(object):

    @pytest.mark.complete("declare -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("declare +")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("declare -p BASH_ARG")
    def test_3(self, completion):
        assert completion.list == "BASH_ARGC BASH_ARGV".split()

    @pytest.mark.complete("declare -f _parse_")
    def test_4(self, completion):
        assert "_parse_help" in completion.list
