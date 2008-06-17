# TODO -- needs someone to review it entirely.

Name: bash-completion
Summary: Programmable completion for bash 2.05b and later.
Version: 20080617
Release: 1
Group: System Environment/Shells
License: GPL
# TODO
#Packager: Ian Macdonald <ian@caliban.org>
Source0: http://www.caliban.org/files/bash/%{name}-%{version}.tar.bz2
#Source0: http://bash-completion.alioth.debian.org/files/%{name}-%{version}.tar.bz2
Source1: bash_completion.sh
URL: http://www.caliban.org/bash/
#URL: http://bash-completion.alioth.debian.org
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch
Requires: bash >= 2.05-12, grep, textutils, sed, fileutils

%description
bash-completion is a collection of shell functions that take advantage of
the programmable completion feature of bash 2.04 and later.

To use this collection, you should ideally have version 2.05b or later of
bash. This will ensure that all features work and that you experience the
least amount of hindrance from bugs in the completion subsystem.

bash 2.05a may also be used, but certain unavoidable annoyances will be
experienced. You should upgrade to at least 2.05b.

bash 2.05 may be used if you apply the group name completion patch available
at http://www.caliban.org/files/bash/bash-2.05-group_completion.patch.
Alternatively, you can just comment out the lines in
%{_sysconfdir}/bash_completion that contain 'comp{lete,gen} -g'. However,
upgrading to at least 2.05b is recommended.

If you're stuck using bash 2.04, in addition to commenting out the lines
mentioned above, you'll also need to edit %{_sysconfdir}/bashrc
to reflect this version in the $BASH_VERSION test. Again, an upgrade to at
least 2.05b is strongly recommended.

%prep
%setup -n bash_completion

