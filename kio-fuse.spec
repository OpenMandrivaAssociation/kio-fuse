Name: kio-fuse
Version: 5.0.0
Release: 1
Source0: https://invent.kde.org/system/kio-fuse/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Summary: KIO module for accessing FUSE filesystems
URL: https://invent.kde.org/system/kio-fuse
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5DBus)
BuildRequires: pkgconfig(fuse3)
BuildRequires: cmake ninja

%description
KIO module for accessing FUSE filesystems

%prep
%autosetup -p1 -n %{name}-v%{version}
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_prefix}/lib/tmpfiles.d/kio-fuse-tmpfiles.conf
%{_libdir}/libexec/kio-fuse
%{_datadir}/dbus-1/services/org.kde.KIOFuse.service
%{_prefix}/lib/systemd/user/kio-fuse.service
