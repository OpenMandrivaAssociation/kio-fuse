Summary: KIO module for accessing FUSE filesystems
Name: kio-fuse
Version: 5.1.0
Release: 2
Source0:  https://download.kde.org/stable/kio-fuse/kio-fuse-%{version}.tar.xz
#Source0: https://invent.kde.org/system/kio-fuse/-/archive/v%{version}/%{name}-%{version}.tar.xz
URL: https://invent.kde.org/system/kio-fuse
License: GPL
Group: Graphical desktop/KDE

BuildRequires: ninja
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5DBus)
BuildRequires: pkgconfig(fuse3)

Requires: fuse >= 3
Supplements: dolphin


%description
KIO module for accessing FUSE filesystems.

%prep
%autosetup -p1
%cmake_kde5  \
              -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%post
%systemd_user_post kio-fuse.service

%postun
%systemd_user_postun kio-fuse.service

%files
%{_tmpfilesdir}/kio-fuse-tmpfiles.conf
%{_libdir}/libexec/kio-fuse
%{_datadir}/dbus-1/services/org.kde.KIOFuse.service
%{_userunitdir}/kio-fuse.service
