import pytest


@pytest.mark.bashcomp(cmd="ssh-keygen")
class TestSshKeygen:
    @pytest.mark.complete("ssh-keygen -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete(
        "ssh-keygen -", require_cmd=True, shopt=dict(failglob=True)
    )
    def test_1_failglob(self, completion):
        assert completion

    @pytest.mark.complete(
        "ssh-keygen -", require_cmd=True, shopt=dict(nullglob=True)
    )
    def test_1_nullglob(self, completion):
        assert completion

    @pytest.mark.complete("ssh-keygen -s foo_key ssh-copy-id/.ssh/")
    def test_filedir_pub_at_end_of_s(self, completion):
        assert completion
        assert all(x.endswith(".pub") for x in completion)

    @pytest.mark.complete("ssh-keygen -s foo_key -n foo,")
    def test_usernames_for_n(self, completion):
        assert completion
        # TODO check that these are usernames

    @pytest.mark.complete("ssh-keygen -s foo_key -h -n foo,")
    def test_host_for_h_n(self, completion):
        assert completion
        # TODO check that these are hostnames

    @pytest.mark.complete("ssh-keygen -Y foo -n ")
    def test_n_with_Y(self, completion):
        assert not completion

    @pytest.mark.complete("ssh-keygen -r ")
    def test_r_without_Y(self, completion):
        assert not completion

    @pytest.mark.complete("ssh-keygen -Y foo -r ")
    def test_r_with_Y(self, completion):
        assert "ssh/" in completion

    @pytest.mark.complete("ssh-keygen -t ecdsa -b ")
    def test_ecdsa_b(self, completion):
        assert completion

    @pytest.mark.complete("ssh-keygen -t ecdsa-sk -b ")
    def test_ecdsa_sk_b(self, completion):
        assert not completion

    @pytest.mark.complete("ssh-keygen -O ")
    def test_O(self, completion):
        assert completion
        assert any(x.endswith("=") for x in completion)

    @pytest.mark.complete("ssh-keygen -O force-command=bas")
    def test_O_force_command(self, completion):
        assert completion
        assert not completion.startswith("force-command=")

    @pytest.mark.complete("ssh-keygen -O unknown=")
    def test_O_unknown(self, completion):
        assert not completion

    @pytest.mark.complete("ssh-keygen -O application=")
    def test_O_application(self, completion):
        assert completion == "ssh:"

    @pytest.mark.complete("ssh-keygen -O application=s")
    def test_O_application_s(self, completion):
        assert completion == "sh:"

    @pytest.mark.complete("ssh-keygen -O application=ssh:")
    def test_O_application_ssh_colon(self, completion):
        assert not completion

    @pytest.mark.complete("ssh-keygen -O application=nonexistent")
    def test_O_application_nonexistent(self, completion):
        assert not completion
