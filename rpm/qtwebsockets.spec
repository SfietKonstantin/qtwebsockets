Name: qt5-qtwebsockets
Summary: Qt WebSockets module
Version: 0.0.0
Release: 1
Group: Qt/Qt
License: LGPLv2.1 with exception or GPLv3
URL: https://qt.gitorious.org/qt/qtwebsockets
Source0: %{name}-%{version}.tar.bz2
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: fdupes
%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the WebSockets module
%package devel
Summary: Qt WebSockets - development files
Group: Qt/Qt
Requires: %{name} = %{version}-%{release}
%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the WebSockets module development files
%package -n qt5-qtdeclarative-import-websockets
Summary: QtQml WebSockets import
Group: Qt/Qt
Requires: %{name} = %{version}-%{release}
Requires: qt5-qtdeclarative
%description -n qt5-qtdeclarative-import-websockets
This package contains the WebSockets import for QtQml
%prep
%setup -q -n %{name}-%{version}
%build
export QTDIR=/usr/share/qt5
touch .git
%qmake5
make %{_smp_mflags}
%install
rm -rf %{buildroot}
%qmake5_install
# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;
#
%fdupes %{buildroot}/%{_includedir}
%post
/sbin/ldconfig
%postun
/sbin/ldconfig
%files
%defattr(-,root,root,-)
%{_libdir}/libQt5WebSockets.so.5
%{_libdir}/libQt5WebSockets.so.5.*
%files devel
%defattr(-,root,root,-)
%{_libdir}/libQt5WebSockets.so
%{_libdir}/libQt5WebSockets.prl
%{_libdir}/pkgconfig/*
%{_includedir}/qt5/*
%{_datadir}/qt5/mkspecs/
%{_libdir}/cmake/
%files -n qt5-qtdeclarative-import-websockets
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/Qt/WebSockets/