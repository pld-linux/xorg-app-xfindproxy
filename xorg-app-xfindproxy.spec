Summary:	xfindproxy application to locate available X11 proxy services
Summary(pl.UTF-8):	Aplikacja xfindproxy do odnajdywania dostępnych serwisów proxy dla X11
Name:		xorg-app-xfindproxy
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xfindproxy-%{version}.tar.bz2
# Source0-md5:	2fa74c68511ae845f52c2f33e641d0fd
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-proto-xproxymanagementprotocol-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfindproxy application is used to locate available X11 proxy services.

It utilizes the Proxy Management Protocol to communicate with a proxy
manager. The proxy manager keeps track of all available proxy
services, starts new proxies when necessary, and makes sure that
proxies are shared whenever possible.

%description -l pl.UTF-8
Aplikacja xfindproxy służy do odnajdywania dostępnych serwisów proxy
dla X11.

Wykorzystuje protokół Proxy Management Protocol do komunikacji z
zarządcą proxy. Zarządca ten utrzymuje informacje o wszystkich
dostępnych serwisach proxy, uruchamia w razie potrzeby nowe proxy i
zapewnia, że proxy są w miarę możliwości współdzielone.

%prep
%setup -q -n xfindproxy-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xfindproxy
%{_mandir}/man1/xfindproxy.1x*
