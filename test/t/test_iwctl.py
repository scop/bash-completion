import contextlib
import textwrap

import pytest

from conftest import assert_bash_exec

COMMANDS = [
    "adapter",
    "ad-hoc",
    "ap",
    "device",
    "known-networks",
    "wsc",
    "station",
    "dpp",
    "pkex",
    "debug",
]


class TestIwctl:
    @pytest.mark.complete("iwctl ")
    def test_commands(self, completion):
        assert set(completion) == set(COMMANDS)

    @pytest.mark.parametrize(
        "option",
        [
            "--username",
            "--password",
            "--passphrase",
            "--dont-ask",
            "--help",
        ],
    )
    @pytest.mark.complete("iwctl -")
    def test_options(self, completion, option):
        assert option in completion

    @pytest.mark.complete("iwctl --username ")
    def test_option_username(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl --username=stat ")
    def test_option_username_with_equal(self, completion):
        assert set(completion) == set(COMMANDS)

    @pytest.mark.complete("iwctl --password ")
    def test_option_password(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl --password=stat ")
    def test_option_password_with_equal(self, completion):
        assert set(completion) == set(COMMANDS)

    @pytest.mark.complete("iwctl --passphrase ")
    def test_option_passphrase(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl --passphrase=stat ")
    def test_option_passphrase_with_equal(self, completion):
        assert set(completion) == set(COMMANDS)

    @pytest.mark.parametrize("command", COMMANDS)
    @pytest.mark.complete(
        "iwctl --username USR --password PS --passphrase PP --dont-ask --help "
    )
    def test_commands_with_options(self, completion, command):
        assert command in completion

    # adapter

    @pytest.mark.complete("iwctl adapter ", require_cmd=True)
    def test_adapter(self, completion):
        assert "list" in completion

    @pytest.mark.complete(
        "iwctl adapter ",
        require_cmd=True,
        skipif="iwctl adapter list | command grep -q 'No devices in'",
    )
    def test_adapter_with_interfaces(self, completion):
        assert "list" in completion
        assert len(completion) >= 2

    @pytest.mark.complete("iwctl adapter list ")
    def test_adapter_list(self, completion):
        assert not completion

    @pytest.mark.parametrize("subcmd", ["set-property", "show"])
    @pytest.mark.complete("iwctl adapter phy0 ")
    def test_adapter_commands(self, completion, subcmd):
        assert subcmd in completion

    # ad-hoc

    @pytest.mark.complete("iwctl ad-hoc ", require_cmd=True)
    def test_ad_hoc(self, completion):
        assert "list" in completion

    @pytest.mark.complete(
        "iwctl ad-hoc ",
        require_cmd=True,
        skipif="iwctl ad-hoc list | command grep -q 'No devices in'",
    )
    def test_ad_hoc_with_interfaces(self, completion):
        assert "list" in completion
        assert len(completion) >= 2

    @pytest.mark.complete("iwctl ad-hoc list ")
    def test_ad_hoc_list(self, completion):
        assert not completion

    @pytest.mark.parametrize("subcmd", ["start", "start_open", "stop"])
    @pytest.mark.complete(
        "iwctl ad-hoc phy0 ",
    )
    def test_ad_hoc_commands(self, completion, subcmd):
        assert subcmd in completion

    @pytest.mark.complete("iwctl adapter wlan0 set-property prop ")
    def test_adapter_set_property_prop(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl adapter wlan0 set-property prop val ")
    def test_adapter_set_property_prop_val(self, completion):
        assert not completion

    # ap

    @pytest.mark.complete("iwctl ap ", require_cmd=True)
    def test_ap(self, completion):
        assert "list" in completion

    @pytest.mark.complete(
        "iwctl ap ",
        require_cmd=True,
        skipif="iwctl ap list | command grep -q 'No devices in'",
    )
    def test_ap_with_interfaces(self, completion):
        assert "list" in completion
        assert len(completion) >= 2

    @pytest.mark.complete("iwctl ap list ")
    def test_ap_list(self, completion):
        assert not completion

    @pytest.mark.parametrize(
        "subcmd",
        [
            "start",
            "start-profile",
            "stop",
            "show",
            "scan",
            "get-networks",
        ],
    )
    @pytest.mark.complete("iwctl ap wlan0 ")
    def test_ap_commands(self, completion, subcmd):
        assert subcmd in completion

    @pytest.mark.complete("iwctl ap wlan0 start ")
    def test_ap_start(self, completion):
        assert not completion

    # device

    @pytest.mark.complete("iwctl device ", require_cmd=True)
    def test_device(self, completion):
        assert "list" in completion

    @pytest.mark.complete(
        "iwctl device ",
        require_cmd=True,
        skipif="iwctl device list | command grep -q 'No devices in'",
    )
    def test_device_with_interfaces(self, completion):
        assert "list" in completion
        assert len(completion) >= 2

    @pytest.mark.complete("iwctl device list ")
    def test_device_list(self, completion):
        assert not completion

    @pytest.mark.parametrize("subcmd", ["set-property", "show"])
    @pytest.mark.complete("iwctl device wlan0 ")
    def test_device_commands(self, completion, subcmd):
        assert subcmd in completion

    @pytest.mark.complete("iwctl device wlan0 show ")
    def test_device_show(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl device wlan0 set-property ")
    def test_device_set_property(self, completion):
        # No suggestions for properties in implementation.
        assert not completion

    @pytest.mark.complete("iwctl device wlan0 set-property prop ")
    def test_device_set_property_prop(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl device wlan0 set-property prop val ")
    def test_device_set_property_prop_val(self, completion):
        assert not completion

    # known-networks

    @pytest.mark.complete("iwctl known-networks ", require_cmd=True)
    def test_known_networks(self, completion):
        assert "list" in completion

    @pytest.mark.complete(
        "iwctl known-networks ",
        require_cmd=True,
        skipif="iwctl known-networks list | command grep -q 'No network with'",
    )
    def test_known_networks_with_interfaces(self, completion):
        assert "list" in completion
        assert len(completion) >= 2

    @pytest.mark.complete("iwctl known-networks list ")
    def test_known_networks_list(self, completion):
        assert not completion

    @pytest.mark.parametrize("subcmd", ["forget", "show", "set-property"])
    @pytest.mark.complete("iwctl known-networks WifiNetwork ")
    def test_known_networks_commands(self, completion, subcmd):
        assert subcmd in completion

    @pytest.mark.complete("iwctl known-networks WifiNetwork forget ")
    def test_known_networks_forget(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl known-networks WifiNetwork show ")
    def test_known_networks_show(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl known-networks WifiNetwork set-property ")
    def test_known_networks_set_property(self, completion):
        # No suggestions for properties in implementation.
        assert not completion

    @pytest.mark.complete("iwctl known-networks wlan0 set-property prop ")
    def test_known_networks_set_property_prop(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl known-networks wlan0 set-property prop val ")
    def test_known_networks_set_property_prop_val(self, completion):
        assert not completion

    # wsc

    @pytest.mark.complete("iwctl wsc ", require_cmd=True)
    def test_wsc(self, completion):
        assert "list" in completion

    @pytest.mark.complete(
        "iwctl wsc ",
        require_cmd=True,
        skipif="iwctl wsc list | command grep -q 'No devices in'",
    )
    def test_wsc_with_interfaces(self, completion):
        assert "list" in completion
        assert len(completion) >= 2

    @pytest.mark.complete("iwctl wsc list ")
    def test_wsc_list(self, completion):
        assert not completion

    @pytest.mark.parametrize(
        "subcmd",
        [
            "push-button",
            "start-user-pin",
            "start-pin",
            "cancel",
        ],
    )
    @pytest.mark.complete("iwctl wsc wlan0 ")
    def test_wsc_commands(self, completion, subcmd):
        assert subcmd in completion

    @pytest.mark.complete("iwctl wsc wlan0 push-button ")
    def test_wsc_push_button(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl wsc wlan0 start-user-pin ")
    def test_wsc_start_user_pin(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl wsc wlan0 start-user-pin PIN ")
    def test_wsc_start_user_pin_with_value(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl wsc wlan0 start-pin ")
    def test_wsc_start_pin(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl wsc wlan0 cancel ")
    def test_wsc_cancel(self, completion):
        assert not completion

    # station

    @pytest.mark.complete("iwctl station ", require_cmd=True)
    def test_station(self, completion):
        assert "list" in completion

    @pytest.mark.complete(
        "iwctl station ",
        require_cmd=True,
        skipif="iwctl station list | command grep -q 'No devices in'",
    )
    def test_station_with_interfaces(self, completion):
        assert "list" in completion
        assert len(completion) >= 2

    @pytest.mark.parametrize(
        "subcmd",
        [
            "connect",
            "connect-hidden",
            "disconnect",
            "get-networks",
            "get-hidden-access-points",
            "scan",
            "show",
            "get-bsses",
        ],
    )
    @pytest.mark.complete("iwctl station wlan0 ")
    def test_station_commands(self, completion, subcmd):
        assert subcmd in completion

    @pytest.mark.complete("iwctl station list ")
    def test_station_list(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl station wlan0 connect WifiNetwork ")
    def test_station_connect_network(self, completion):
        # No security completion
        assert not completion

    @pytest.mark.complete("iwctl station wlan0 connect WifiNetwork psk ")
    def test_station_connect_network_security(self, completion):
        assert not completion

    @pytest.mark.complete(
        'iwctl station wlan0 connect-hidden "01:23:45:67:89:ab" '
    )
    def test_station_connect_hidden_network(self, completion):
        assert not completion

    @pytest.mark.parametrize("option", ["rssi-dbms", "rssi-bars"])
    @pytest.mark.complete("iwctl station wlan0 get-networks ")
    def test_station_get_networks(self, completion, option):
        assert option in completion

    @pytest.mark.parametrize("option", ["rssi-dbms", "rssi-bars"])
    @pytest.mark.complete("iwctl station wlan0 get-hidden-access-points ")
    def test_station_get_hidden_access_points(self, completion, option):
        assert option in completion

    @pytest.mark.complete("iwctl station wlan0 disconnect ")
    def test_station_disconnect(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl station wlan0 get-networks rssi-dbms ")
    def test_station_get_networks_rssi_dbms(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl station wlan0 get-networks rssi-bars ")
    def test_station_get_networks_rssi_bars(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl station wlan0 scan ")
    def test_station_scan(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl station wlan0 show ")
    def test_station_show(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl station get-bsses WifiNetwork ")
    def test_station_get_bsses_network(self, completion):
        # No security completion
        assert not completion

    @pytest.mark.complete("iwctl station get-bsses WifiNetwork psk ")
    def test_station_get_bsses_network_security(self, completion):
        assert not completion

    # dpp

    @pytest.mark.complete("iwctl dpp ", require_cmd=True)
    def test_dpp(self, completion):
        assert "list" in completion

    @pytest.mark.complete(
        "iwctl dpp ",
        require_cmd=True,
        skipif="iwctl dpp list | command grep -q 'No devices in'",
    )
    def test_dpp_with_interfaces(self, completion):
        assert "list" in completion
        assert len(completion) >= 2

    @pytest.mark.complete("iwctl dpp list ")
    def test_dpp_list(self, completion):
        assert not completion

    @pytest.mark.parametrize(
        "subcmd",
        [
            "start-enrollee",
            "start-configurator",
            "stop",
            "show",
        ],
    )
    @pytest.mark.complete("iwctl dpp wlan0 ")
    def test_dpp_commands(self, completion, subcmd):
        assert subcmd in completion

    @pytest.mark.complete("iwctl dpp wlan0 start-enrollee ")
    def test_dpp_start_enrollee(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl dpp wlan0 start-configurator ")
    def test_dpp_start_configurator(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl dpp wlan0 stop ")
    def test_dpp_stop(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl dpp wlan0 show ")
    def test_dpp_show(self, completion):
        assert not completion

    # pkex

    @pytest.mark.complete("iwctl pkex ", require_cmd=True)
    def test_pkex(self, completion):
        assert "list" in completion

    @pytest.mark.complete(
        "iwctl pkex ",
        require_cmd=True,
        skipif="iwctl pkex list | command grep -q 'No devices in'",
    )
    def test_pkex_with_interfaces(self, completion):
        assert "list" in completion
        assert len(completion) >= 2

    @pytest.mark.complete("iwctl pkex list ")
    def test_pkex_list(self, completion):
        assert not completion

    @pytest.mark.parametrize(
        "subcmd",
        [
            "stop",
            "show",
            "enroll",
            "configure",
        ],
    )
    @pytest.mark.complete("iwctl pkex wlan0 ")
    def test_pkex_commands(self, completion, subcmd):
        assert subcmd in completion

    @pytest.mark.parametrize("option", ["key"])
    @pytest.mark.complete("iwctl pkex wlan0 enroll ")
    def test_pkex_enroll(self, completion, option):
        assert option in completion

    @pytest.mark.parametrize("option", ["key"])
    @pytest.mark.complete("iwctl pkex wlan0 configure ")
    def test_pkex_configure(self, completion, option):
        assert option in completion

    @pytest.mark.complete("iwctl pkex wlan0 stop ")
    def test_pkex_stop(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl pkex wlan0 show ")
    def test_pkex_show(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl pkex wlan0 enroll key ")
    def test_pkex_enroll_key(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl pkex wlan0 configure key ")
    def test_pkex_configure_key(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl pkex wlan0 enroll key KEY ")
    def test_pkex_enroll_key_with_key(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl pkex wlan0 configure key KEY ")
    def test_pkex_configure_key_with_key(self, completion):
        assert not completion

    # debug

    @pytest.mark.complete(
        "iwctl debug ",
        require_cmd=True,
        skipif="iwctl station list | command grep -q 'No devices in'",
    )
    def test_debug_with_interfaces(self, completion):
        assert completion

    @pytest.mark.parametrize(
        "subcmd",
        [
            "connect",
            "roam",
            "get-networks",
            "autoconnect",
        ],
    )
    @pytest.mark.complete("iwctl debug wlan0 ")
    def test_debug_commands(self, completion, subcmd):
        assert subcmd in completion

    @pytest.mark.complete("iwctl debug wlan0 connect ")
    def test_debug_connect(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl debug wlan0 connect BSSID ")
    def test_debug_connect_bssid(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl debug wlan0 roam ")
    def test_debug_roam(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl debug wlan0 roam BSSID ")
    def test_debug_roam_bssid(self, completion):
        assert not completion

    @pytest.mark.parametrize("option", ["on", "off"])
    @pytest.mark.complete("iwctl debug wlan0 autoconnect ")
    def test_debug_autoconnect(self, completion, option):
        assert option in completion

    @pytest.mark.complete("iwctl debug wlan0 autoconnect on ")
    def test_debug_autoconnect_on(self, completion):
        assert not completion

    @pytest.mark.complete("iwctl debug wlan0 autoconnect off ")
    def test_debug_autoconnect_off(self, completion):
        assert not completion


@contextlib.contextmanager
def bash_prepended_path(bash, path):
    """Update 'bash' environment by prepending PATH.

    `assert_bash_exec` seems to fail with too long commands, so rely on bash
    variable modification to not repeat the whole PATH in command.

    It should be done on a function scope level.
    """
    try:
        assert_bash_exec(bash, f'export PATH="{path}:$PATH"')
        yield
    finally:
        assert_bash_exec(bash, 'PATH="${PATH#*:}"')


ADAPTER_LIST = """\
                                    Adapters\x1b[1;90m                                   \x1b[0m
\x1b[90m--------------------------------------------------------------------------------
\x1b[0m\x1b[1;90m  Name      Powered   Vendor                Model
\x1b[0m\x1b[90m--------------------------------------------------------------------------------
\x1b[0m  phy0      on        Qualcomm              ABCDE123 Wireless
                      Name, Inc             Network Adapter

"""

AD_HOC_LIST_NONE = """\
                             Devices in Ad-Hoc Mode\x1b[1;90m                            \x1b[0m
\x1b[90m--------------------------------------------------------------------------------
\x1b[0m\x1b[1;90m  Name                  Started
\x1b[0m\x1b[90m--------------------------------------------------------------------------------
\x1b[0mNo devices in Ad-Hoc mode available.

"""

AP_LIST_NONE = """\
                          Devices in Access Point Mode\x1b[1;90m                         \x1b[0m
\x1b[90m--------------------------------------------------------------------------------
\x1b[0m\x1b[1;90m  Name                  Started
\x1b[0m\x1b[90m--------------------------------------------------------------------------------
\x1b[0mNo devices in access point mode available.

"""

DEVICES_LIST = """\
                                    Devices\x1b[1;90m                                    \x1b[0m
\x1b[90m--------------------------------------------------------------------------------
\x1b[0m\x1b[1;90m  Name                  Address               Powered     Adapter     Mode
\x1b[0m\x1b[90m--------------------------------------------------------------------------------
\x1b[0m  wlan0                 00:11:22:33:44:55     on          phy0        station

"""

KNOWN_NETWORKS_LIST = """\
                                 Known Networks\x1b[1;90m                                \x1b[0m
\x1b[90m--------------------------------------------------------------------------------
\x1b[0m\x1b[1;90m  Name                              Security     Hidden     Last connected
\x1b[0m\x1b[90m--------------------------------------------------------------------------------
\x1b[0m  MyWifiNetwork                     psk                     Mar 29, 11:49 PM
  WifiBox 1234                      open                    Mar  8,  6:09 PM
  Really  long  Wifi Network  Name  psk                     Mar 22,  6:51 AM
  HomeNetwork                       8021x                   Nov 20, 11:13 PM

"""

WSC_LIST = """\
                              WSC-capable Devices\x1b[1;90m                              \x1b[0m
\x1b[90m--------------------------------------------------------------------------------
\x1b[0m\x1b[1;90m  Name
\x1b[0m\x1b[90m--------------------------------------------------------------------------------
\x1b[0m  wlan0

"""

STATION_LIST = """\
                            Devices in Station Mode\x1b[1;90m                            \x1b[0m
\x1b[90m--------------------------------------------------------------------------------
\x1b[0m\x1b[1;90m  Name                  State            Scanning
\x1b[0m\x1b[90m--------------------------------------------------------------------------------
\x1b[0m  wlan0                 connected        scanning

"""

STATION_GET_NETWORKS = """\
                               Available networks\x1b[1;90m                              \x1b[0m
\x1b[90m--------------------------------------------------------------------------------
\x1b[0m\x1b[1;90m      Network name                      Security            Signal
\x1b[0m\x1b[90m--------------------------------------------------------------------------------
\x1b[0m  \x1b[1;90m> \x1b[0m  MyWifiNetwork                     psk                 ****
      WifiBox 1234                      open                ***\x1b[1;90m*\x1b[0m
      Really  long  Wifi Network  Name  psk                 *\x1b[1;90m***\x1b[0m
      HomeNetwork                       8021x               *\x1b[1;90m***\x1b[0m

"""

STATION_GET_HIDDEN_ACCESS_POINTS = """\
                              Available hidden APs\x1b[1;90m                             \x1b[0m
\x1b[90m--------------------------------------------------------------------------------
\x1b[0m\x1b[1;90m  Address               Security    Signal
\x1b[0m\x1b[90m--------------------------------------------------------------------------------
\x1b[0m  01:23:45:67:89:ab     8021x       ****
  00:98:76:54:32:10     8021x       ****
  00:11:22:33:44:55     8021x       *\x1b[1;90m***\x1b[0m

"""

DPP_LIST = """\
                              DPP-capable Devices\x1b[1;90m                              \x1b[0m
\x1b[90m--------------------------------------------------------------------------------
\x1b[0m\x1b[1;90m  Name
\x1b[0m\x1b[90m--------------------------------------------------------------------------------
\x1b[0m  wlan0

"""

PKEX_LIST = """\
                            DPP-PKEX-capable Devices\x1b[1;90m                           \x1b[0m
\x1b[90m--------------------------------------------------------------------------------
\x1b[0m\x1b[1;90m  Name
\x1b[0m\x1b[90m--------------------------------------------------------------------------------
\x1b[0m  wlan0

"""


class TestIwctlMockedOutput:
    """Test Iwctl networks/environment dependant completions.

    Uses mocked output to check the internal parsing implementation.
    If 'iwctl' output would change this would not detect it, but tests should be
    updated/added.

    It relies on an 'iwctl' binary that will output content of 'iwctl_output'
    file in the same directory.

    On a per-test basis, the output file is created and path of 'iwctl' binary
    added to the 'bash' environment.
    """

    IWCTL_MOCK = textwrap.dedent(
        """\
        #!/bin/sh
        cat "$(dirname $0)/iwctl_output"
        printf "%s\\n" "$@" >> "$(dirname $0)/iwctl_cmd"
        """
    )

    def iwctl_create_binfile(self, iwctl_bindir):
        iwctl = iwctl_bindir / "iwctl"
        iwctl.write_text(self.IWCTL_MOCK, encoding="utf-8")
        iwctl.chmod(0o777)

    @pytest.fixture(scope="function")
    def iwctl_mock(self, tmp_path, bash, iwctl_output, iwctl_cmd):
        bindir = tmp_path / "iwctl_bindir"
        bindir.mkdir()

        self.iwctl_create_binfile(bindir)
        (bindir / "iwctl_output").write_text(iwctl_output, encoding="utf-8")

        with bash_prepended_path(bash, bindir):
            yield

        command = (bindir / "iwctl_cmd").read_text(encoding="utf-8").split()
        assert command == iwctl_cmd

    @pytest.mark.usefixtures("iwctl_mock")
    @pytest.mark.parametrize(
        "iwctl_output,iwctl_cmd",
        [(ADAPTER_LIST, ["adapter", "list"])],
        ids=["multi_line"],
    )
    @pytest.mark.complete("iwctl adapter ")
    def test_adapter(self, completion):
        assert set(completion) == set(("list", "phy0"))

    @pytest.mark.usefixtures("iwctl_mock")
    @pytest.mark.parametrize(
        "iwctl_output,iwctl_cmd",
        [(AD_HOC_LIST_NONE, ["ad-hoc", "list"])],
        ids=["no_devices"],
    )
    @pytest.mark.complete("iwctl ad-hoc ")
    def test_ad_hoc_none(self, completion):
        assert set(completion) == set(("list",))

    @pytest.mark.usefixtures("iwctl_mock")
    @pytest.mark.parametrize(
        "iwctl_output,iwctl_cmd",
        [(AP_LIST_NONE, ["ap", "list"])],
        ids=["no_devices"],
    )
    @pytest.mark.complete("iwctl ap ")
    def test_ap_none(self, completion):
        assert set(completion) == set(("list",))

    @pytest.mark.usefixtures("iwctl_mock")
    @pytest.mark.parametrize(
        "iwctl_output,iwctl_cmd",
        [(DEVICES_LIST, ["device", "list"])],
        ids=["devices"],
    )
    @pytest.mark.complete("iwctl device ")
    def test_device(self, completion):
        assert set(completion) == set(("list", "wlan0"))

    @pytest.mark.usefixtures("iwctl_mock")
    @pytest.mark.parametrize(
        "iwctl_output,iwctl_cmd",
        [(KNOWN_NETWORKS_LIST, ["known-networks", "list"])],
        ids=["devices"],
    )
    @pytest.mark.complete("iwctl known-networks ")
    def test_known_networks(self, completion):
        assert set(completion) == set(
            (
                "list",
                '"WifiBox 1234"',
                "MyWifiNetwork",
                "HomeNetwork",
                '"Really  long  Wifi Network  Name"',
            )
        )

    @pytest.mark.usefixtures("iwctl_mock")
    @pytest.mark.parametrize(
        "iwctl_output,iwctl_cmd",
        [(WSC_LIST, ["wsc", "list"])],
        ids=["devices"],
    )
    @pytest.mark.complete("iwctl wsc ")
    def test_wsc(self, completion):
        assert set(completion) == set(("list", "wlan0"))

    @pytest.mark.usefixtures("iwctl_mock")
    @pytest.mark.parametrize(
        "iwctl_output,iwctl_cmd",
        [(STATION_LIST, ["station", "list"])],
        ids=["devices"],
    )
    @pytest.mark.complete("iwctl station ")
    def test_station(self, completion):
        assert set(completion) == set(("list", "wlan0"))

    @pytest.mark.usefixtures("iwctl_mock")
    @pytest.mark.parametrize(
        "iwctl_output,iwctl_cmd",
        [(STATION_GET_NETWORKS, ["station", "wlan0", "get-networks"])],
        ids=["all_networks"],
    )
    @pytest.mark.complete("iwctl station wlan0 connect ")
    def test_station_connect(self, completion):
        assert set(completion) == set(
            (
                '"WifiBox 1234"',
                "MyWifiNetwork",
                "HomeNetwork",
                '"Really  long  Wifi Network  Name"',
            )
        )

    @pytest.mark.usefixtures("iwctl_mock")
    @pytest.mark.parametrize(
        "iwctl_output,iwctl_cmd",
        [
            (
                STATION_GET_HIDDEN_ACCESS_POINTS,
                ["station", "wlan0", "get-hidden-access-points"],
            )
        ],
        ids=["hidden_networks"],
    )
    @pytest.mark.complete("iwctl station wlan0 connect-hidden ")
    def test_station_connect_hidden(self, completion):
        assert '"01:23:45:67:89:ab"' in completion
        assert '"00:98:76:54:32:10"' in completion
        assert '"00:11:22:33:44:55"' in completion

    @pytest.mark.usefixtures("iwctl_mock")
    @pytest.mark.parametrize(
        "iwctl_output,iwctl_cmd",
        [(DPP_LIST, ["dpp", "list"])],
        ids=["devices"],
    )
    @pytest.mark.complete("iwctl dpp ")
    def test_dpp(self, completion):
        assert set(completion) == set(("list", "wlan0"))

    @pytest.mark.usefixtures("iwctl_mock")
    @pytest.mark.parametrize(
        "iwctl_output,iwctl_cmd",
        [(PKEX_LIST, ["pkex", "list"])],
        ids=["devices"],
    )
    @pytest.mark.complete("iwctl pkex ")
    def test_pkex(self, completion):
        assert set(completion) == set(("list", "wlan0"))

    @pytest.mark.usefixtures("iwctl_mock")
    @pytest.mark.parametrize(
        "iwctl_output,iwctl_cmd",
        [(STATION_LIST, ["station", "list"])],
        ids=["devices"],
    )
    @pytest.mark.complete("iwctl debug ")
    def test_debug(self, completion):
        assert set(completion) == set(("wlan0",))
