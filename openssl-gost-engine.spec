Name:	openssl-gost-engine
Version:	
Release:	1%{?dist}
Summary: Loadable module for openssl implementing GOST cryptoalgoritms	

Group:	Libraries/Cryptography	
License: OpenSSL	
URL: https://github.com/gost-engine/engine		
Source0: %{name}-%{version}.tar.bz2	

BuildRequires: cmake, openssl-devel	
Requires: openssl-libs	

%description

This package contains openssl module with software implementation of GOST cryptoalgorithms.

%prep
%setup -q


%build
cmake .
make %{?_smp_mflags}


%install
install -d -m 755 %{buildroot}%{_libdir}/engines-1.1
install -c -m 755 bin/gost.so %{buildroot}%{_libdir}/engines-1.1

%files
%doc README.gost
%doc README.md
%dir %{_libdir}/engines-1.1
%{_libdir}/engines-1.1/gost.so

%changelog

* Wed Aug  2 2017 Victor Wagner <vitus@wagner.pp.ru>
- initial release

