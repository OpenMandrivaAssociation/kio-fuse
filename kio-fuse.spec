Summary: KIO module for accessing FUSE filesystems
Name: kio-fuse
Version: 5.1.0
Release: 1
Source0:  https://download.kde.org/stable/kio-fuse/kio-fuse-%{version}.tar.xz
#Source0: https://invent.kde.org/system/kio-fuse/-/archive/v%{version}/%{name}-%{version}.tar.xz
URL: https://invent.kde.org/system/kio-fuse
License: GPL
Group: Graphical desktop/KDE

BuildRequires:	ninja
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5DBus)
BuildRequires: pkgconfig(fuse3)
# QT6
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6DBus)
BuildRequires: qt6-qtbase-theme-gtk3

Requires: fuse >= 3
Supplements: dolphin


%description
KIO module for accessing FUSE filesystems.

%prep
%autosetup -p1
%cmake_kde5  \
              -G Ninja
cd ..

export CMAKE_BUILD_DIR=build-qt6 
%cmake \
	      -DBUILD_WITH_QT6:BOOL=ON \
        -G Ninja

%build
%ninja_build -C build

%ninja_build -C build-qt6

%install
%ninja_install -C build

%ninja_install -C build-qt6

%post
%systemd_user_post kio-fuse.service

%postun
%systemd_user_postun kio-fuse.service

%files
%{_tmpfilesdir}/kio-fuse-tmpfiles.conf
%{_libdir}/libexec/kio-fuse
%{_datadir}/dbus-1/services/org.kde.KIOFuse.service
%{_userunitdir}/kio-fuse.service
