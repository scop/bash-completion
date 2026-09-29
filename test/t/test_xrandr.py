import pytest

ENV = dict(PATH="$PWD/xrandr:$PATH")
OUTPUTS = sorted("DP-0 DP-1 DP-2 DP-3 eDP-1-1 HDMI-0".split())


@pytest.mark.bashcomp(pre_cmds=("PATH=$PATH:$PWD/xrandr",))
class TestXrandr:
    @pytest.mark.complete("xrandr ", require_cmd=True)
    def test_no_args(self, completion):
        assert completion

    @pytest.mark.complete("xrandr -", require_cmd=True)
    def test_single_dash(self, completion):
        assert completion

    @pytest.mark.complete("xrandr --output ", env=ENV)
    def test_output(self, completion):
        assert completion == OUTPUTS

    @pytest.mark.complete("xrandr --output HDMI-0 --left-of ", env=ENV)
    def test_output_left_of(self, completion):
        assert completion == OUTPUTS

    @pytest.mark.complete("xrandr --output HDMI-0 --reflect ", env=ENV)
    def test_output_reflect(self, completion):
        assert completion == sorted("normal x y xy".split())

    @pytest.mark.complete("xrandr --reflect ", require_cmd=True)
    def test_output_reflect_nooutput(self, completion):
        assert not completion

    @pytest.mark.complete("xrandr --output HDMI-0 --rotate ", env=ENV)
    def test_output_rotate(self, completion):
        assert completion == sorted("normal inverted left right".split())

    @pytest.mark.complete("xrandr --rotate ", require_cmd=True)
    def test_output_rotate_nooutput(self, completion):
        assert not completion

    @pytest.mark.complete("xrandr --output HDMI-0 --filter ", env=ENV)
    def test_output_filter(self, completion):
        assert completion == sorted("bilinear nearest".split())

    @pytest.mark.complete("xrandr --output HDMI-0 --mode ", env=ENV)
    def test_output_mode(self, completion):
        assert completion == sorted(
            "1024x768 1280x1024 1280x800 1600x900 1920x1080 720x480 "
            "800x600 1152x864 1280x720 1440x900 1680x1050 640x480 720x576".split()
        )

    @pytest.mark.complete("xrandr --mode ", require_cmd=True)
    def test_output_mode_nooutput(self, completion):
        assert not completion

    @pytest.mark.complete("xrandr --addmode ", env=ENV)
    def test_addmode_first(self, completion):
        assert completion == OUTPUTS

    @pytest.mark.complete("xrandr --addmode HDMI-0 ", env=ENV)
    def test_addmode_second(self, completion):
        assert completion == sorted(
            "1024x576 1280x800 1440x900 320x200 432x243 640x350 700x450 800x450 928x696 "
            "1024x768 1280x960 1600x900 320x240 480x270 640x360 700x525 800x600 960x540 "
            "1024x768i 1368x768 1680x1050 360x200 512x288 640x400 720x400 832x624 960x600 "
            "1152x864 1400x1050 1920x1080 360x202 512x384 640x480 720x405 840x525 960x720 "
            "1280x1024 1400x900 320x175 400x300 512x384i 640x512 720x480 864x486 "
            "1280x720 1440x810 320x180 416x312 576x432 684x384 720x576 896x672".split()
        )

    @pytest.mark.complete("xrandr --delmode ", env=ENV)
    def test_delmode_first(self, completion):
        assert completion == OUTPUTS

    @pytest.mark.complete("xrandr --delmode HDMI-0 ", env=ENV)
    def test_delmode_second(self, completion):
        assert completion == sorted(
            "1024x768 1280x1024 1280x800 1600x900 1920x1080 720x480 "
            "800x600 1152x864 1280x720 1440x900 1680x1050 640x480 720x576".split()
        )

    @pytest.mark.complete("xrandr --dpi ", env=ENV)
    def test_dpi(self, completion):
        assert completion == OUTPUTS

    @pytest.mark.complete("xrandr -o ", env=ENV)
    def test_orientation(self, completion):
        assert completion == sorted(
            "normal inverted left right 0 1 2 3".split()
        )

    @pytest.mark.complete("xrandr --setmonitor testmonitor ", env=ENV)
    def test_setmonitor_second(self, completion):
        assert completion == sorted("auto".split())

    @pytest.mark.complete("xrandr --setmonitor testmonitor auto ", env=ENV)
    def test_setmonitor_third(self, completion):
        assert completion == OUTPUTS + ["none"]

    @pytest.mark.complete("xrandr --delmonitor ", env=ENV)
    def test_delmonitor(self, completion):
        assert completion == sorted("eDP-1-1 HDMI-0".split())

    @pytest.mark.complete("xrandr --setprovideroutputsource ", env=ENV)
    def test_setprovideroutputsource_first(self, completion):
        assert completion == sorted("modesetting".split())

    @pytest.mark.complete(
        "xrandr --setprovideroutputsource modesetting ", env=ENV
    )
    def test_setprovideroutputsource_second(self, completion):
        assert completion == sorted("0x0 modesetting NVIDIA-0".split())

    @pytest.mark.complete("xrandr --setprovideroffloadsink ", env=ENV)
    def test_setprovideroffloadsink_first(self, completion):
        assert completion == sorted("modesetting".split())

    @pytest.mark.complete(
        "xrandr --setprovideroffloadsink modesetting ", env=ENV
    )
    def test_setprovideroffloadsink_second(self, completion):
        assert completion == sorted("0x0 modesetting".split())
