import pytest

from conftest import assert_complete


class TestSet:
    @pytest.mark.parametrize("dash", ["", "-", "--"])
    def test_basic(self, bash, dash):
        completion = assert_complete(bash, f"set {dash} ")
        assert completion

    @pytest.mark.parametrize("prefix", ["-", "+"])
    def test_options(self, bash, prefix):
        completion = assert_complete(bash, f"set {prefix}")
        assert f"{prefix}o" in completion
        assert "+-" not in completion

    @pytest.mark.parametrize("prefix", ["-", "+"])
    def test_o_args(self, bash, prefix):
        completion = assert_complete(bash, f"set {prefix}o ")
        assert any(x.startswith("no") for x in completion)

    @pytest.mark.parametrize("dash,prefix", [["-", "--"], ["-", "+"]])
    def test_options_after_dash_or_dashdash(self, bash, dash, prefix):
        completion = assert_complete(bash, f"set {dash} {prefix}")
        assert not completion
