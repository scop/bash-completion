import pytest


class TestNewgrp(object):

    @pytest.mark.complete("newgrp ")
    def test_1(self, completion):
        assert completion.list
