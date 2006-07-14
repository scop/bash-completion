Name:		bash-completion
Version:	20060301
Release:	alt03

Summary:	bash-completion offers programmable completion for bash
License:	GPL
Group:		Shells
URL:		http://www.caliban.org/bash/

Source0:	http://www.caliban.org/files/bash/%name-%version.tar.bz2
Source1:	bash-completion.sh
Patch0:	bash-completion-20050103-alt-rsync.patch.gz

Requires:	bash >= 2.05
BuildArch:	noarch

%description
bash-completion is a collection of shell functions that take advantage
of the programmable completion feature of bash 2.04 and later.

%prep
%setup -q -n bash_completion
%patch0 -p0

%install
%__install -d %buildroot%_sysconfdir/bash_completion.d
%__install bash_completion %buildroot%_sysconfdir

%__mkdir_p %buildroot%_sysconfdir/profile.d/
install -p -m755 -D %SOURCE1 $RPM_BUILD_ROOT%_sysconfdir/profile.d/%name.sh

%files
%doc README Changelog contrib BUGS
%_sysconfdir/bash_completion
%dir %_sysconfdir/bash_completion.d
%attr(0755,root,root) %_sysconfdir/profile.d/%name.sh


%changelog
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

