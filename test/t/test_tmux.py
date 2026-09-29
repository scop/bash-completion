# SPDX-License-Identifier: GPL-2.0-or-later OR ISC

import pytest

from conftest import assert_complete


@pytest.mark.bashcomp(cmd="tmux", require_cmd=True)
class TestTmux:
    # Tests for _comp_cmd_tmux__parse_usage(). Most of this function is tested
    # elsewhere since almost everything else depends on it. These are just
    # tests for corner cases that aren't tested elsewhere.

    @pytest.mark.complete("tmux wait-for -")
    def test_parse_usage_alternative_options(self, completion):
        """Tests the [-a|-b|-c] form of option parsing."""
        assert "-L" in completion
        assert "-S" in completion
        assert "-U" in completion
        assert "-|" not in completion
        assert "--" not in completion

    # Tests for _comp_cmd_tmux__value()

    @pytest.mark.complete("tmux new-")
    def test_value_command(self, completion):
        assert "new-session" in completion
        assert "new-window" in completion

    @pytest.mark.complete("tmux new-window -c ", cwd="shared/default")
    def test_value_directory(self, completion):
        assert completion == ["bar bar.d/", "foo.d/"]

    @pytest.mark.complete("tmux -f ", cwd="shared/default")
    def test_value_file(self, completion):
        assert completion == ["bar", "bar bar.d/", "foo", "foo.d/"]

    # Tests for _comp_cmd_tmux__options()

    @pytest.mark.complete("tmux -f /dev/null ")
    def test_option_with_value(self, completion):
        assert "new-session" in completion

    @pytest.mark.complete("tmux -Nvf /dev/null ")
    def test_option_multiple_with_value(self, completion):
        assert "new-session" in completion

    @pytest.mark.complete("tmux -f -f ")
    def test_option_with_value_with_dash(self, completion):
        """Tests that the second -f is a filename not an option."""
        assert "new-session" in completion

    @pytest.mark.complete("tmux -- ")
    def test_option_explicit_end(self, completion):
        assert "new-session" in completion

    @pytest.mark.complete("tmux -f/dev/null ")
    def test_option_with_attached_value(self, completion):
        assert "new-session" in completion

    @pytest.mark.complete("tmux -Nvf/dev/null ")
    def test_option_multiple_with_attached_value(self, completion):
        assert "new-session" in completion

    @pytest.mark.complete("tmux -v ")
    def test_option_without_value(self, completion):
        assert "new-session" in completion

    @pytest.mark.complete("tmux -Nv ")
    def test_option_multiple_without_value(self, completion):
        assert "new-session" in completion

    # Tests for _comp_cmd_tmux__nested_arguments()

    @pytest.mark.complete(
        "tmux bind-key C-a new-window -c ",
        cwd="shared/default",
    )
    def test_nested_arguments_tmux_subcommand(self, completion):
        assert completion == ["bar bar.d/", "foo.d/"]

    # Tests for _comp_cmd_tmux__subcommand()

    @pytest.mark.complete("tmux this-is-not-a-real-subcommand-i-hope ")
    def test_subcommand_unknown(self, completion):
        assert not completion

    @pytest.mark.complete("tmux new-window -c ", cwd="shared/default")
    def test_subcommand_option_value(self, completion):
        assert completion == ["bar bar.d/", "foo.d/"]

    @pytest.mark.complete("tmux new-window -")
    def test_subcommand_options(self, completion):
        assert "-a" in completion  # takes no value
        assert "-c" in completion  # takes a value

    @pytest.mark.complete("tmux display-menu ")
    def test_subcommand_no_positional_arg_completion(self, completion):
        assert not completion

    @pytest.mark.complete("tmux source-file abc def ", cwd="shared/default")
    def test_subcommand_repetition(self, completion):
        assert completion == ["bar", "bar bar.d/", "foo", "foo.d/"]

    @pytest.mark.complete("tmux source-file ", cwd="shared/default")
    def test_subcommand_positional_arg_1(self, completion):
        assert completion == ["bar", "bar bar.d/", "foo", "foo.d/"]

    @pytest.mark.complete("tmux bind-key C-a ")
    def test_subcommand_positional_arg_2(self, completion):
        assert "new-session" in completion

    @pytest.mark.complete("tmux start-server ")
    def test_subcommand_no_positional_args(self, completion):
        assert not completion

    @pytest.mark.complete("tmux choose-tree abc def ghi ")
    def test_subcommand_too_many_positional_args(self, completion):
        assert not completion

    # Tests for _comp_cmd_tmux()

    @pytest.mark.complete("tmux -f ", cwd="shared/default")
    def test_tmux_option_value(self, completion):
        assert completion == ["bar", "bar bar.d/", "foo", "foo.d/"]

    @pytest.mark.complete("tmux -")
    def test_tmux_options(self, completion):
        assert "-f" in completion  # takes a value
        assert "-v" in completion  # takes no value

    @pytest.mark.parametrize(
        "other_commands",
        [
            r"foo ';'",
            r"foo';'",
            r"foo '\\;'",  # backslash escaped in tmux
            r"foo'\\;'",
        ],
    )
    def test_tmux_multiple_commands(self, bash, other_commands):
        completion = assert_complete(
            bash,
            f"tmux {other_commands} bind-key C-a ",
        )
        assert "new-session" in completion

    @pytest.mark.parametrize(
        "semicolon_arg",
        [
            r"foo '\;'",  # semicolon escaped in tmux
            r"foo'\;'",
            r"foo '\\\;'",  # escaped backslash then escaped semicolon in tmux
            r"foo'\\\;'",
            r"foo';'bar",  # semicolon doesn't need to be escaped in the middle
        ],
    )
    def test_tmux_semicolon_within_subcommand(self, bash, semicolon_arg):
        completion = assert_complete(
            bash,
            # Note that the next arg is a file, not a subcommand. If it were a
            # subcommand, it wouldn't be possible to tell if the completion was
            # parsing semicolon_arg correctly.
            f"tmux source-file {semicolon_arg} ",
            cwd="shared/default",
        )
        assert completion == ["bar", "bar bar.d/", "foo", "foo.d/"]

    @pytest.mark.complete("tmux ")
    def test_tmux_subcommand(self, completion):
        assert "new-session" in completion
