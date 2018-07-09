import getpass

import pytest

from conftest import assert_bash_exec


class TestChown(object):

    @pytest.mark.complete("chown ")
    def test_1(self, bash, completion):
        if getpass.getuser() == "root":
            users = sorted(assert_bash_exec(
                bash, "compgen -A user", want_output=True).split())
        else:
            users = [getpass.getuser()]
        assert completion.list == users

    @pytest.mark.xfail  # TODO: whitespace split issue
    @pytest.mark.complete("chown foo: shared/default/")
    def test_2(self, completion):
        assert completion.list == ["bar", "bar bar.d/", "foo", "foo.d/"]

    @pytest.mark.xfail  # TODO: whitespace split issue
    @pytest.mark.complete("chown :foo shared/default/")
    def test_3(self, completion):
        assert completion.list == ["bar", "bar bar.d/", "foo", "foo.d/"]
