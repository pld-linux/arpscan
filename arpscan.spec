Summary:	Very simple ARP scanner
Summary(pl):	Prosty skaner ARP
Name:		arpscan
Version:	0.5
Release:	1
License:	GPL
Group:		Networking/Admin
URL:		http://wizard.ae.krakow.pl/~jb/arpscan/
Source0:	http://wizard.ae.krakow.pl/~jb/arpscan/%{name}-%{version}.tar.gz
# Source0-md5:	681fdb51baa8f52492e2275dafca3307
# http://standards.ieee.org/regauth/oui/oui.txt
Source1:	oui.txt
BuildRequires:	gawk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Arpscan is a utility that scans local network using ARP protocol and
reports alive hosts. Program is designed for Linux.

%description -l pl
Arpscan jest narzêdziem skanuj±cym sieæ lokaln± korzystaj±c z 
protoko³u ARP i wypisuj±cym aktywne komputery. Program przeznaczony
jest dla Linuksa.

%prep
%setup -q

%build
%{__make} \
	CC=%{__cc} \
	CFLAGS="%{rpmcflags} -DVER=\$(VERSION) -DOUI=\$(OUI)" \
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
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/%{name}
