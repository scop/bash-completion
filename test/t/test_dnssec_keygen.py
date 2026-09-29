import pytest


@pytest.mark.bashcomp(
    cmd="dnssec-keygen", pre_cmds=("PATH=$PATH:$PWD/dnssec-keygen",)
)
class TestDnssecKeygen:
    @pytest.mark.complete("dnssec-keygen -")
    def test_1(self, completion):
        assert completion
        assert not any(x.endswith(":") for x in completion)

    @pytest.mark.complete("dnssec-keygen -a ")
    def test_2(self, completion):
        assert completion
        assert any(x in completion for x in ("HMAC-MD5", "RSASHA1", "ED25519"))
        assert "|" not in completion
        assert not any(x.startswith("-") for x in completion)

    @pytest.mark.complete("dnssec-keygen -n ")
    def test_3(self, completion):
        assert completion
        assert "HOST" in completion
        assert "|" not in completion
        assert not any(x.startswith("-") for x in completion)

    @pytest.mark.complete("dnssec-keygen -f ")
    def test_4(self, completion):
        assert completion
        assert "|" not in completion
        assert not any(x.startswith("-") for x in completion)

    @pytest.mark.complete("dnssec-keygen ")
    def test_5(self, completion):
        assert not completion

    @pytest.mark.complete(
        "dnssec-keygen -a ", env=dict(PATH="$PWD/dnssec-keygen:$PATH")
    )
    def test_6(self, completion):
        assert completion == sorted(
            "RSA RSAMD5 DSA RSASHA1 NSEC3RSASHA1 NSEC3DSA "
            "RSASHA256 RSASHA512 ECCGOST "
            "ECDSAP256SHA256 ECDSAP384SHA384 "
            "ED25519 ED448 DH "
            "HMAC-MD5 HMAC-SHA1 HMAC-SHA224 HMAC-SHA256 "
            "HMAC-SHA384 HMAC-SHA512".split()
        )

    @pytest.mark.complete(
        "dnssec-keygen -n ", env=dict(PATH="$PWD/dnssec-keygen:$PATH")
    )
    def test_7(self, completion):
        assert completion == sorted("ZONE HOST ENTITY USER OTHER".split())

    @pytest.mark.complete(
        "dnssec-keygen -f ", env=dict(PATH="$PWD/dnssec-keygen:$PATH")
    )
    def test_8(self, completion):
        assert completion == sorted("KSK REVOKE".split())

    @pytest.mark.complete(
        "dnssec-keygen -T ", env=dict(PATH="$PWD/dnssec-keygen:$PATH")
    )
    def test_9(self, completion):
        assert completion == sorted("DNSKEY KEY".split())

    @pytest.mark.complete(
        "dnssec-keygen -t ", env=dict(PATH="$PWD/dnssec-keygen:$PATH")
    )
    def test_10(self, completion):
        assert completion == sorted(
            "AUTHCONF NOAUTHCONF NOAUTH NOCONF".split()
        )

    @pytest.mark.complete(
        "dnssec-keygen -m ", env=dict(PATH="$PWD/dnssec-keygen:$PATH")
    )
    def test_11(self, completion):
        assert completion == sorted("usage trace record size mctx".split())
