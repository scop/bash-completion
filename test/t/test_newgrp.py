import pytest


class TestNewgrp:
    @pytest.mark.complete("newgrp ")
    def test_1(self, completion):
        assert completion
