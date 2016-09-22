Name:       libksba
Summary:    X.509 library
Version:    1.3.5
Release:    1
Group:      System/Libraries
License:    GPLv2+ or LGPLv3+
URL:        http://www.gnupg.org/
Source0:    libksba-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  gawk
BuildRequires:  libgpg-error-devel >= 1.2
BuildRequires:  bison
BuildRequires:  texinfo

%description
KSBA is a library designed to build software based on the X.509 and
CMS protocols.

%package devel
Summary:    Development headers and libraries for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
License:    GPLv3+ and (GPLv2+ or LGPLv3+)

%description devel
A library designed to build software based on the X.509 and
CMS protocols.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
./autogen.sh
%configure --disable-static --enable-maintainer-mode
make

%install
rm -rf %{buildroot}
%make_install 

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING.GPLv2
%{_libdir}/lib*.so.*

%files devel
%doc AUTHORS ChangeLog COPYING COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv3 NEWS README* THANKS TODO VERSION
%defattr(-,root,root,-)
# GPLv3+
%{_bindir}/ksba-config
# GPLv2+ or LGPLv3+
%{_libdir}/lib*.so
%{_includedir}/*
# GPLv3+
%{_datadir}/aclocal/*
%{_infodir}/*

