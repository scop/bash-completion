import pytest


class TestMount(object):

    @pytest.mark.complete("mount ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("mount -t ")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("mount /dev/sda1 def", cwd="shared")
    def test_3(self, completion):
        assert completion.list == ["default/"]
        assert not completion.line.endswith(" ")
