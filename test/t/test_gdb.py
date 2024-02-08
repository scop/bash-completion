import pytest


class TestGdb:
    @pytest.mark.complete("gdb - ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("gdb foo ", cwd="gdb")
    def test_2(self, completion):
        assert completion == sorted(
            "core core.12345 "
            "core.weston.1000.deadbeef.5308.1555362132000000".split()
        )

    @pytest.mark.complete("gdb aw")
    def test_3(self, completion):
        """Check that the completion can generate command names"""
        assert completion == ["k"] or "awk" in completion

    @pytest.mark.complete("gdb built")
    def test_4(self, completion):
        """Check that the completion does not generate builtin names"""
        assert not (completion == ["in"] or "builtin" in completion)
