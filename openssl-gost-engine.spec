Name:	openssl-gost-engine
Version:	
Release:	1%{?dist}
Summary: Loadable module for openssl implementing GOST cryptoalgoritms	

Group:	Libraries/Cryptography	
License: OpenSSL	
URL: https://github.com/gost-engine/engine		
Source0: %{name}-%{version}.tar.bz2	

BuildRequires: cmake, openssl-devel	>= %{?rhel:1:}1.1
Requires: openssl-libs	


%description

This package contains openssl module with software implementation of GOST cryptoalgorithms.

%package -n gostsum
Summary: utilities to compute GOST hashes
Group: Utilities/Cryptography
License: OpenSSL

%description -n gostsum
Gostsum and gost12sum are utilities, similar to md5sum or sha1sum which computes


%prep
%setup -q


%build
cmake .
make %{?_smp_mflags}


%install
install -d -m 755 %{buildroot}%{_libdir}/engines-1.1
install -c -m 755 bin/gost.so %{buildroot}%{_libdir}/engines-1.1
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -c -m 755 bin/gostsum %{buildroot}%{_bindir}
install -c -m 755 bin/gost12sum %{buildroot}%{_bindir}
install -c -m 644 gostsum.1 %{buildroot}%{_mandir}/man1
install -c -m 644 gost12sum.1 %{buildroot}%{_mandir}/man1

%files
%doc README.gost
%doc README.md
%dir %{_libdir}/engines-1.1
%{_libdir}/engines-1.1/gost.so

%files -n gostsum
%{_bindir}/gostsum
%{_bindir}/gost12sum
%{_mandir}/man1/gostsum.1*
%{_mandir}/man1/gost12sum.1*

%changelog

* Wed Aug  2 2017 Victor Wagner <vitus@wagner.pp.ru>
- initial release

