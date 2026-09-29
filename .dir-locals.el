;;; Directory Local Variables
;;; For more information see (info "(emacs) Directory Variables")

((python-mode
  (mode . ruff-format-on-save))
 (sh-mode
  (flycheck-sh-bash-args "-O" "extglob")
  (sh-indent-comment . t)))
