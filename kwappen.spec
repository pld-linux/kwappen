Summary:	KDE3 board game
Summary(pl.UTF-8):	Gra planszowa dla KDE3
Name:		kwappen
Version:	1.1.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.lcs-chemie.de/%{name}-%{version}.tar.gz
# Source0-md5:	8e21df6cbebc9d6e847d7e4317d2c324
Patch0:		%{name}-am.patch
URL:		http://www.lcs-chemie.de/kwappen_eng.htm
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        /usr/share/doc/kde/HTML

%description
KWappen is a colorful KDE3 board game.

%description -l pl.UTF-8
KWappen jest kolorowa grą planszową dla KDE3.

%prep
%setup -q
%patch -P0 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Games/Board/*
%{_datadir}/apps/* # specify excplicit dirs here (to avoid packaging kde dirs)
%{_pixmapsdir}/*/*/*/*
