;;; Directory Local Variables
;;; For more information see (info "(emacs) Directory Variables")

((python-mode
  (mode . ruff-format-on-save))
 (sh-mode
  (mode . shfmt-on-save)
  (shfmt-arguments "-s")
  (flycheck-sh-bash-args "-O" "extglob")
  (sh-indent-comment . t)))
