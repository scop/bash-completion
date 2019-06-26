import pytest


@pytest.mark.bashcomp(cmd="gnome-mplayer", ignore_env=r"^[+-]XDG_DATA_DIRS=")
class TestGnomeMplayer:
    @pytest.mark.complete("gnome-mplayer ")
    def test_1(self, completion):
        assert completion

    # XDG_DATA_DIRS set to a dir with no schemas results in
    # "GLib-GIO-ERROR **: No GSettings schemas are installed on the system"
    # and a core dump on --help on Ubuntu 14.
    @pytest.mark.complete(
        "gnome-mplayer -", require_cmd=True, pre_cmds=("unset XDG_DATA_DIRS",)
    )
    def test_2(self, completion):
        assert completion
