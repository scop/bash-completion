import pytest


class TestSudo(object):

    @pytest.mark.complete("sudo -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("sudo cd fo", cwd="shared/default")
    def test_2(self, completion):
        assert completion.list == ["foo.d/"]
        assert not completion.line.endswith(" ")

    @pytest.mark.complete("sudo sh share")
    def test_3(self, completion):
        assert completion.list == ["shared/"]
        assert not completion.line.endswith(" ")

    @pytest.mark.complete("sudo mount /dev/sda1 def", cwd="shared")
    def test_4(self, completion):
        assert completion.list == ["default/"]
        assert not completion.line.endswith(" ")

    @pytest.mark.complete("sudo -e -u root bar foo", cwd="shared/default")
    def test_5(self, completion):
        assert completion.list == ["foo", "foo.d/"]
