# startup file for bash-completion                         -*- shell-script -*-

((_comp__test_startup__loading_order = ${_comp__test_startup__loading_order:-0} + 1))

_comp__test_startup__foo=user:$_comp__test_startup__loading_order
