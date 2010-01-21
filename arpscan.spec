Summary:	Very simple ARP scanner
Summary(pl.UTF-8):	Prosty skaner ARP
Name:		arpscan
Version:	0.10
Release:	1
License:	GPL v2
Group:		Networking/Admin
Source0:	http://wizard.ae.krakow.pl/~jb/arpscan/%{name}-%{version}.tar.gz
# Source0-md5:	960addcbb4051ef2d1c3d9ff0562f09e
Source1:	http://standards.ieee.org/regauth/oui/oui.txt
# Source1-md5:	10dffbf4706f1ba00a0883b70ab88dfa
URL:		http://wizard.ae.krakow.pl/~jb/arpscan/
BuildRequires:	gawk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Arpscan is a utility that scans local network using ARP protocol and
reports alive hosts. Program is designed for Linux.

%description -l pl.UTF-8
Arpscan jest narzędziem skanującym sieć lokalną korzystając z 
protokołu ARP i wypisującym aktywne komputery. Program przeznaczony
jest dla Linuksa.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DVER=\$(VERSION) -DOUI=\$(OUI)" \
	LDFLAGS="%{rpmldflags}" \
	OUI=%{_datadir}/%{name}/oui

gawk -f oui.awk %{SOURCE1} >oui

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}
install -D oui $RPM_BUILD_ROOT%{_datadir}/%{name}/oui

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/arpscan
%{_datadir}/%{name}
