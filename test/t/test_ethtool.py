import os
import pytest
import shlex

from conftest import assert_bash_exec


_MOCK_ETHTOOL_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "fixtures",
    "ethtool",
)

_CHANGE_SETTINGS = [
    "advertise",
    "autoneg",
    "duplex",
    "mdix",
    "msglvl",
    "port",
    "phyad",
    "speed",
    "wol",
    "xcvr",
]
_CHANGE_MSG_TYPES = [
    "drv",
    "hw",
    "ifdown",
    "ifup",
    "intr",
    "link",
    "pktdata",
    "probe",
    "rx_err",
    "rx_status",
    "timer",
    "tx_done",
    "tx_err",
    "tx_queued",
    "wol",
]
_FEATURES = [
    "gro",
    "gso",
    "rx",
    "rx-all",
    "rx-fcs",
    "rxhash",
    "rxvlan",
    "sg",
    "tso",
    "tx",
    "tx-checksum-ip-generic",
    "tx-tcp-mangleid-segmentation",
    "tx-tcp-segmentation",
    "tx-tcp6-segmentation",
    "tx-nocache-copy",
    "tx-scatter-gather",
    "txvlan",
    "ufo",
]
_FEC = [
    "BaseR",
    "RS",
    "auto",
    "off",
]
_FLOW_SETTINGS = [
    "action",
    "context",
    "loc",
    "queue",
    "vf",
]
_FLOW_AH4_SETTINGS = sorted(_FLOW_SETTINGS + [
    "dst-ip",
    "dst-mac",
    "spi",
    "src-ip",
    "tos",
    "user-def",
    "vlan",
    "vlan-etype",
])
_MOCK_CONTEXTS = [
    "1",
    "2",
]
_MOCK_ENV_SHOW_PRIV_ERR = {
    "MOCK_ETHTOOL_FAIL": "'No private flags defined'"
}
_MOCK_ENV_SHOW_NFC_ERR = {
    "MOCK_ETHTOOL_FAIL": "'Cannot get RX rings: Operation not supported'",
}
_MOCK_NFC_RULE_NUMBERS = [
    "2044",
    "2045",
    "2046",
    "2047",
]
_MOCK_PRIV_FLAGS = [
    "flow-director-atr",
    "vlan-stag-rx",
    "vlan-stag-filter",
    "vlan-stag-ethertype-802.1ad",
]
_MODULE_INFO = [
    "hex",
    "length",
    "offset",
    "raw",
]
_PAUSE = [
    "autoneg",
    "rx",
    "tx",
]
_REGISTER_DUMP = [
    "file",
    "hex",
    "raw",
]
_RESET = [
    "all",
    "ap",
    "ap-shared",
    "dedicated",
    "dma",
    "dma-shared",
    "filter",
    "filter-shared",
    "flags",
    "irq",
    "irq-shared",
    "mac",
    "mac-shared",
    "mgmt",
    "mgmt-shared",
    "offload",
    "offload-shared",
    "phy",
    "phy-shared",
    "ram",
    "ram-shared",
]
_RING = [
    "rx",
    "rx-jumbo",
    "rx-mini",
    "tx",
]
_RX_FLOW_HASH_OPTS = list("dfmnrstv")
_RX_FLOW_TYPES = [
    "ah4",
    "ah6",
    "esp4",
    "esp6",
    "ether",
    "ip4",
    "ip6",
    "sctp4",
    "sctp6",
    "tcp4",
    "tcp6",
    "udp4",
    "udp6",
]
_RX_FLOW_HASH_TYPES = list(_RX_FLOW_TYPES)
_RX_FLOW_HASH_TYPES.remove("ip4")
_RX_FLOW_HASH_TYPES.remove("ip6")
_RXFH = [
    "context",
    "default",
    "delete",
    "equal",
    "hfunc",
    "hkey",
    "weight",
]
_WOL_TYPES = list("abdfgmpsu")


