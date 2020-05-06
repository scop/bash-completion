;;; Directory Local Variables
;;; For more information see (info "(emacs) Directory Variables")

((python-mode
  (eval add-hook 'before-save-hook 'blacken-buffer nil t))
 (sh-mode
  (mode . shfmt-on-save)
  (shfmt-arguments "-s")
  (flycheck-sh-bash-args "-O" "extglob")
  (sh-indent-comment . t)))
