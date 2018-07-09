import os

import pytest


@pytest.mark.bashcomp(ignore_env=r"^\+ROOT=")
class TestRemovepkg(object):

    @pytest.mark.complete("removepkg -")
    def test_1(self, completion):
        assert completion.list == "-copy -keep -preserve -warn".split()

    @pytest.mark.complete("removepkg ", env=dict(ROOT="./slackware"))
    def test_2(self, completion):
        files = sorted(x for x in os.listdir("slackware/var/log/packages"))
        assert completion.list == files
