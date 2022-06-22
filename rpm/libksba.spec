Name:       libksba
Summary:    X.509 library
Version:    1.3.5
Release:    1
License:    GPLv2+ or LGPLv3+
URL:        https://github.com/sailfishos/libksba
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
Requires:   %{name} = %{version}-%{release}
License:    GPLv3+ and (GPLv2+ or LGPLv3+)

%description devel
A library designed to build software based on the X.509 and
CMS protocols.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
Info page for %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
./autogen.sh
%configure --disable-static --enable-maintainer-mode
make

%install
rm -rf %{buildroot}
%make_install 

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
        AUTHORS ChangeLog NEWS README* THANKS TODO VERSION

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING.GPLv2
%{_libdir}/%{name}.so.*

%files devel
%license COPYING COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv3
%defattr(-,root,root,-)
# GPLv3+
%{_bindir}/ksba-config
# GPLv2+ or LGPLv3+
%{_libdir}/%{name}.so
%{_includedir}/*
# GPLv3+
%{_datadir}/aclocal/*

%files doc
%defattr(-,root,root,-)
%{_infodir}/ksba.*
%{_docdir}/%{name}-%{version}
