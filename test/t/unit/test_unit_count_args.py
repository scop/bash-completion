import pytest

from conftest import TestUnitBase, assert_bash_exec


@pytest.mark.bashcomp(
    cmd=None,
    ignore_env=r"^[+-](REPLY|cword|words|COMP_(WORDS|CWORD|LINE|POINT))=",
)
class TestUnitCountArgs(TestUnitBase):
    @pytest.fixture
    def functions(self, bash):
        assert_bash_exec(
            bash,
            '_comp__test_unit() { local -a words=(); local cword REPLY=""; _comp__reassemble_words "<>&" words cword; _comp_count_args "$@"; echo "$REPLY"; }',
        )

    def _test(self, *args, **kwargs):
        return self._test_unit("_comp__test_unit %s", *args, **kwargs)

    def test_1(self, bash):
        assert_bash_exec(
            bash,
            'COMP_LINE= COMP_POINT=0 COMP_WORDS=() COMP_CWORD=; _comp_count_args -n ""',
        )

    def test_2(self, bash, functions):
        """a b| should set args to 1"""
        output = self._test(bash, "(a b)", 1, "a b", 3)
        assert output == "1"

    def test_3(self, bash, functions):
        """a b|c should set args to 1"""
        output = self._test(bash, "(a bc)", 1, "a bc", 3)
        assert output == "1"

    def test_4(self, bash, functions):
        """a b c| should set args to 2"""
        output = self._test(bash, "(a b c)", 2, "a b c", 4)
        assert output == "2"

    def test_5(self, bash, functions):
        """a b| c should set args to 1"""
        output = self._test(bash, "(a b c)", 1, "a b c", 3)
        assert output == "1"

    def test_6(self, bash, functions):
        """a b -c| d should set args to 2"""
        output = self._test(bash, "(a b -c d)", 2, "a b -c d", 6)
        assert output == "2"

    def test_7(self, bash, functions):
        """a b -c d e| with -c arg excluded should set args to 2"""
        output = self._test(
            bash, "(a b -c d e)", 4, "a b -c d e", 10, arg='-a "@(-c|--foo)"'
        )
        assert output == "2"

    def test_8(self, bash, functions):
        """a -b -c d e| with -c arg excluded
        and -b included should set args to 1"""
        output = self._test(
            bash,
            "(a -b -c d e)",
            4,
            "a -b -c d e",
            11,
            arg='-a "@(-c|--foo)" -i "-[b]"',
        )
        assert output == "2"

    def test_9(self, bash, functions):
        """a -b -c d e| with -b included should set args to 3"""
        output = self._test(
            bash, "(a -b -c d e)", 4, "a -b -c d e", 11, arg='-i "-b"'
        )
        assert output == "3"

    def test_10_single_hyphen_1(self, bash):
        """- should be counted as an argument representing stdout/stdin"""
        output = self._test(bash, "(a -b - c -d e)", 5, "a -b - c -d e", 12)
        assert output == "3"

    def test_10_single_hyphen_2(self, bash):
        """- in an option argument should be skipped"""
        output = self._test(
            bash, "(a -b - c - e)", 5, "a -b - c - e", 11, arg='-a "-b"'
        )
        assert output == "3"

    def test_11_double_hyphen_1(self, bash):
        """all the words after -- should be counted"""
        output = self._test(
            bash, "(a -b -- -c -d e)", 5, "a -b -- -c -d e", 14
        )
        assert output == "3"

    def test_11_double_hyphen_2(self, bash):
        """all the words after -- should be counted"""
        output = self._test(bash, "(a b -- -c -d e)", 5, "a b -- -c -d e", 13)
        assert output == "4"

    def test_12_exclude_optarg_1(self, bash):
        """an option argument should be skipped even if it matches the argument pattern"""
        output = self._test(
            bash, "(a -o -x b c)", 4, "a -o -x b c", 10, arg='-a "-o" -i "-x"'
        )
        assert output == "2"

    def test_12_exclude_optarg_2(self, bash):
        """an option argument should be skipped even if it matches the argument pattern"""
        output = self._test(
            bash,
            "(a -o -x -x c)",
            4,
            "a -o -x -x c",
            11,
            arg='-a "-o" -i "-x"',
        )
        assert output == "2"

    def test_12_exclude_optarg_3(self, bash):
        """an option argument should be skipped even if it matches the argument pattern"""
        output = self._test(
            bash,
            "(a -o -x -y c)",
            4,
            "a -o -x -y c",
            11,
            arg='-a "-o" -i "-x"',
        )
        assert output == "1"

    def test_13_plus_option_optarg(self, bash):
        """When +o is specified to be an option taking an option argument, it should not be counted as an argument"""
        output = self._test(
            bash, "(a +o b c)", 3, "a +o b c", 7, arg='-a "+o"'
        )
        assert output == "1"

    def test_14_no_optarg_chain_1(self, bash):
        """an option argument should not take another option argument"""
        output = self._test(
            bash, "(a -o -o -o -o c)", 5, "a -o -o -o -o c", 14, arg='-a "-o"'
        )
        assert output == "1"

    def test_14_no_optarg_chain_2(self, bash):
        """an option argument should not take another option argument"""
        output = self._test(
            bash,
            "(a -o -o b -o -o c)",
            6,
            "a -o -o b -o -o c",
            16,
            arg='-a "-o"',
        )
        assert output == "2"

    def test_15_double_hyphen_optarg(self, bash):
        """-- should lose its meaning when it is an option argument"""
        output = self._test(
            bash, "(a -o -- -b -c d)", 5, "a -o -- -b -c d", 14, arg='-a "-o"'
        )
        assert output == "1"

    def test_16_empty_word(self, bash):
        """An empty word should not take an option argument"""
        output = self._test(bash, "(a '' x '' y d)", 5, "a  x  y d", 8)
        assert output == "5"
