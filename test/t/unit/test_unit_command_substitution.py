import pytest

from conftest import TestUnitBase


@pytest.mark.bashcomp(
    cmd=None,
    ignore_env=r"^[+-](COMP(_(WORDS|CWORD|LINE|POINT)|REPLY)|"
    r"cur|prev|cword|words)=",
)
class TestUnitCommandSubstitution(TestUnitBase):
    def test_command_substitution_completion(self, bash):
        """Test that command substitution completion works correctly"""
        # Test basic command substitution: $(echo
        output = self._test_unit(
            "_comp_initialize %s; echo $COMP_LINE,$COMP_CWORD,$cur,$prev",
            bash,
            "(echo '$(echo')",
            1,
            "echo '$(echo'",
            12,
        )
        assert output == "echo,0,echo,"

        # Test command substitution with arguments: $(ls -l
        output = self._test_unit(
            "_comp_initialize %s; echo $COMP_LINE,$COMP_CWORD,$cur,$prev",
            bash,
            "(echo '$(ls -l')",
            1,
            "echo '$(ls -l'",
            13,
        )
        assert output == "ls -l,1,-l,ls"

        # Test that normal completion is not affected
        output = self._test_unit(
            "_comp_initialize %s; echo $COMP_LINE,$COMP_CWORD,$cur,$prev",
            bash,
            "(echo hello)",
            1,
            "echo hello",
            10,
        )
        assert output == "echo hello,1,hello,echo"
