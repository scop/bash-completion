# $Id: bash-completion.spec,v 1.14 2002/03/18 18:14:57 ianmacd Exp $
#
Name: bash-completion
%define bashversion 2.05a
Summary: bash-completion offers programmable completion for bash %{bashversion}
Version: 20020318
Release: 1
Group: System Environment/Shells
License: GPL
Packager: Ian Macdonald <ian@caliban.org>
Source: http://www.caliban.org/files/bash/%{name}-%{version}.tar.bz2
URL: http://www.caliban.org/bash/
BuildRoot: /var/tmp/%{name}-root
BuildArch: noarch
Requires: bash >= 2.05-12
Requires(post): grep
Requires(postun): sed

%description
bash-completion is a collection of shell functions that take advantage of
the programmable completion feature of bash 2.04 and later.

To use this collection, you ideally need bash 2.05a or later. You can also use
bash 2.05 if you apply the group name completion patch available at
http://www.caliban.org/files/bash/bash-2.05-group_completion.patch.
Alternatively, you can just comment out the lines that contain
'comp{lete,gen} -g'.

If you're using bash 2.04, in addition to commenting out the lines discussed
in the previous paragraph, you'll also to comment out the '-o <option>'
part of each invocation of 'complete' and edit /etc/bashrc to reflect this
version in the $BASH_VERSION test.