@pytest.mark.bashcomp(
    ignore_env=r"^\+MOCK_ETHTOOL_FAIL=",
    pre_cmds=(
        "PATH=" + shlex.quote(_MOCK_ETHTOOL_DIR) + ":\"$PATH\"",
    ),
)
class TestEthtool:

    @pytest.fixture(scope="class")
    # Note: bash arg required for sequencing due to os.chdir in conftest.bash()
    def cwd_names(self, bash):
        """Directory entry names in the current directory."""
        return sorted(os.listdir(os.getcwd()))

    @pytest.fixture(scope="class")
    def firmware_filenames(self, bash):
        """Firmware files which would be found by request_firmware:
        https://www.kernel.org/doc/html/latest/driver-api/firmware/core.html"""
        firmware_paths = [
            "/lib/firmware/updates/",
            "/lib/firmware/",
        ]

        if hasattr(os, "uname"):
            release = os.uname().release
            firmware_paths.append("/lib/firmware/updates/" + release + "/")
            firmware_paths.append("/lib/firmware/" + release + "/")

        try:
            sys_fw_path_path = "/sys/module/firmware_class/parameters/path"
            with open(sys_fw_path_path) as sys_fw_path_file:
                sys_fw_path = sys_fw_path_file.read().rstrip("\n")
            if sys_fw_path:
                firmware_paths.append(sys_fw_path)
        except OSError:
            pass

        filename_set = set()
        for firmware_path in firmware_paths:
            for _dirpath, _dirnames, filenames in os.walk(firmware_path):
                filename_set.update(filenames)
                break

        return sorted(filename_set)

    @pytest.fixture(scope="class")
    def interfaces(self, bash):
        """Set of interfaces completed by `_available_interfaces`."""
        output = assert_bash_exec(bash,
                                  "("
                                  "cur='' _available_interfaces;"
                                  "printf '%s\\n' \"${COMPREPLY[@]}\" '';"
                                  ")",
                                  True)
        return sorted(output.split("\r\n")[1:-1])

    @pytest.fixture(scope="class")
    def ip_addresses4(self, bash):
        """Set of addresses completed by `_ip_addresses -4`."""
        output = assert_bash_exec(bash,
                                  "("
                                  "cur='' _ip_addresses -4;"
                                  "printf '%s\\n' \"${COMPREPLY[@]}\" '';"
                                  ")",
                                  True)
        return sorted(output.split("\r\n")[1:-1])

    @pytest.fixture(scope="class")
    def ip_addresses6(self, bash):
        """Set of addresses completed by `_ip_addresses -6`."""
        output = assert_bash_exec(bash,
                                  "("
                                  "cur='' _ip_addresses -6;"
                                  "printf '%s\\n' \"${COMPREPLY[@]}\" '';"
                                  ")",
                                  True)
        return sorted(output.split("\r\n")[1:-1])

    @pytest.fixture(scope="class")
    def mac_addresses(self, bash):
        """Set of addresses completed by `_mac_addresses`."""
        output = assert_bash_exec(bash,
                                  "("
                                  "cur='' _mac_addresses;"
                                  "printf '%s\\n' \"${COMPREPLY[@]}\" '';"
                                  ")",
                                  True)
        return sorted(output.split("\r\n")[1:-1])

    @pytest.mark.complete("ethtool ")
    def test_1(self, interfaces, completion):
        assert "--help" in completion
        assert "--version" in completion
        assert "--pause" in completion, "Includes custom long option"
        assert "--identify" in completion, "Includes devname long option"
        assert "-h" not in completion, "Does not include special short option"
        assert "-p" not in completion, "Does not include short options"
        assert all(i in completion for i in interfaces)

    @pytest.mark.complete("ethtool --help ")
    def test_2(self, completion):
        assert not completion

    @pytest.mark.complete("ethtool --identify ")
    def test_3(self, interfaces, completion):
        assert interfaces == completion

    @pytest.mark.complete("ethtool --identify eth0 ")
    def test_4(self, completion):
        assert not completion

    @pytest.mark.complete("ethtool -p ")
    def test_5(self, interfaces, completion):
        assert interfaces == completion

    @pytest.mark.complete("ethtool -p eth0 ")
    def test_6(self, completion):
        assert not completion

    @pytest.mark.complete("ethtool --change eth0 ")
    def test_7(self, completion):
        assert _CHANGE_SETTINGS == completion

    @pytest.mark.complete("ethtool --change eth0 port mii ")
    def test_8(self, completion):
        settings = list(_CHANGE_SETTINGS)
        settings.remove("port")
        assert settings == completion, "not repeated settings"

    @pytest.mark.complete("ethtool --change eth0 msglvl ")
    def test_9(self, completion):
        assert _CHANGE_MSG_TYPES == completion

    @pytest.mark.complete("ethtool --change eth0 msglvl wol ")
    def test_10(self, completion):
        assert ['off', 'on'] == completion, "wol msglvl on/off"

    @pytest.mark.complete("ethtool --change eth0 msglvl wol on ")
    def test_11(self, completion):
        settings = list(_CHANGE_SETTINGS)
        settings.remove("msglvl")
        msg_types = list(_CHANGE_MSG_TYPES)
        msg_types.remove("wol")
        assert sorted(settings + msg_types) == completion

    @pytest.mark.complete("ethtool --change eth0 wol ")
    def test_12(self, completion):
        assert _WOL_TYPES == completion, "wol option types"

    @pytest.mark.complete("ethtool --change eth0 wol p")
    def test_13(self, completion):
        wol_types = ["p" + wol_type
                     for wol_type in _WOL_TYPES if wol_type != "p"]
        assert wol_types == completion, "p + other wol option types"

    @pytest.mark.complete("ethtool --change eth0 wol " + "".join(_WOL_TYPES))
    def test_14(self, completion):
        assert not completion

    @pytest.mark.complete("ethtool --change-eeprom eth0 ")
    def test_15(self, completion):
        assert [
            "length",
            "magic",
            "offset",
            "value",
        ] == completion

    @pytest.mark.complete("ethtool --coalesce eth0 ")
    def test_16(self, completion):
        assert [
            "adaptive-rx",
            "adaptive-tx",
            "pkt-rate-high",
            "pkt-rate-low",
            "rx-frames",
            "rx-frames-high",
            "rx-frames-irq",
            "rx-frames-low",
            "rx-usecs",
            "rx-usecs-high",
            "rx-usecs-irq",
            "rx-usecs-low",
            "sample-interval",
            "stats-block-usecs",
            "tx-frames",
            "tx-frames-high",
            "tx-frames-irq",
            "tx-frames-low",
            "tx-usecs",
            "tx-usecs-high",
            "tx-usecs-irq",
            "tx-usecs-low",
        ] == completion

    @pytest.mark.complete("ethtool --config-nfc eth0 ")
    def test_17(self, completion):
        assert [
            "delete",
            "flow-type",
            "rx-flow-hash"
        ] == completion

    @pytest.mark.complete("ethtool --config-nfc eth0 rx-flow-hash ")
    def test_18(self, completion):
        assert _RX_FLOW_HASH_TYPES == completion

    @pytest.mark.complete("ethtool --config-nfc eth0 rx-flow-hash tcp4 ")
    def test_19(self, completion):
        assert _RX_FLOW_HASH_OPTS == completion

    @pytest.mark.complete("ethtool --config-nfc eth0 rx-flow-hash tcp4 m")
    def test_20(self, completion):
        hash_opts = ["m" + hash_opt
                     for hash_opt in _RX_FLOW_HASH_OPTS if hash_opt != "m"]
        assert hash_opts == completion, "m + other hash options"

    @pytest.mark.complete("ethtool --config-nfc eth0 rx-flow-hash tcp4 m ")
    def test_21(self, completion):
        assert ["context"] == completion

    @pytest.mark.complete("ethtool --config-nfc eth0 flow-type ")
    def test_22(self, completion):
        assert _RX_FLOW_TYPES == completion

    @pytest.mark.complete("ethtool --config-nfc eth0 flow-type ah4 ")
    def test_23(self, completion):
        assert _FLOW_AH4_SETTINGS == completion

    @pytest.mark.complete("ethtool --config-nfc eth0 flow-type ah4 action 1 ")
    def test_24(self, completion):
        settings = list(_FLOW_AH4_SETTINGS)
        settings.remove("action")
        settings.remove("queue")
        settings.remove("vf")
        assert settings == completion

    @pytest.mark.complete("ethtool --config-nfc eth0 flow-type ah4 dst-ip ")
    def test_25(self, ip_addresses4, completion):
        assert ip_addresses4 == completion

    @pytest.mark.complete("ethtool --config-nfc eth0 flow-type ah4 dst-mac ")
    def test_26(self, mac_addresses, completion):
        assert mac_addresses == completion

    @pytest.mark.complete(
        "ethtool --config-nfc eth0 flow-type ah4 dst-ip 1.1.1.1 ")
    def test_27(self, completion):
        settings = list(_FLOW_AH4_SETTINGS)
        settings.remove("dst-ip")
        settings.append("m")
        settings.append("dst-ip-mask")
        assert sorted(settings) == completion

    @pytest.mark.complete(
        "ethtool --config-nfc eth0 flow-type ah4 dst-ip 1.1.1.1 m ")
    def test_28(self, completion):
        assert not completion

    @pytest.mark.complete(
        "ethtool --config-nfc eth0 flow-type ah4 dst-ip 1.1.1.1 m 255.0.0.0 ")
    def test_29(self, completion):
        settings = list(_FLOW_AH4_SETTINGS)
        settings.remove("dst-ip")
        assert settings == completion

    @pytest.mark.complete("ethtool --config-nfc eth0 flow-type ah6 ")
    def test_30(self, completion):
        assert sorted(_FLOW_SETTINGS + [
            "dst-ip",
            "dst-mac",
            "spi",
            "src-ip",
            "tclass",
            "user-def",
            "vlan-etype",
            "vlan",
        ]) == completion

    @pytest.mark.complete("ethtool --config-nfc eth0 flow-type ah6 dst-ip ")
    def test_31(self, ip_addresses6, completion):
        assert ip_addresses6 == completion

    @pytest.mark.complete("ethtool --config-nfc eth0 flow-type ether ")
    def test_32(self, completion):
        assert sorted(_FLOW_SETTINGS + [
            "dst",
            "proto",
            "src",
            "user-def",
            "vlan-etype",
            "vlan",
        ]) == completion

    @pytest.mark.complete("ethtool --config-nfc eth0 flow-type ip4 ")
    def test_33(self, completion):
        assert sorted(_FLOW_SETTINGS + [
            "dst-ip",
            "dst-mac",
            "dst-port",
            "l4data",
            "l4proto",
            "spi",
            "src-ip",
            "src-port",
            "tos",
            "user-def",
            "vlan-etype",
            "vlan",
        ]) == completion

    @pytest.mark.complete("ethtool --config-nfc eth0 flow-type ip6 ")
    def test_34(self, completion):
        assert sorted(_FLOW_SETTINGS + [
            "dst-ip",
            "dst-mac",
            "dst-port",
            "l4data",
            "l4proto",
            "spi",
            "src-ip",
            "src-port",
            "tclass",
            "user-def",
            "vlan-etype",
            "vlan",
        ]) == completion

    @pytest.mark.complete("ethtool --config-nfc eth0 flow-type tcp4 ")
    def test_35(self, completion):
        assert sorted(_FLOW_SETTINGS + [
            "dst-ip",
            "dst-mac",
            "dst-port",
            "src-ip",
            "src-port",
            "tos",
            "user-def",
            "vlan-etype",
            "vlan",
        ]) == completion

    @pytest.mark.complete("ethtool --config-nfc eth0 flow-type tcp6 ")
    def test_36(self, completion):
        assert sorted(_FLOW_SETTINGS + [
            "dst-ip",
            "dst-mac",
            "dst-port",
            "src-ip",
            "src-port",
            "tclass",
            "user-def",
            "vlan-etype",
            "vlan",
        ]) == completion

    @pytest.mark.complete("ethtool --config-nfc eth0 flow-type tcp6 context ")
    def test_37(self, completion):
        assert _MOCK_CONTEXTS == completion

    @pytest.mark.complete("ethtool --config-nfc eth0 flow-type tcp6 context ",
                          env=_MOCK_ENV_SHOW_NFC_ERR)
    def test_38(self, completion):
        assert not completion

    @pytest.mark.complete("ethtool --eeprom-dump eth0 ")
    def test_39(self, completion):
        assert ["length", "offset", "raw"] == completion

    @pytest.mark.complete("ethtool --eeprom-dump eth0 raw ")
    def test_40(self, completion):
        assert ["off", "on"] == completion

    @pytest.mark.complete("ethtool --eeprom-dump eth0 raw on ")
    def test_41(self, completion):
        assert ["length", "offset"] == completion

    @pytest.mark.complete("ethtool --features eth0 ")
    def test_42(self, completion):
        assert _FEATURES == completion

    @pytest.mark.complete("ethtool --features eth0 gso ")
    def test_43(self, completion):
        assert ["off", "on"] == completion

    @pytest.mark.complete("ethtool --features eth0 tx-checksum-ip-generic ")
    def test_44(self, completion):
        assert ["off", "on"] == completion

    @pytest.mark.complete("ethtool --features eth0 gso on ")
    def test_45(self, completion):
        features = list(_FEATURES)
        features.remove("gso")
        assert features == completion

    @pytest.mark.complete("ethtool --flash eth0 ")
    def test_46(self, firmware_filenames, completion):
        assert firmware_filenames == completion

    @pytest.mark.complete("ethtool --get-dump eth0 ")
    def test_47(self, completion):
        assert ["data"] == completion

    @pytest.mark.complete("ethtool --get-dump eth0 data ")
    def test_48(self, cwd_names, completion):
        assert cwd_names == completion

    @pytest.mark.complete("ethtool --get-phy-tunable eth0 ")
    def test_49(self, completion):
        assert ["downshift"] == completion

    @pytest.mark.complete("ethtool --get-phy-tunable eth0 downshift ")
    def test_50(self, completion):
        assert not completion

    @pytest.mark.complete("ethtool --module-info eth0 ")
    def test_51(self, completion):
        assert _MODULE_INFO == completion

    @pytest.mark.complete("ethtool --module-info eth0 hex ")
    def test_52(self, completion):
        assert ["off", "on"] == completion

    @pytest.mark.complete("ethtool --module-info eth0 hex on ")
    def test_53(self, completion):
        module_info = list(_MODULE_INFO)
        module_info.remove("hex")
        assert module_info == completion

    @pytest.mark.complete("ethtool --pause eth0 ")
    def test_54(self, completion):
        assert _PAUSE == completion

    @pytest.mark.complete("ethtool --pause eth0 autoneg ")
    def test_55(self, completion):
        assert ["off", "on"] == completion

    @pytest.mark.complete("ethtool --pause eth0 autoneg on ")
    def test_56(self, completion):
        pause = _PAUSE
        pause.remove("autoneg")
        assert pause == completion

    @pytest.mark.complete("ethtool --register-dump eth0 ")
    def test_57(self, completion):
        assert _REGISTER_DUMP == completion

    @pytest.mark.complete("ethtool --register-dump eth0 hex ")
    def test_58(self, completion):
        assert ["off", "on"] == completion

    @pytest.mark.complete("ethtool --register-dump eth0 file ")
    def test_59(self, cwd_names, completion):
        assert cwd_names == completion

    @pytest.mark.complete("ethtool --register-dump eth0 file foo.bin ")
    def test_60(self, cwd_names, completion):
        register_dump = _REGISTER_DUMP
        register_dump.remove("file")
        assert register_dump == completion

    @pytest.mark.complete("ethtool --reset eth0 ")
    def test_61(self, completion):
        assert _RESET == completion

    @pytest.mark.complete("ethtool --reset eth0 all ")
    def test_62(self, completion):
        assert not completion

    @pytest.mark.complete("ethtool --reset eth0 dedicated ")
    def test_63(self, completion):
        shared = [reset for reset in _RESET if reset.endswith("-shared")]
        assert shared == completion

    @pytest.mark.complete("ethtool --reset eth0 ap ")
    def test_64(self, completion):
        reset = list(_RESET)
        reset.remove("all")
        reset.remove("ap")
        reset.remove("dedicated")
        reset.remove("flags")
        assert reset == completion

    @pytest.mark.complete("ethtool --reset eth0 ap-shared ")
    def test_65(self, completion):
        reset = list(_RESET)
        reset.remove("all")
        reset.remove("ap-shared")
        reset.remove("flags")
        assert reset == completion

    @pytest.mark.complete("ethtool --rxfh eth0 ")
    def test_66(self, completion):
        assert _RXFH == completion

    @pytest.mark.complete("ethtool --rxfh eth0 context ")
    def test_67(self, completion):
        assert _MOCK_CONTEXTS + ["new"] == completion

    @pytest.mark.complete("ethtool --rxfh eth0 context ",
                          env=_MOCK_ENV_SHOW_NFC_ERR)
    def test_68(self, completion):
        assert ["new"] == completion

    @pytest.mark.complete("ethtool --rxfh eth0 hfunc ")
    def test_69(self, completion):
        assert ["crc32", "toeplitz", "xor"] == completion

    @pytest.mark.complete("ethtool --rxfh eth0 hfunc ",
                          env=_MOCK_ENV_SHOW_NFC_ERR)
    def test_70(self, completion):
        assert not completion

    @pytest.mark.complete("ethtool --rxfh eth0 context 1 ")
    def test_71(self, completion):
        rxfh = list(_RXFH)
        rxfh.remove("context")
        rxfh.remove("default")
        assert rxfh == completion

    @pytest.mark.complete("ethtool --rxfh eth0 default ")
    def test_72(self, completion):
        rxfh = list(_RXFH)
        rxfh.remove("context")
        rxfh.remove("default")
        rxfh.remove("delete")
        rxfh.remove("equal")
        rxfh.remove("weight")
        assert rxfh == completion

    @pytest.mark.complete("ethtool --rxfh eth0 delete ")
    def test_73(self, completion):
        rxfh = list(_RXFH)
        rxfh.remove("default")
        rxfh.remove("delete")
        rxfh.remove("equal")
        rxfh.remove("hkey")
        rxfh.remove("weight")
        assert rxfh == completion

    @pytest.mark.complete("ethtool --rxfh eth0 equal 2 ")
    def test_74(self, completion):
        rxfh = list(_RXFH)
        rxfh.remove("default")
        rxfh.remove("delete")
        rxfh.remove("equal")
        rxfh.remove("weight")
        assert rxfh == completion

    @pytest.mark.complete("ethtool --rxfh eth0 hkey de:ad:be:ef ")
    def test_75(self, completion):
        rxfh = list(_RXFH)
        rxfh.remove("delete")
        rxfh.remove("hkey")
        assert rxfh == completion

    @pytest.mark.complete("ethtool --rxfh eth0 weight ")
    def test_76(self, completion):
        assert not completion

    @pytest.mark.complete("ethtool --rxfh eth0 weight 2 5 ")
    def test_77(self, completion):
        rxfh = list(_RXFH)
        rxfh.remove("default")
        rxfh.remove("delete")
        rxfh.remove("equal")
        rxfh.remove("weight")
        assert rxfh == completion

    @pytest.mark.complete("ethtool --set-channels eth0 ")
    def test_78(self, completion):
        assert [
            "combined",
            "other",
            "rx",
            "tx",
        ] == completion

    @pytest.mark.complete("ethtool --set-eee eth0 ")
    def test_79(self, completion):
        assert [
            "advertise",
            "eee",
            "tx-lpi",
            "tx-timer",
        ] == completion

    @pytest.mark.complete("ethtool --set-eee eth0 eee ")
    def test_80(self, completion):
        assert ["off", "on"] == completion

    @pytest.mark.complete("ethtool --set-fec eth0 ")
    def test_81(self, completion):
        assert ["encoding"] == completion

    @pytest.mark.complete("ethtool --set-fec eth0 encoding ")
    def test_82(self, completion):
        assert _FEC == completion

    @pytest.mark.complete("ethtool --set-fec eth0 encoding b")
    def test_83(self, completion):
        assert ["b\bBaseR"] == completion

    @pytest.mark.complete("ethtool --set-fec eth0 encoding baseR ")
    def test_84(self, completion):
        fec = list(_FEC)
        fec.remove("BaseR")
        assert fec == completion

    @pytest.mark.complete("ethtool --set-phy-tunable eth0 ")
    def test_85(self, completion):
        assert ["downshift"] == completion

    @pytest.mark.complete("ethtool --set-phy-tunable eth0 downshift ")
    def test_86(self, completion):
        assert ["off", "on"] == completion

    @pytest.mark.complete("ethtool --set-phy-tunable eth0 downshift on ")
    def test_87(self, completion):
        assert ["count"] == completion

    @pytest.mark.complete("ethtool --set-priv-flags eth0 ")
    def test_88(self, completion):
        assert _MOCK_PRIV_FLAGS == completion

    @pytest.mark.complete("ethtool --set-priv-flags eth0 ",
                          env=_MOCK_ENV_SHOW_PRIV_ERR)
    def test_89(self, completion):
        assert not completion

    @pytest.mark.complete("ethtool --set-priv-flags eth0 vlan-stag-rx ")
    def test_90(self, completion):
        assert ["off", "on"] == completion

    @pytest.mark.complete("ethtool --set-priv-flags eth0 vlan-stag-rx off ")
    def test_91(self, completion):
        priv_flags = list(_MOCK_PRIV_FLAGS)
        priv_flags.remove("vlan-stag-rx")
        assert priv_flags == completion

    @pytest.mark.complete("ethtool --set-ring eth0 ")
    def test_92(self, completion):
        assert _RING == completion

    @pytest.mark.complete("ethtool --set-ring eth0 rx 1 ")
    def test_93(self, completion):
        ring = list(_RING)
        ring.remove("rx")
        assert ring == completion

    @pytest.mark.complete("ethtool --show-nfc eth0 ")
    def test_94(self, completion):
        assert ["rule", "rx-flow-hash"] == completion

    @pytest.mark.complete("ethtool --show-nfc eth0 rule ")
    def test_95(self, completion):
        assert _MOCK_NFC_RULE_NUMBERS == completion

    @pytest.mark.complete("ethtool --show-nfc eth0 rule ",
                          env=_MOCK_ENV_SHOW_NFC_ERR)
    def test_96(self, completion):
        assert not completion

    @pytest.mark.complete("ethtool --show-nfc eth0 rx-flow-hash ")
    def test_97(self, completion):
        assert _RX_FLOW_HASH_TYPES == completion

    @pytest.mark.complete("ethtool --show-nfc eth0 rx-flow-hash ah4 ")
    def test_98(self, completion):
        assert ["context"] == completion

    @pytest.mark.complete("ethtool --show-nfc eth0 rx-flow-hash ah4 context ")
    def test_99(self, completion):
        assert _MOCK_CONTEXTS == completion

    @pytest.mark.complete("ethtool --show-nfc eth0 rx-flow-hash ah4 context ",
                          env=_MOCK_ENV_SHOW_NFC_ERR)
    def test_100(self, completion):
        assert not completion

    @pytest.mark.complete("ethtool --show-rxfh eth0 ")
    def test_101(self, completion):
        assert ["context"] == completion

    @pytest.mark.complete("ethtool --show-rxfh eth0 context ")
    def test_102(self, completion):
        assert _MOCK_CONTEXTS == completion

    @pytest.mark.complete("ethtool --show-rxfh eth0 context ",
                          env=_MOCK_ENV_SHOW_NFC_ERR)
    def test_103(self, completion):
        assert not completion

    @pytest.mark.complete("ethtool --test eth0 ")
    def test_104(self, completion):
        assert ["external_lb", "offline", "online"] == completion

    @pytest.mark.complete("ethtool --test eth0 offline ")
    def test_105(self, completion):
        assert not completion
