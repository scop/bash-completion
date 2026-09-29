import pytest


class TestPython:
    @pytest.mark.complete("python ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("python -", require_cmd=True)
    def test_2(self, completion):
        assert len(completion) > 1

    @pytest.mark.complete("python -c ")
    def test_3(self, completion):
        assert not completion

    @pytest.mark.complete("python shared/default/")
    def test_4(self, completion):
        assert completion == ["bar bar.d/", "foo.d/"]

    @pytest.mark.complete("python -c foo shared/default/")
    def test_5(self, completion):
        assert completion == ["bar", "bar bar.d/", "foo", "foo.d/"]

    @pytest.mark.complete("python -c foo -")
    def test_6(self, completion):
        assert not completion

    @pytest.mark.complete("python -m foo -")
    def test_7(self, completion):
        assert not completion

    @pytest.mark.complete("python -m sy", require_cmd=True)
    def test_8(self, completion):
        assert completion

    @pytest.mark.complete("python -m json.", require_cmd=True)
    def test_9(self, completion):
        assert "json.tool" in completion

    @pytest.mark.complete(
        "python -b",
        require_cmd=True,
        skipif="! python -h | command grep -qwF -- -bb",
    )
    def test_bb(self, completion):
        assert "-bb" in completion

    @pytest.mark.complete("python foo ", cwd="python")
    def test_script_arg(self, completion):
        assert "bar.txt" in completion

    @pytest.mark.complete("python -- foo ", cwd="python")
    def test_script_arg_with_double_hyphen(self, completion):
        assert "bar.txt" in completion

    @pytest.mark.complete("python -m foo bar -p ", cwd="python")
    def test_module_arg(self, completion):
        assert "bar.txt" in completion

    @pytest.mark.complete("python foo bar -p ", cwd="python")
    def test_script_arg_after_option(self, completion):
        assert "bar.txt" in completion

    @pytest.mark.complete("python -- foo bar -p ", cwd="python")
    def test_script_arg_after_option_with_double_hyphen(self, completion):
        assert "bar.txt" in completion

    @pytest.mark.complete("python -m foo bar -p ", cwd="python")
    def test_module_arg_after_option(self, completion):
        assert "bar.txt" in completion

    @pytest.mark.complete("python -mfoo bar -p ", cwd="python")
    def test_module_arg_after_option_with_connected_m_arg(self, completion):
        assert "bar.txt" in completion

    @pytest.mark.complete("python -- ", cwd="python")
    def test_script_name(self, completion):
        assert "bar.txt" not in completion

    @pytest.mark.complete("python -W -mfoo ", cwd="python")
    def test_script_name_with_fake_m_arg(self, completion):
        """In this case, -mfoo looks like an option to specify the module, but
        it should not be treated as the module name because it is an option
        argument to -W."""
        assert "bar.txt" not in completion
