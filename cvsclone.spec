Summary:	Utility to clone CVS repositories over the cvspserver interface
Name:		cvsclone
Version:	0.1
Release:	1
License:	GPL v2
Source0:	http://repo.or.cz/w/cvsclone.git/snapshot/558950ab442bc0551c8c16f8d3d6bc972818a81d.tar.gz#/%{name}.tgz
# Source0-md5:	f678e9cd37f4d2f85466a4e817a108c2
Group:		Development/Languages
URL:		https://samba.org/ftp/tridge/rtc/cvsclone.l
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
As git cvsimport is pretty slow over the wire (and as cvs2git can do a
substantially better job if there are a lot of branches), it is often
better to "clone" a whole CVS repository. Enter cvsclone, written by
Peter Backes.

You can find a few touchups by yours truly here, allowing to pipe the
output of "cvs rlog" into a file, editing the file to fix errors (such
as geniuses who put the cvs log of moved files into a commit message)
and use that file as input instead.

%prep
%setup -qn %{name}

%{__sed} -i -e '
	s,gcc,$(CC),
	s,-g,$(CFLAGS),
' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p cvsclone $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cvsclone
