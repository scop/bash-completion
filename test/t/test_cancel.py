import pytest

from conftest import assert_bash_exec


class TestCancel:
    @pytest.fixture(scope="class")
    def added_job(self, request, bash):
        try:
            got = (
                assert_bash_exec(
                    bash, "lp -H hold shared/default/foo", want_output=True
                )
                .strip()
                .split()
            )
        except AssertionError:
            pytest.skip("Could not add test print job")
            return
        if len(got) > 3:
            request.addfinalizer(
                lambda: assert_bash_exec(bash, "cancel %s" % got[3])
            )

    @pytest.mark.complete("cancel ")
    def test_1(self, bash, completion, added_job):
        got = (
            assert_bash_exec(
                bash, "lpstat | awk '{print $1}'", want_output=True
            )
            .strip()
            .split()
        )
        assert completion == sorted(got)
