%def_disable tests

Name: bash-completion
Epoch: 1
Version: 1.99
Release: alt3

Summary: bash-completion offers programmable completion for bash
License: GPL2
Group: Shells
Url: http://%name.alioth.debian.org/

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: %name-%version.tar
# git://git.debian.org/git/bash-completion/bash-completion.git
Source1: rpm-cache.filetrigger
Patch1: %name-20060301-alt-iptables.patch
Patch9: %name-alt-specific.patch
Source2: mutt

%if_enabled tests
BuildRequires: dejagnu tcllib
%endif

Requires: bash >= 2.05
BuildArch: noarch

%description
bash-completion is a collection of shell functions that take advantage
of the programmable completion feature of bash 2.04 and later.

%prep
%setup
%patch1 -p1
%patch9 -p1

%build
./autogen.sh
%configure && make

%check
#FIXME
%if_enabled tests
	pushd test
	./runCompletion
	./runInstall
	./runUnit
	popd
%endif

%install
%makeinstall_std
mv %buildroot%_sysconfdir/{profile.d,bashrc.d}
mkdir -p %buildroot%_rpmlibdir
install -p -m755 %SOURCE1 %buildroot%_rpmlibdir/

#fixes
install -p -m644 %SOURCE2 %buildroot%_sysconfdir/bash_completion.d/
#one line fixes
>> %buildroot%_sysconfdir/bash_completion.d/_alt.fixes

%files
%doc AUTHORS CHANGES README TODO doc/*.txt
%_sysconfdir/bash_completion
%_sysconfdir/bash_completion.d
%_sysconfdir/bashrc.d/bash_completion.sh
%_rpmlibdir/*
%_datadir/%name

%changelog
* Sun Aug 22 2010 Ildar Mulyukov <ildar@altlinux.ru> 1:1.99-alt3
- new GIT version
- bug fixes (closes: #22386, #22443, #23861)

* Tue Dec 29 2009 Ildar Mulyukov <ildar@altlinux.ru> 1:1.99-alt2
- new git version
- %name-20050103-alt-rsync.patch pushed to upstream
- mutt completion from Gentoo bugzilla: http://bugs.gentoo.org/attachment.cgi?id=208607
- quick regression fix for showmount

* Wed Nov 04 2009 Ildar Mulyukov <ildar@altlinux.ru> 1:1.99-alt1
- new version
- patches rebase
- remove unneeded _known_hosts_fix

* Sun Jul 19 2009 Ildar Mulyukov <ildar@altlinux.ru> 1:1.0-alt2
- add rpm filetrigger for updating a rpm cache
- Closes: #15250

* Sat Jul 18 2009 Ildar Mulyukov <ildar@altlinux.ru> 1:1.0-alt1
- new source origin (Closes: #18940)
- Epoch up - new versioning scheme

* Tue Sep 23 2008 Alex Murygin <murygin@altlinux.ru> 20060301-alt06
- patches section typo fix

* Fri Feb 22 2008 Alex Murygin <murygin@altlinux.ru> 20060301-alt05
- moved bash-completion.sh from profile.d to bashrc.d
    (13532, 9273, 9148, 13041, 14606)

* Wed Oct 17 2007 Alex Murygin <murygin@altlinux.ru> 20060301-alt04
- fixed [13041] (bash-completion.sh changed)
- added patch to iptables completion [7382]

* Fri Jul 14 2006 Alex Murygin <murygin@altlinux.ru> 20060301-alt03
- fixed [9148] (bash-completion.sh changed)

* Sat Mar 04 2006 Alex Murygin <murygin@altlinux.ru> 20060301-alt02
- new version

* Wed Jan 18 2006 Alex Murygin <murygin@altlinux.ru> 20050712-alt02
- moved %_sysconfdir/profile.d/%name.sh from spec to source1
- fixing checking bash major version more 2 [8862]

* Thu Jul 14 2005 Alex Murygin <murygin@altlinux.ru> 20050712-alt01
- new version

* Wed Feb 09 2005 Alex Murygin <murygin@altlinux.ru> 20050121-alt01
- new version

* Fri Jan 14 2005 Alex Murygin <murygin@altlinux.ru> 20050112-alt01
- new version

* Mon Jan 10 2005 Alex Murygin <murygin@altlinux.ru> 20050103-alt01
- new version
- added bash-completion-20050103-alt-rsync.patch

* Thu Nov 11 2004 Alex Murygin <murygin@altlinux.ru> 20041017-alt01
- new version

* Thu Aug 12 2004 Alex Murygin <murygin@altlinux.ru> 20040711-alt01
- new version

* Mon Mar 15 2004 Alex Murygin <murygin@altlinux.ru> 20040214-alt01
- new version
- added BUGS to doc

* Thu Jan 08 2004 Alex Murygin <murygin@altlinux.ru> 20040101-alt01
- new version

* Fri Dec 26 2003 Alex Murygin <murygin@altlinux.ru> 20031225-alt01
- new version

* Tue Dec 16 2003 Alex Murygin <murygin@altlinux.ru> 20031215-alt01
- new version

* Sat Dec 06 2003 Alex Murygin <murygin@altlinux.ru> 20031125-alt01
- First build for Sisyphus.

