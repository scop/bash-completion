import pytest


class TestMount:
    @pytest.mark.complete("mount ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("mount -t ")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("mount /dev/sda1 def", cwd="shared")
    def test_3(self, completion):
        assert completion == "ault/"
        assert not completion.endswith(" ")

    @pytest.mark.complete(
        "mount mocksrv:/", env=dict(PATH="$PWD/mount/bin:$PATH")
    )
    def test_4(self, completion):
        assert completion == "/second/path /test/path /test/path2".split()
