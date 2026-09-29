import pytest

from conftest import find_unique_completion_pair


@pytest.mark.bashcomp(cmd=None)
class TestUnitFindUniqueCompletionPair:
    def _test(self, inp: str, exp: str) -> None:
        res = find_unique_completion_pair(inp.split())
        if exp:
            part, cont = exp.split()
            assert res == (part, part + cont)
        else:
            assert not exp

    def test_1(self):
        self._test("a", "")

    def test_2(self):
        self._test("ab", "a b")

    def test_3(self):
        self._test("ab ab ab", "a b")

    def test_4(self):
        self._test("a ab abcd abc", "")

    def test_5(self):
        self._test("user1 user2", "")

    def test_6(self):
        self._test("root username1 username2", "ro ot")

    def test_7(self):
        self._test("root username21 username2", "ro ot")

    def test_8(self):
        self._test(
            "long_user_name lang_user_name long_usor_name", "lang_us er_name"
        )

    def test_9(self):
        self._test(
            "lang_user_name1 long_user_name lang_user_name long_usor_name",
            "long_use r_name",
        )

    def test_10(self):
        self._test("root username", "user name")

    def test_11(self):
        self._test("a aladin", "ala din")

    def test_12(self):
        self._test("ala aladin", "alad in")
