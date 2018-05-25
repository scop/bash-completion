;; bash-completion shell-script mode additional settings for Emacs

((sh-mode . ((sh-indent-comment . t)
             ;; Somewhat fragile, waiting for flycheck-sh-bash-args
             (eval . (setq flycheck-command-wrapper-function
                           (lambda (command)
                             (append (butlast command 1)
                                     '("-O" "extglob")
                                     (last command)))))
             )))
