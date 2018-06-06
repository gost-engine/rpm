GOST ENGINE RPM
===============

This repository contain spec files to build rpm package for gost engine.

Separate GOST engine package can be build for systems with openssl 1.1.0 and
above.

We have no plans to support CentOS/RHEL/OracleLinux until they would
release version 8 with appropriate OpenSSl in the base system.

Now this spec files are intended for recent releases of Fedora and,
possible other RPM-based distros which do include OpenSSL 1.1 and above.

You should have installed rpm-build, git, openssl-devel and cmake in order 
to build RPM package

Type make in this directory and it would 

1. Clone gost-engine/engine repository
2. Prepare source tarball
3. Copy it and spec file out into rpm build tree
4. Build RPM
5. Copy it back here.

