import pytest


class TestGrep:
    @pytest.mark.complete("grep --", require_longopt=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("grep --no-complete-dir f", cwd="shared/default")
    def test_2(self, completion):
        """
        Test --no-*dir isn't restricted to dirs only.

        Not really a grep option, but tests _comp_complete_longopt.
        """
        assert completion == "foo foo.d/".split()

    @pytest.mark.complete("grep TZ ", cwd="shared/default")
    def test_no_variable_assignment_confusion(self, completion):
        """
        Test TZ doesn't trigger known variable value assignment completion.

        Not really a grep specific, but good to test somewhere.
        Refs https://github.com/scop/bash-completion/issues/457
        """
        assert "foo" in completion
