import pytest

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

    @pytest.mark.complete("iwctl debug wlan0 roam ")
    def test_debug_roam(self, completion):
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