%install
rm -rf $RPM_BUILD_ROOT %{name}-ghosts.list
install -dm 0755 $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -dm 0755 $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
install -pm 0644 bash_completion $RPM_BUILD_ROOT%{_sysconfdir}/
sed -e 's@/etc@%{_sysconfdir}@g' %{SOURCE1} > $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/bash_completion.sh
touch -r %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/bash_completion.sh
# Take care of contrib files
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -pm 644 contrib/* $RPM_BUILD_ROOT%{_datadir}/%{name}
cd contrib
for f in *; do
  ln -s %{_datadir}/%{name}/$f $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
  echo "%ghost %{_sysconfdir}/bash_completion.d/$f" >> ../%{name}-ghosts.list
done
cd -

%clean
rm -rf $RPM_BUILD_ROOT

%pre
# Legacy clean-up
if grep -q '^# START bash completion' %{_sysconfdir}/bashrc; then
    sed -e '/^# START bash completion/,/^# END bash completion/d' %{_sysconfdir}/bashrc > %{_sysconfdir}/bashrc.$$
    chmod --reference %{_sysconfdir}/bashrc %{_sysconfdir}/bashrc.$$
    touch -r %{_sysconfdir}/bashrc %{_sysconfdir}/bashrc.$$
    mv -f %{_sysconfdir}/bashrc.$$ %{_sysconfdir}/bashrc
fi

%define bashcomp_trigger() \
%triggerin -- %1\
if [ ! -e %{_sysconfdir}/bash_completion.d/%{?2}%{!?2:%1} ] ; then\
  ln -s %{_datadir}/%{name}/%{?2}%{!?2:%1} %{_sysconfdir}/bash_completion.d\
fi\
%triggerun -- %1\
[ $2 -gt 0 ] || rm -f %{_sysconfdir}/bash_completion.d/%{?2}%{!?2:%1}\
%{nil}

%bashcomp_trigger bittorrent
%bashcomp_trigger cksfv
%bashcomp_trigger clisp
%bashcomp_trigger freeciv
%bashcomp_trigger gcc-gnat gnatmake
%bashcomp_trigger gkrellm
%bashcomp_trigger mailman
%bashcomp_trigger mcrypt
%bashcomp_trigger mtx
%bashcomp_trigger ruby-ri ri
%bashcomp_trigger sbcl
%bashcomp_trigger snownews
%bashcomp_trigger unace
%bashcomp_trigger unixODBC isql
%bashcomp_trigger unrar

%files -f %{name}-ghosts.list
%defattr(-,root,root)
%config %{_sysconfdir}/bash_completion
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/profile.d/bash_completion.sh
%dir %{_sysconfdir}/bash_completion.d/
%{_datadir}/%{name}/
%doc BUGS COPYING README TODO Changelog

%changelog
* Wed Mar  1 2006 Ian Macdonald <ian@caliban.org> 20060301-1
- Completion for minicom(1), mtr(8), sysctl(8), smartctl(8), vncviewer(1),
  invoke-rc.d, update-rc.d and dpkg-source has been added.
- gdb completion of second parameter was broken when first parameter contained
  white space.
- gdb completion wasn't completing second parameter correctly when it was
  a file, rather than a PID.
- Ruby ri completion has been broken for some time. This is now fixed.
- Various fixes to work around change in how POSIX quoting is handled in
  bash 3.1.
- subversion completion has been reimplemented from scratch and integrated
  into the main file.
- iconv(1) completion has been improved.
- yum(8) completion has been updated for current version of yum.
- ant completion will now make use of complete-ant-cmd.pl, if available.
- cvs(1) completion has been improved with 'update' and 'stat' completion.
- 'aptitude show' now works in the same way as 'apt-cache show'.
- make(1) now also completes on file names.
- MPlayer will now also complete on .flac, .mpc and .3gp files.
- wine will now also complete on .exe.so files.
- unzip will now also complete on oowriter's .ott files.
- xine et al will now complete on .mng files.
- The list of programs completing on .dvi files has been expanded.
- The range of files on which timidity and evince complete has been expanded.
- mkisofs completion now defaults to treating results as file names.
- $DEBUG has been renamed $BASH_COMPLETION_DEBUG to avoid namespace clashes
  with other software.
- man(1) completion now works correctly on OpenBSD.
- svk and Mercurial completion have been added to contribs.
- The %%install code that creates bash_completion.sh has been moved to a
  separate file.
- Ville Skyttä's triggers code from the Fedora Core extras RPM spec file has
  been integrated.
- Preserve timestamps when installing files. This was also lifted from the FC
  extras package spec file.
- Many other small optimisations and fixes.

* Thu Jul 21 2005 Ian Macdonald <ian@caliban.org>
- MPlayer options should now use dashes, not underscores.
- mc completion has been greatly extended.
- lilo completion fix.
- iwconfig improvements.
- Fix tcpdump and dhclient completion to use correct interfaces function.
- Turn off glob expansion disabling in _filedir(), as this has the annoying
  side-effect of temporarily cancelling alias expansion.

* Wed Jul 20 2005 Ian Macdonald <ian@caliban.org>
- Patterns for tarball matching fixed.
- Evince completion for .pdf files added.
- More OpenOffice 2 completions added.
- Completion for xine front-ends and kplayer/MPlayer added.

* Tue Jul 12 2005 Ian Macdonald <ian@caliban.org>
- completion added for rpm2cpio, ntpdate, getent, id and cpio.
- Make mutt completion also work for muttng.
- tar 1.15.1 can unpack compressed archives, even if [IZzjy] are not given.
- Fix _filedir(), so that literal filenames that appear to be glob patterns are
  not treated as such.
- Fix scp completion when filename contains shell metacharacters.
- Fix broken sudo completion.
- More extensions for MPlayer.
- Support the new open document formats of OpenOffice 2.0.
- Many minor fixes and enhancements.

* Fri Jan 21 2005 Ian Macdonald <ian@caliban.org>
- Fix broken _command() completion.

* Thu Jan 20 2005 Ian Macdonald <ian@caliban.org>
- Improve ssh2 known hosts completion.
- Remove xargs from list of commands that do longopts completion. xargs
  now does completion like sudo, exec, nice, strace, etc.
- Pass over switches to metacommands like sudo, nice, exec, etc.
- unzip should also work on .sxw files.
- Lots of commands that use _longopts() don't use filenames at all, so
  these shouldn't be mapped with '-o filenames'.
- Make dd treat completions as filenames, which is bad for options, but
  good for filename arguments to 'if' and 'of'.
- Fix lvresize errors when running as non-root.

* Wed Jan 12 2005 Ian Macdonald <ian@caliban.org>
- Make completion work for chown/chgrp when group names contain spaces.
- Wireless tools completion improvements.
- Make location of openssl.cnf somewhat more flexible.

* Mon Jan  3 2005 Ian Macdonald <ian@caliban.org>
- Complete rewrite of openssl(1) completion.
- Added pkg-config completion.
- Cygwin mount patch and minor find (fstab) robustness fix.
- Enhanced make completion with alternate Makefile paths.
- Added ps2pdf completion.
- Added mkinitrd completion.
- modprobe factorisation patch merged.
- Wireless tools improvements.
- cvs(1) completion fixes.
- Add ,v files to list rcs(1) can complete on.
- Fixes for completing RealAudio files.
- screen completion now includes the socket part of session names.
- sitecopy and snownews enhancements in contrib/.

* Sun Oct 17 2004 Ian Macdonald <ian@caliban.org>
- properly unset $have at end of sourcing
- scp completion was broken for file names, both local and remote, that
  contained shell metacharacters.
- fix gzip with files whose names contain spaces
- rename _comp-dpkg-installed-packages() to _comp_dpkg_installed_packages()
  to comply with POSIX.2 shell function naming
- make talk, ytalk and finger not add a suffix of '@' after completing a user
  name
- apt-cache improvements
- add .miff as an extension for display completion
- process targets in included Makefiles during make completion
- new dhclient, lvm and bittorrent (contrib) completion
- fix sed error on service completion
- add kghostview and kpdf for PostScript and PDF files
- allow mplayer to complete on .dv files
- CVS completion fix to allow better handling of files and dirs whose names
  contain whitespace
- rpm completion fix to avoid "--nodigest --nosignatures" being passed as a
  single option
- many minor fixes

* Sun Jul 11 2004 Ian Macdonald <ian@caliban.org>
- eliminate use of grep in _filedir_xspec() for better performance
- minor fix to mutt completion
- fix for dpkg completion
- allow symbolic links in /etc/bash_completion.d
- improve insmod, modinfo etc completion with path names

* Sun Jul  4 2004 Ian Macdonald <ian@caliban.org>
- append a '/' to directories completed from $CDPATH
- add _rl_enabled() to detect whether a given readline variable is on
- pgrep and pidof completion
- use getent for UID and GID completion when available
- allow service completion to work on xinetd services
- fix some spurious warnings in CVS completion
- use --dump-options to get switchs for gpg completion
- fix mutt completion so that leading '=' character is handled properly
- allow Emacs to complete on archives
- add autossh to list of commands that perform _ssh() completion
- properly complete on .Z files during tar completion
- add ssh-installkeys to list of programs that use known host completion
- various OpenOffice completions added
- fix PID completion for AIX and Solaris
- update to aptitude completion
- '[' must come first in character classes for sed 4.1. _configure() needed to
  be fixed.

* Wed May 26 2004 Ian Macdonald <ian@caliban.org>
- added info completion
- chkconfig factorisation and improvements
- xmms(1) gets its own completion function
- use filenames by default for cdrecord completion
- added aspell completion
- add SuSE support for ifup/down and ifstatus, if present
- improvement to _update_alternatives()
- minor fix to _command() to allow leading whitespace on the command line
- dpkg -P was not recognised or completed
- don't allow aliases for grep to be used during make completion
- make mutt file completion actually work after redirection
- fix mutt sed errors after redirection
- builtin completes on builtins

* Wed Mar 31 2004 Ian Macdonald <ian@caliban.org>
- remove links from list of commands that complete on .html
- mplayer file extension additions
- add CUPS cancel(1) completion
- minor mkisofs fix
- add amaya to list of browsers
- _comp-dpkg-installed-packages() was not returning packages designated
  'essential'
- allow cvs completion to handle the various sub-command abbreviataions
- fix man and cc completion for Cygwin
- some versions of bash don't like function names containing hyphens
- some new completions in contrib

* Tue Feb 10 2004 Ian Macdonald <ian@caliban.org>
- big speed up for dpkg completion
- fix chsh completion to work on Debian
- fix for ant completion
- fix up a continuation error in _filedir()
- make 'make -f' completion work properly
- don't unset $have twice at end of script

* Tue Feb 10 2004 Ian Macdonald <ian@caliban.org>
- fix broken command completion for sudo and others
- make apt-cache know about the 'rdepends' option
- install yum-arch completion only if we also have yum
- add dd completion
- xine and mplayer can complete on .VOB files
- make xspec parsing immune to comments
- allow mplayer to complete on .m2v files, too
- make export completion do proper quoting when completing a variable's value
- add 'up' as a synonym of 'update' in cvs completion
- xine can also complete on .asx files

* Thu Jan  1 2004 Ian Macdonald <ian@caliban.org>
- avoid pulling in .rpm* files from $BASH_COMPLETION_DIR/*
- Postfix completion enhancement
- wvdial improvements
- FreeBSD portinstall fix
- make ri (Ruby Interactive) completion work with more versions
- mtx and snownews completion in contrib dir

* Thu Dec 25 2003 Ian Macdonald <ian@caliban.org>
- ogg123 can now handle .flac and .spx files
- mutt completion improvements
- more improvements to find(1) completion

* Mon Dec 15 2003 Ian Macdonald <ian@caliban.org>
- find(1) completion improvements
- add ImageMagick completion
- apt-cache completion updates
- allow gpdf to complete on PDF files

* Tue Nov 25 2003 Ian Macdonald <ian@caliban.org>
- first cut at mutt(1) completion
- user completion for w(1)
- yum completion improvements

* Wed Nov 12 2003 Ian Macdonald <ian@caliban.org>
- remove bogus targets from make completion
- default to file completion in perldoc, if current parameter contains
  a slash
- add .aac and .mp4 support to mplayer, as well as support for matroska files
- rpm -qf improvement
- gzip should complete on .gz files after redirection
- bash 'command' built-in should also complete on commands

* Wed Oct 22 2003 Ian Macdonald <ian@caliban.org>
- another unbound variable warning removed
- add completion for vsound and really
- FreeBSD portinstall speed improvements
- ee and display also complete on .pcx files
- yum and yum-arch now use -o filenames

* Mon Oct  7 2003 Ian Macdonald <ian@caliban.org>
- compatibility fixes for forthcoming bash 3.x
- added yum(8) and yum-arch(8) completion
- iptables fixes
- minor FreeS/WAN fixes
- ggv can also handle .bz2 files

* Mon Sep 29 2003 Ian Macdonald <ian@caliban.org>
- various Java fixes
- urpmi completion removed; it's now maintained by the urpmi people
- postsuper fix
- perl fix
- .m3u completion for relevant tools

* Thu Sep 11 2003 Ian Macdonald <ian@caliban.org>
- gzip and bzip2 rewrite
- fix service completion from completing on ~ and function files
- add .xpi files to unzip completion
- properly skip classpath string in Java completion
- minor ant completion fix

* Thu Aug 21 2003 Ian Macdonald <ian@caliban.org>
- add mc completion
- add postcat completion and minor improvements to other Postfix commands
- make chown completion work, whether or not the colon between user and
  group name is escaped
- bind pkill to same completion function as killall for now
- xine can also play .wav files
- allow rpm to complete on .nosrc.rpm packages

* Mon Aug 11 2003 Ian Macdonald <ian@caliban.org>
- more make completion fixes
- add mkisofs completion
- add cdrecord completion
- make _uids() and _gids() functions use Perl for getpwent(3)
- fix killall completion on bash 2.05a

* Sun Aug  3 2003 Ian Macdonald <ian@caliban.org>
- 'make' completion rewrite
- various rpm completion fixes
- tcpdump completion fixes
- mplayer completion improvements
- allow find completion to return filenames in addition to options if
  completing on a null token
- perldoc clean-up
- vi et al no longer complete on Java .class files

* Mon Jul 21 2003 Ian Macdonald <ian@caliban.org>
- .shtml completion for browsers
- extra extension completions for xine and xanim
- vim et al should not complete on .gz and .bz2 files
- mplayer fixes and improvements
- dselect fix

* Sun Jul 13 2003 Ian Macdonald <ian@caliban.org>
- allow find to search through more than one directory root
- update rpm completion for rpm 4.2
- modify kldload and portinstall completion for FreeBSD 5
- minor fix for ifconfig and iwconfig completion

* Mon Jun 30 2003 Ian Macdonald <ian@caliban.org>
- fix process truncation problem with killall completion
- psql update from
- new urpmi update
- allow mplayer to complete on .dump files
- add xhost to host completion

* Sat Jun  7 2003 Ian Macdonald <ian@caliban.org>
- _command() subcompletion should now work OK for commands with spaces,
  when command completion is done with complete -W, when complete -F function
  is used, and when function uses COMP_POINT or COMP_LINE
- make ifconfig completion work on FreeBSD
- explicit path to postconf(1) for Postfix completion
- minor mount completion fix
- make .html completion case-insensitive
- fix FreeBSD portinstall completion

* Tue May 27 2003 Ian Macdonald <ian@caliban.org>
- minor apt-cache completion fix
- handle the case whereby we're sourced from a shell function
- dpkg completion was missing the -x option
- add FreeBSD portinstall completion
- various bits of code referred to ${#COMP_WORDS} instead of ${#COMP_WORDS[@]}
- silence stderr in man invocation in perldoc completion
- make insmod/modprobe completion handle .ko files for the 2.5/2.6 Linux kernel
- modify _cd() to make an attempt at variable completion

* Mon May  5 2003 Ian Macdonald <ian@caliban.org>
- fixed rpm completion for Mandrake 9.1
- this RPM now has much cleaner installation. /etc/bashrc is no longer
  modified; instead, we work from a small stub script in /etc/profile.d/

* Thu May  1 2003 Ian Macdonald <ian@caliban.org>
- minor fix to _insmod() to get modprobe -k <Tab> to do something
- some rpm completion speed-ups
- add --target to rpm -[bt] completion
- fix scp completion problem where 'scp file\ <Tab>' did not complete for
  a file with a space in the name
- make have() use a wider path to search for binaries on the system
- fix up command completion noglob stuff ('sudo service' was broken, for
   example)
- update to urpmi completion
- fix FreeBSD ports programs completion
- allow xmms to complete on .mp2 files

* Sat Apr 19 2003 Ian Macdonald <ian@caliban.org>
- fix for sudo completion when subcommand is passed wildcard globs
- minor improvements to gpg completion
- fix _expand() helper function
- move dict completion into main file and rewrite from scratch

* Mon Apr 14 2003 Ian Macdonald <ian@caliban.org>
- added completion for iconv(1)
- make apt-cache complete the showsrc argument
- added KDE dcop completion
- fix another unset variable warning in CVS completion

* Thu Mar 27 2003 Ian Macdonald <ian@caliban.org>
- stop /etc/init.d completions from completing on stand-alone commands
  of the same name
- gdb completion bug fixed

* Thu Feb 27 2003 Ian Macdonald <ian@caliban.org>
- exclude mysql and ssh init scripts from completion, as they clash with
  stand-alone commands
- make bash-completion compatible with the new bash completion emulation
  feature of zsh
- add .tga completion to ee and display
- make slay complete on users
- don't redefine su completion

* Sun Feb  9 2003 Ian Macdonald <ian@caliban.org>
- allow 'cvs -d' to complete from ~/.cvspass
- don't append spaces after directories when doing mount completion
- allow default completion if there are no matches during make completion
- allow Java completion to cover .ear files (J2EE Enterprise Application
- silence more unset variable warnings in CVS completion

* Sat Feb  1 2003 Ian Macdonald <ian@caliban.org>
- rsync completion
- make service completion Debian compatible
- minor cvs fix

* Sun Jan 26 2003 Ian Macdonald <ian@caliban.org>
- contrib additions for unrar, unace, cksfv and povray
- make completion now also supports GNUmakefile
- modinfo completes the same as insmod and modprobe
- minor fix to ant completion
- silence more unset variable warnings in cvs completion

* Sat Jan 18 2003 Ian Macdonald <ian@caliban.org>
- fix mount completion so that it also works on Solaris
- improve handling of 'cvs export'
- fixes to man completion to make it work on Solaris

* Mon Jan 13 2003 Ian Macdonald <ian@caliban.org>
- allow vim et al to complete on .a files and ld.so.conf
- cd should also complete on variable names if cdable_vars is set
- jar completes on .war as well as .jar
- when completing on classes inside Java JAR files, use zipinfo instead of
  the jar command, if it is available
- silence awk errors in known_hosts completion

* Tue Dec 31 2002 Ian Macdonald <ian@caliban.org>
- extensive gpg(1) completion
- wvdial(1) completion
- mplayer improvements
- minor known_hosts() fix

* Mon Dec 23 2002 Ian Macdonald <ian@caliban.org>
- add groups(1) to list of commands that complete on user names
- add dig(1) to commands that complete on known hosts
- in known hosts completion, also check for known hosts files in
  /etc/ssh/ssh_known_hosts and /etc/ssh/ssh_known_hosts2
- mplayer fixes
- Java classpath string was not being skipped
- minor spec file changes

* Sat Dec 21 2002 Ian Macdonald <ian@caliban.org>
- extensive mplayer completion
- avoid unbound variable warnings when bash is run with 'set -u'
- avoid error if CVS completion is attempted in a directory with no
  CVS/Entries file

* Tue Dec 17 2002 Ian Macdonald <ian@caliban.org>
- tar should also be able to recognise .tar.Z files
- perldoc completion also returns names of core Perl man pages
- update README

* Fri Dec 13 2002 Ian Macdonald <ian@caliban.org>
- ytalk now completes in the same way as talk
- traceroute6, tracepath and tracepath6 now also complete on known hosts
- command completion now also performed for ltrace, then, else and do
- minor fix to gdb completion
- commands that complete on .htm(l) files now complete on .(x)htm(l)

* Thu Dec  5 2002 Ian Macdonald <ian@caliban.org>
- first stab at ypmatch(1) and ypcat(1) completion
- check for insmod and rmmod in path before installing completion functions
- add rcsdiff to list of RCS commands that use RCS completion function
- don't bother completing on PIDs in screen completion
- add FreeBSD portupgrade completion
- add FreeBSD kernel module command completion
- add .zargo to list of extensions that unzip can complete on (Gentleware)
- don't source files in $BASH_COMPLETION_DIR if they are vi swap files,
  Debian back-ups, Emacs temp files, back-ups, etc.
- add .flac completion to xmms
- make dpkg completion also handle .udeb files
- dpkg completion completes for -c as for --contents
- make gzip work with .tgz files, not just .gz files
- make ee and display complete on .pnm and .xwd files
- minor rpm fix
- make texi2dvi complete like other LaTeX programs

* Sat Oct 26 2002 Ian Macdonald <ian@caliban.org>
- many scp fixes
- Mandrake urpmi completion improvements
- .wav completion for mplayer
- very basic look(1) completion
- fix for man page completion when name has colon in it

* Tue Oct 22 2002 Ian Macdonald <ian@caliban.org>
- fix the fix to scp completion

* Mon Oct 21 2002 Ian Macdonald <ian@caliban.org>
- PID is optional in screen completion
- avoid problems on systems where ps has been aliased
- fix FreeBSD pkg_delete completion
- fixes to scp completion

* Thu Oct 17 2002 Ian Macdonald <ian@caliban.org>
- various improvements to scp completion
- add Slackware Linux removepkg completion
- add FreeBSD pkg_delete and pkg_info completion
- Perl module completion endless loop fix
- minor fix to apt-build completion
- allow xmms to also complete on .wav files
- return core files in gdb completion
- tar file completion on files within .bz2 archives did not work
- tar completion on files inside tar files should not return files outside
  archive

* Sun Oct 13 2002 Ian Macdonald <ian@caliban.org>
- fixed apt-cache 'show' completion bug
- fixed function names with hyphens
- aptitude completion function was loaded, regardless of presence of program
- various improvements to other Debian command completions
- mount completion should ignore commented out lines in /etc/fstab
- add option completion to Python
- make Python completion append a '/' at the end of directories
- offer --force-confmiss, not --force-miss with dpkg completion
- perform file completion with ssh when -i is given

* Mon Oct  7 2002 Ian Macdonald <ian@caliban.org>
- fix missing keywords in find completion
- back out double hostname scp fix, as issue is more complex

* Sat Oct  5 2002 Ian Macdonald <ian@caliban.org>
- make java completion aware of -jar
- make jar completion accept a leading dash to its option list
- fix cvs counting bug
- silence some apt-cache complaints in various completions
- avoid awk error message in rmmod completion when passed a '\'
- avoid grep error message in mount completion when passed a '\'
- avoid double machine name bug in scp completion
- check for existence of links history file in links completion
- many Debian command updates

* Tue Oct  1 2002 Ian Macdonald <ian@caliban.org>
- links completion
- fix quoting issue in chown and chgrp completion

* Sat Sep 28 2002 Ian Macdonald <ian@caliban.org>
- add some options to apt-get and apt-build completion

* Mon Sep  9 2002 Ian Macdonald <ian@caliban.org>
- fix for 'cvs add', where filename ends with another filename
- add option completion for chown and chgrp
- add .ogm and .mp4 to mplayer and xine
- more file-types for xmms to complete on

* Mon Aug 19 2002 Ian Macdonald <ian@caliban.org>
- add Linux iwconfig(8) completion
- xmms can now also complete on .xm, .mod and .s3m files
- gnatmake completion in contrib directory

* Mon Aug 12 2002 Ian Macdonald <ian@caliban.org>
- ./configure completion was not returning all possible completions on systems
  with mawk
- no space after export completion (assuming bash 2.05b)
- add .wmv files to those that aviplay will complete on

* Sat Aug  3 2002 Ian Macdonald <ian@caliban.org>
- silence eval errors in _filedir_xspec() when quoting goes awry
- add apt-build completion
- add elinks to commands performing .html completion
- perl and perldoc completion
- apparently, vim can edit .gz and .bz2 files, so don't exclude these from
  the completion list
- fix sed error when completing a relative path in insmod completion

* Sat Jul 27 2002 Ian Macdonald <ian@caliban.org>
- _man(): when completing on man page names, a trailing dot would be removed
  when trying to complete a man page such as syslog.conf
- fix typo in vi/vim completion and add a couple more file types to avoid
  returning as possible completions

* Tue Jul 23 2002 Ian Macdonald <ian@caliban.org>
- add _user_at_host() for user@host style completion. Use this for finger
  and talk
- scp completion now no longer appends a space with bash 2.05b
- scp completion now discards stderr when performing remote path completion
- allow '@' in the release of RPM packages for rpm completion

* Tue Jul 16 2002 Ian Macdonald <ian@caliban.org>
- mount completion will now complete on Samba shares (only the volume, not
  the hostname part)
- catch more possible completions in ./configure completion
- bzgrep et al now also recognise .tbz2
- add some more file types that xv can complete on

* Thu Jul 11 2002 Ian Macdonald <ian@caliban.org>
- PINE address book completion fix
- allow WINE to complete on .scr files

* Thu Jul  4 2002 Ian Macdonald <ian@caliban.org>
- urpmi completion update
- touch-ups to mplayer completion

* Wed Jun 26 2002 Ian Macdonald <ian@caliban.org>
- make tilde expansion work during chown completion
- make tar completion '-o filenames' by default.
  '-o dirnames' can be obtained by setting $COMP_TAR_INTERNAL_PATHS prior to
  sourcing.
- restore expansion of ~ in _expand(): its removal broke too much

* Mon Jun 24 2002 Ian Macdonald <ian@caliban.org>
- avoid tilde expansion in _expand()
- gdb completion defaults to -o filenames, not -o default
- simplify process matching code in gdb completion
- allow unzip to complete on Java Enterprise Application Archive files (.ear)

* Fri Jun 21 2002 Ian Macdonald <ian@caliban.org>
- add edit and unedit to cvs completion
- don't exclude .o files from make completion
- {gzip,bzip2} -t should also complete on .gz and .bz2 files, respectively
- man completion still needed one fix for FreeBSD

* Wed Jun 19 2002 Ian Macdonald <ian@caliban.org>
- allow .tbz as an extension during tar completion
- check for non-Linux and presence of gsed (GNU sed). If it's there, alias
  it to sed.
- make man completion work for FreeBSD

* Sun Jun 16 2002 Ian Macdonald <ian@caliban.org>
- eliminate errors when setting read-only variables
- fix quoting bug in PINE address completion

* Tue Jun 11 2002 Ian Macdonald <ian@caliban.org>
- BASH_COMPLETION_DIR had a typo and was set to /etc/bash_completion
  instead of /etc/bash_completion.d
- in tar completion, completing on files within a tar file would consume all
  memory in bash 2.05a (the perennial compgen -W bug)

* Sun Jun  9 2002 Ian Macdonald <ian@caliban.org>
- tar completion now recognises the .tbz2 extension
- 'tar cf' completed properly, but 'tar -cf' did not
- galeon, links and curl now also complete on .html files
- unzip and zipinfo now recognise the .wsz extension

* Wed Jun  5 2002 Ian Macdonald <ian@caliban.org>
- add .html file completion for netscape, mozilla, lynx, w3m
- use 'command ls' instead of '\ls', since while the latter avoids aliases,
  it will still call functions. 'command' always gets us the binary.
- add newgrp to list of commands that complete on group names
- tar completion now completes first on tar files, then on their contents
- add bash complete completion
- add lilo(8) completion
- Java completion overhaul

* Sat Jun  1 2002 Ian Macdonald <ian@caliban.org>
- add basic completion for RCS suite (rcs, rlog, ci, co)
- fix bug in known hosts completion on platforms with no GNU sed
- fix bug present in both _comp-dpkg-installed-packages() and
  _comp-dpkg-hold-packages() that results in all packages being returned

* Tue May 28 2002 Ian Macdonald <ian@caliban.org>
- java -jar completes on .jar files
- urpmi now completes on rpm files
- urpmf, urpme, urpmq completion added

* Tue May 21 2002 Ian Macdonald <ian@caliban.org>
- add bzme completion (Mandrake)
- unzip & zipinfo also complete on .war files (as used by Tomcat, etc.)
- _comp-dpkg-installed-packages(): remove dependence on grep-dctrl

* Sun May 19 2002 Ian Macdonald <ian@caliban.org>
- Python now completes first on a .@(py|pyc|pyo) file, then on any file
- rpm helper function _file_glob() has been integrated into _filedir()
- replace many calls to compgen -f/-d with calls to _filedir()
- scp completion now also completes on host aliases from ssh config files
- add a Requires for textutils, since %post needs cat(1)
- add a Requires for fileutils, since %postun needs mv(1)
- bug fixes to some of the Debian package management functions

* Thu May 16 2002 Ian Macdonald <ian@caliban.org>
- fix bug in cvs completion when completing on filenames that contain regex
  metacharacters
- fix bug that caused null completion list in 'cvs diff'
- cd completion was failing when CDPATH pointed to directories containing
  spaces in their names
- don't include variable assignments when returning targets in make completion

* Tue May 14 2002 Ian Macdonald <ian@caliban.org>
- _ssh() and _known_hosts(): ssh config file directives are case-insensitive
- simplify cd completion and fix a bug in unique stem completion

* Sat May 11 2002 Ian Macdonald <ian@caliban.org>
- work around compgen -W memory eating bug in ssh completion
- perform tilde expansion in dpkg completion
- use sed instead of Perl in urpmi completion
- add MP3 files to those on which mplayer and xine will complete
- mpg321 completes on MP3 files
- minor code patch-ups to make Linux-specific functions work on HURD systems
- in cvs completion, 'cvs co -c' should take into account '-d'
- postmap(1) and postalias(1) from the latest Postfix snapshot have a
  new option, '-o'

* Tue May  7 2002 Ian Macdonald <ian@caliban.org>
- add completion for Postfix commands
- rpm completion additions for rpm 4.1
- ssh completion now also returns host aliases from /etc/ssh/ssh_config and
  ~/.ssh/config files
- _known_hosts(): check /etc/ssh/ssh_config and ~/ssh/config to get location
  of global and user known hosts files, rather than assuming default locations
- 'cvs checkout' now checks for registered modules, not just directories in
  $CVSROOT
- add Debian Linux aptitude(8) completion
- _comp-dpkg-installed-packages(): return list of installed packages, rather
  than all installable packages

* Sat May  4 2002 Ian Macdonald <ian@caliban.org>
- add python completion on .py, .pyc and .pyo files
- cvs completion now handles diff option
- make xine complete on the same file types as mplayer
- cvs completion code clean-up
- add long option completion to psql completion
- _filedir_xspec(): avoid eval errors when completing within backticks or
  quotes

* Tue Apr 30 2002 Ian Macdonald <ian@caliban.org>
- reworking of Postgresql completion
- add PINE address-book completion
- _cvs(): remove a superfluous grep and redirect stderr on ls
- make installation of RPM functions a compound statement

* Sat Apr 27 2002 Ian Macdonald <ian@caliban.org>
- add update-alternatives completion
- _urpmi_media(): urpmi completion now deals properly with spaces
- check that the files we try to source in $BASH_COMPLETION_DIR are actually
  plain old files
- zipinfo now completes on the same files as unzip
- _export(): make 'export FOO=$<Tab>' complete on variable names
- latex et al now also complete on .dtx and .ins files
- add Debian dselect(8) completion

* Mon Apr 22 2002 Ian Macdonald <ian@caliban.org>
- _filedir(): fix error when completing on a quoted parameter
- add dict completion in contrib
- tex, latex et al now also complete on .latex files
- _cd(): remove useless call of _expand()
- move ri completion into contrib, because it's relatively uncommon
- use $UNAME instead of $OS, since the latter purportedly interacts badly
  in environments such as Cygwin

* Thu Apr 18 2002 Ian Macdonald <ian@caliban.org>
- add 'annotate' to list of cvs commands that perform completion
- added ri (Ruby documentation) completion
- _rpm(): rpm -qf worked, but rpm -q -f didn't. Simiarly, rpm -V -f didn't
  work; nor did rpm -Vg or rpm -V -g
- avoid errors when comp{gen,lete} -g aren't available on unpatched bash 2.05

* Sat Apr 13 2002 Ian Macdonald <ian@caliban.org>
- backed out recalculation of current parameter position after wildcard
  expansion in sudo completion

* Mon Apr  8 2002 Ian Macdonald <ian@caliban.org>
- apt-get completion improvements
- structural changes to rpm completion

* Sat Apr  6 2002 Ian Macdonald <ian@caliban.org>
- various fixes to urpmi function names to make them officially valid
- rpm would wrongly attempt group query completion or uninstalled package
  completion under certain circumstances

* Thu Apr  4 2002 Ian Macdonald <ian@caliban.org>
- add lftp and autorpm completion
- minor enhancements to route completion
- add compressed files (.Z) to the list that gv and ggv will complete on
- add .m3u to list of extensions that xmms et al can complete on
- clean up grep argument quoting throughout the code
- rpm group completion (rpm -qg) was very buggy
- make entire code base bash 2.04 compatible
- add which to list of commands that complete on commands
- fix bug in umount completion that mangled returned paths
- cvs completion now checks remote repository for checked-out files on
  'cvs diff' if $COMP_CVS_REMOTE is defined
- ./configure completion now only returns parameter hints if
  $COMP_CONFIGURE_HINTS is defined
- update FAQ section of README

* Tue Apr  2 2002 Ian Macdonald <ian@caliban.org>
- add long option completion for netstat
- add renice(8) completion
- fix and enhancements for dpkg-reconfigure completion
- sudo and other commands that perform command completion weren't performing
  correctly when wildcards in their parameters were expanded
- 'cvs commit' now defaults to local file completion
- silence remote completion errors in scp completion

* Sun Mar 31 2002 Ian Macdonald <ian@caliban.org>
- fix escaping issues in _command()
- fixes to _ant(), _java() and _urpmi()
- simplification of _rpm()
- rpm now only returns options if user attempts completion on a '-'
- simplify cd completion by checking for CDPATH at start
- fix quoting bug in _cd()
- don't turn relative paths into absolute ones for people who don't use CDPATH
- insmod completion now deals with gzipped modules (Mandrake)
- fixes to urpmi completion

* Thu Mar 28 2002 Ian Macdonald <ian@caliban.org>
- in _longopt(), don't call _expand() directly, since it's called indirectly
  later via _filedir(). This fixes an eval error.
- various improvements to dpkg completion
- _cd(): more work to remove duplicates from list of completions
- fakeroot completes just like sudo
- fix slowdown in _querybts()
- fix parameter bug in _querybts() and _reportbug()
- add parameter escapes to _java()

* Tue Mar 26 2002 Ian Macdonald <ian@caliban.org>
- tar completion now supports more switches for bzip compression
- chown completion now uses ':' as user:group separator
- ncftp and mount completion now compatible with FreeBSD
- _ncftp() now handles comments in /etc/shells properly
- dpkg completion now handles -r|--remove|--purge
- add completion for dpkg-reconfigure
- time now also completes on commands

* Sun Mar 24 2002 Ian Macdonald <ian@caliban.org>
- kill and killall completion now also work on FreeBSD

* Fri Mar 22 2002 Ian Macdonald <ian@caliban.org>
- move p4 completion to contrib directory
- rpm completion now handles verification of uninstalled packages
- one-liners for various editors to avoid completion on binaries
- realplay now also handles .smi and .smil files
- timidity and playmidi complete on .mid and .midi files

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
- better Perforce completion
- _command meta-command completion
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
