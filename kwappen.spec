Summary:	KDE3 board game
Summary(pl):	Gra planszowa dla KDE3
Name:		kwappen
Version:	1.1.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.lcs-chemie.de/%{name}-%{version}.tar.gz
Patch0:		%{name}-am.patch
URL:		http://www.lcs-chemie.de/kwappen_eng.htm
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define         _htmldir        /usr/share/doc/kde/HTML

%description
KWappen is a colorful KDE3 board game. 

%description -l pl
KWappen jest kolorowa gr± planszow± dla KDE3.

%prep
%setup -q
%patch0 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"

%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Games/Board/*
%lang(de) %{_datadir}/locale/de/*
%{_datadir}/apps/*
%{_pixmapsdir}/*/*/*/*
%lang(de) %{_docdir}/kde/HTML/de/kwappen
%{_docdir}/kde/HTML/en/kwappen