%prep
%setup -n bash_completion

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
install bash_completion $RPM_BUILD_ROOT%{_sysconfdir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

%clean
rm -rf $RPM_BUILD_ROOT

%post
if ! grep -q '\[ -f '%{_sysconfdir}'/bash_completion \]' \
     %{_sysconfdir}/bashrc 2>/dev/null; then
    cat <<'EOF' >> %{_sysconfdir}/bashrc
# START bash completion -- do not remove this line
bash=${BASH_VERSION%.*}; bmajor=${bash%.*}; bminor=${bash#*.}
if [ "$PS1" ] && [ $bmajor -eq 2 ] && [ $bminor '>' 04 ] \
   && [ -f %{_sysconfdir}/bash_completion ]; then	# interactive shell
	# Source completion code
        . %{_sysconfdir}/bash_completion
fi
unset bash bmajor bminor
# END bash completion -- do not remove this line
EOF
fi

%postun
if [ "$1" -eq 0 ]; then
    sed -e '/^# START bash completion/,/^# END bash completion/d' /etc/bashrc \
	> /etc/bashrc.tmp
    mv -f /etc/bashrc.tmp /etc/bashrc
fi

%files
%defattr(-,root,root)
%{_sysconfdir}/bash_completion
%dir %{_sysconfdir}/bash_completion.d/
%doc README Changelog contrib/

%changelog
* Mon Mar 18 2002 Ian Macdonald <ian@caliban.org>
- gv ggv now also complete on compressed PDF files
- add completion for -S|--search in dpkg completion
- add chage, write, talk and chfn to list of commands that complete on user
- _insmod(): the output of modinfo has changed in recent versions of modutils,
  so alter awk script to deal with all cases
- add .ico completion to ee, display, etc.
- _scp(): try to perform remote path completion when parameter contains a
  colon

* Thu Mar 14 2002 Ian Macdonald <ian@caliban.org>
- fixed eval indirection bug in _man()

* Mon Mar 11 2002 Ian Macdonald <ian@caliban.org>
- add Debian Linux reportbug(1) and querybts(1) completion
- add dpkg-deb completion and add dpkg-deb options to dpkg completion
- source files in /etc/bash_completion.d prior to sourcing ~/.bash_completion
- fixed _cd() bug where seemingly duplicate completions were returned
- in _dpkg(), certain options were not returning directory completions
- fixed the ignoring of cuurent parameter in _dpkg()
- add _urpmi.media(), _urpmi(), _urpmi.update(), _urpmi.addmedia() and
  _urpmi.removemedia() for Mandrake urpmi completion
- add initial option support to _tar()
- add java completion
- add jar completion
- ant completion replaced by new, more comprehensive routine
- in _rpm(), handle query of uninstalled packages when options are not
  concatenated, i.e. rpm -qp worked, but rpm -q -p did not
- create %{_sysconfdir}/bash_completion.d directory for scripts supplied by
  other packages
- update README

* Wed Mar  6 2002 Ian Macdonald <ian@caliban.org>
- in _man(), Debian does not support man --path, so try setting path using
  manpath and, if that fails, use man --path instead
- _export() and _configure() default to default bash completion
- fix infinite recursion if main completion file installed as
- ~/.bash_completion, since we source this file at the end

* Mon Mar  4 2002 Ian Macdonald <ian@caliban.org>
- cvs completion greatly improved and extended
- _rpm() performs path completion for --whatprovides if parameter contains a /
- _man() now also works on Darwin systems (MacOS X)
- _longopt() now makes vague attempt at path completion after the '=' in
  --long-opt= style options
- _function() now also performs typeset/declare -f completion
- fixed lots of potential sed/awk interpolation problems
- _cd() was not correctly completing on subdirs of $CDPATH
- fixed minor typo in _longopt()
- fixed eval error in _expand() when parameter ends with a \
- fixed quote problem in _man()
- added contrib directory with completions for lesser known programs
- expanded README

* Wed Feb 27 2002 Ian Macdonald <ian@caliban.org>
- dpkg completion added for Debian Linux
- cardctl completion added
- sudo now calls _root_command() to set a more likely root $PATH
- added long option completion to make completion
- minor bug fixes to make, chown and chgrp completion
- _command() now calls _filedir() when subcompletion returns nothing
- psql completion now performs default bash completion if nothing else returned
- innumerable potential opportunities for compgen errors removed
- large scale code clean-up
- documentation dir was accidentally mode 0644, not 0755

* Mon Feb 25 2002 Ian Macdonald <ian@caliban.org>
- fixed compgen error in some long options of _rpm()
- in _psql(), try to get list of valid users from Postgres before resorting to
  system user list
- mkdir and rmdir now complete only on directories and long options
- _cd() was ignoring $CDPATH
- prevent compgen error in _tar() when first parameter starts with hyphen
- fix bug in _known_hosts() where defaulting to standard hostname completion
  would yield a compgen error
- bzip source tar file

* Wed Feb 20 2002 Ian Macdonald <ian@caliban.org>
- new GNU long option completion for large number of commands
  (a2ps, autoconf, automake, bc, gprof, ld, nm, objcopy, objdump, readelf,
  strip, bison, cpio, diff, patch, enscript, cp, df, dir, du, ln, ls, mkfifo,
  mknod, mv, rm, touch, vdir, xargs, awk, gperf, grep, gpg, grub, indent, less,
  m4, sed, shar, date, env, seq, su, tee, uname, who, texindex, cat, csplit,
  cut, expand, fmt, fold, head, md5sum, nl, od, paste, pr, ptx, sha1sum, sort,
  split, tac, tail, tr, unexpand, uniq, wc, units, rsync and irb)
- add gcc completion, plus back-ends (g++, c++, g77, gcj and gpc)
- man completion failed on Sorceror Linux, so use man --path instead of manpath
- function completion failed for function names that start with a hyphen
- killall now completes on signals only if the leading hyphen is supplied
- improved kill completion
- ee, xv, qiv and display also complete on .xpm files
- check for readable $modpath in _insmod()
- check for Linux before installing route and killall completion
- check for commands before installing make and cvs completion
- remove redundant _redir_op() and _redir_test()
- code clean-up in various places

* Fri Feb 15 2002 Ian Macdonald <ian@caliban.org>
- add basic psql completion
- use manpath(1) instead of /etc/man.config to determine man path, so that we
  now honour $MANPATH
- multiple minor rpm completion enhancements
- default to directory completion in _rpm() in more cases
- passwd was actually completing on groups, not users
- fix bug that caused spurious ':' to be returned in all manual sections
- rsh, rlogin and ftp now also use _known_hosts()
- mplayer also completes on .wmv and .mov files files

* Wed Feb 13 2002 Ian Macdonald <ian@caliban.org>
- fix bug in one-liners
- fix _tcpdump() out of memory error

* Tue Feb 12 2002 Ian Macdonald <ian@caliban.org>
- add beginnings of gdb completion
- add bash export completion
- add bash alias and function completion
- add ncftp bookmark completion
- add qiv and display to list of programs that complete on image files
- _scp() now suffixes a ':' on hostnames
- xfig completes on .fig files
- in _apt-cache(), return package list for --show, --showpkg, --depends
  and --dotty
- type now simply completes on commands (complete -c) rather than using
  _command()
- clean up _man() a little
- updated README

* Sat Feb  9 2002 Ian Macdonald <ian@caliban.org>
- handle bzipped man pages in _man() and remove some code duplication
- more file types for ee and xv
- fixed minor quoting and expansion bug in _filedir() and _filedir_xspec()
- include README and Changelog in real tar.gz source archive

* Wed Feb  6 2002 Ian Macdonald <ian@caliban.org>
- make -name, -lname, -iname & -ilname complete on files in _find() and
  change default completion from -o default to -o filenames
- make xdvi also complete on .Z, .gz and .bz2 files
- correct minor bug in one-liners that caused completions that should have
  returned just *.(foo|bar) to also return *.foobar
- add a bunch of one-liners from patch by Matthias Klose
- add --pkgid, --hdrid, --fileid & --tid query options to _rpm() for rpm 4.0.4
- xmms, gqmpeg and freeamp also complete on .pls files
- make unzip also complete on .pk3 (Quake map) files
- make scp work with file names with embedded spaces
- get rpm's package list from /var/log/rpmpkgs only if it is newer than
  /var/lib/rpm/Packages
- clean up /etc/bashrc when package is removed in %postun
- depend on sed for %postun
- improve bash version test in /etc/bashrc (parses cleanly on bash 1.x and 2.x)

* Mon Feb  4 2002 Ian Macdonald <ian@caliban.org>
- _find() now performs directory completion on first parameter if it doesn't
  start with a dash
- unzip now also completes on .exe files
- fixed quoting bug in _zip()
- minor _rpm() touch-ups
- completion added for screen(1) and openssl(1)

* Tue Jan 29 2002 Ian Macdonald <ian@caliban.org>
- perform tilde expansion at more points in _rpm()
- aviplay, not avifile one-liner
- define $BASH_COMPLETION to hold location of completion script
- make _ifupdown() detect a Debian Linux system and act accordingly
- --clean can be used stand-alone in _rpm()

* Wed Jan 23 2002 Ian Macdonald <ian@caliban.org>
- fixed missing quotes bug (duh!)
- 'sudo x <Tab>' now defaults to filename completion if nothing else returned
- rpm -q[a-z]p now works just like rpm -qp[a-z]
- turn off command tracing when DEBUG is unset
- unzip also completes on .jar files
- ggv completes on PostScript files
- remove MP3 extensions from mplayer's compspec
- redirect _command()'s stderr to /dev/null when no compspec for command
- fixed bug where 'sudo x $1 $2 $n' passed rest of line to x's completion
  routine as a single parameter, rather than a series of n tokens
- _rpm() handles --rmspec
- new function _zip() so that gzip and bzip2 complete on .gz and .bz2 files
  when passed the -d flag
- new function _expand() for tilde expansion in pathnames (now called by
  multiple functions)
- new function filedir() is used by cat, less, more, ln and strip, so that
  _expand() can be called for these commands

* Mon Jan 21 2002 Ian Macdonald <ian@caliban.org>
- fixed bug that caused ssh completion to go awry when hostname contained @
- rewrote command completion for commands like sudo, which should first
  complete on a command, then call that command's own completion function
- fixed _man() completion so that file completion on relative paths works

* Tue Jan 15 2002 Ian Macdonald <ian@caliban.org>
- added _mysqladmin() completion

* Wed Jan  9 2002 Ian Macdonald <ian@caliban.org>
- added _chgrp() completion
- added _ifupdown() for Red Hat Linux if{up,down} completion
- improve _iptables() with some chain name completion
- _cd() was no longer completing relative to $CDPATH

* Sat Jan  5 2002 Ian Macdonald <ian@caliban.org>
- fixed _cd() so that if $CDPATH is set and no completions are returned
  relative to its paths, directory completion relative to $PWD is performed
- fixed _cd() so that it completes on directories with an embedded space
- gv also completes on encapsulated PostScript files and PDF files
- jadetex and pdfjadetex added to commands that complete on tex files
- improved _tar() completion to handle .tgz and .tar files
- tar c*f performs file completion
- added 'conflicts' and 'obsoletes' query completions to _rpm()
- added 'repackage' completion option to rpm -[ei]
- fixed _file_and_dir() so that it completes on dirs with an embedded space

* Wed Jan  2 2002 Ian Macdonald <ian@caliban.org>
- check for location of showmount in _mount()
- condense awk|grep combo in _configure() to a single sed command
- change embedded tabs to $'\t' syntax
- be more intelligent about parsing for exclusion (-X) compspecs when
  binding commands to _file_and_dir()

* Thu Dec 20 2001 Ian Macdonald <ian@caliban.org>
- added meta-completion function _file_and_dir for compspecs requiring
  the -X flag. This allows us to exclude files without excluding directories.

* Mon Dec 17 2001 Ian Macdonald <ian@caliban.org>
- add ant and nslookup completion
- make xv and ee complete on more file types

* Mon Dec 10 2001 Ian Macdonald <ian@caliban.org>
- use type instead of which to determine what's on system
- require >= 2.05-12 to allow installation by people using patched 2.05

* Wed Dec  5 2001 Ian Macdonald <ian@caliban.org>
- removed misleading comment on _man completion
- use -g, not -u for group completion (duh!)
- avoid unnecessary use of $COMPREPLY_SAVE in _ssh/_scp
- use '-' as prefix (-P) to kill, not '%', and put it *before* command
- default to filename completion on _scp
- source ~/.bash_completion if it exists

* Wed Nov 28 2001 Ian Macdonald <ian@caliban.org>
- simplify code for group completion, since bash 2.05a has this built in
- now Requires bash 2.05a

* Mon Nov 26 2001 Ian Macdonald <ian@caliban.org>
- make _known_hosts escape meta-characters in path before handing off to awk
- added missing ` to _service

* Tue Nov 20 2001 Ian Macdonald <ian@caliban.org>
- default to _dirnames on _find
- fixed bug in _known_hosts that caused keys in known_hosts2 files to be
  returned as completions
- made _ssh a little more intelligent
- added _scp
- made _cd expand ~ in directory specs
- declared $i as a local variable in many functions

* Sun Nov  4 2001 Ian Macdonald <ian@caliban.org>
- rpm completion now uses /var/log/rpmpkgs if available, which makes some
  completions much more responsive on systems with large numbers of packages
- man completion now checks section 'l' of the manual

* Tue Oct 23 2001 Ian Macdonald <ian@caliban.org>
- add a Requires(post) for grep
- use -q with grep in %post
- use License instead of Copyright
- use macro in %post, rather than a direct reference to the file

* Fri Sep 21 2001 Ian Macdonald <ian@caliban.org>
- fix to _cd that prevented completions being returned when $CDPATH was
  not set and user was attempting to complete on a non-absolute path

* Wed Aug 22 2001 Ian Macdonald <ian@caliban.org>
- removed previous fix to _rpm, since it broke more than it fixed

* Thu Aug 16 2001 Ian Macdonald <ian@caliban.org>
- better Perforce completion from Frank Cusack <frank@google.com>
- _command meta-command completion from Frank Cusack <frank@google.com>
- bug fix to _rpm

* Thu Jul 12 2001 Ian Macdonald <ian@caliban.org>
- minor changes to p4 completion

* Tue Jul 10 2001 Ian Macdonald <ian@caliban.org>
- minor mod to cd completion to make absolute path completion work

* Mon Jul  9 2001 Ian Macdonald <ian@caliban.org>
- fixed bug in have() function that returned false positives
- made some of the default completions more sensible
- added basic Perforce completion

* Tue Jun 19 2001 Ian Macdonald <ian@caliban.org>
- added rudimentary tar, tcpdump and iptables completion functions
- added checking, so that functions are only defined on platforms that
  actually have the commands that will use them

* Mon May 21 2001 Ian Macdonald <ian@caliban.org>
- modified functions for 'complete -o', new in bash 2.05
- require bash instead of bash2

* Wed Jan 31 2001 Ian Macdonald <ian@caliban.org>
- man page completion performs filename completion if no /etc/man.config
- insmod completion wasn't completing module parameters properly
- modprobe -r now completes a la lsmod
- insmod completion now performs filename completion if module name contains /

* Wed Jan 10 2001 Ian Macdonald <ian@caliban.org>
- added Red Hat service completion

* Wed Dec 20 2000 Ian Macdonald <ian@caliban.org>
- added --rmsource as stand-alone option to RPM completion

* Tue Dec 19 2000 Ian Macdonald <ian@caliban.org>
- RPM file glob completion enhanced; bug fix to killall completion

* Mon Nov 20 2000 Ian Macdonald <ian@caliban.org>
- RPM completion updated for rpm 4.x, numerous bug fixes and extra options

* Sun Oct 29 2000 Ian Macdonald <ian@caliban.org>
- fixed bug in rpm completion that made -e, etc. not find all RPMs

* Thu Oct 19 2000 Ian Macdonald <ian@caliban.org>
- reverted cd, mkdir & pushd to standard -d directory completion

* Mon Oct  9 2000 Ian Macdonald <ian@caliban.org>
- minor improvements to _man & _find
- improved FreeS/WAN completion
- added Debian apt-get & apt-cache completion
- added more intelligent directory completion in new _directory function

* Mon Sep 25 2000 Ian Macdonald <ian@caliban.org>
- version set to 20000925
- insmod completion improved with parameter completion
- ssh completion broken up into _known_hosts function for use by other commands
- Makefile completion added

* Mon Sep 11 2000 Ian Macdonald <ian@caliban.org>
- update to 0.06
- fixed bug in man completion that caused pages with a dot (e.g. lilo.conf)
  not to be found
- ssh completion enhanced with command completion after host
- fixed bug in ssh completion that caused spurious completions when completing
  on an IP address
- added route(8) completion

* Tue Aug 29 2000 Ian Macdonald <ian@caliban.org>
- update to 0.05
- fixed bug in killall completion
- added cipher completion to -c option of ssh

* Mon Aug 28 2000 Ian Macdonald <ian@caliban.org>
- update to 0.04
- added ssh completion
- tidied the code in some other functions

* Fri Aug 11 2000 Ian Macdonald <ian@caliban.org>
- update to 0.03
- added cvs, rpm, chsh & chkconfig completion

* Wed Aug  2 2000 Ian Macdonald <ian@caliban.org>
- update to 0.02

* Sun Jul 29 2000 Ian Macdonald <ian@caliban.org>
- 0.01 packaged as RPM
