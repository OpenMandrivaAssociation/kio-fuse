%define date 20251004

Summary: KIO module for accessing FUSE filesystems
Name: kio-fuse
Version: 5.1.1~%{date}
Release: 1
#Source0:  https://download.kde.org/stable/kio-fuse/kio-fuse-%{version}.tar.xz
#Source0: https://invent.kde.org/system/kio-fuse/-/archive/v%{version}/%{name}-%{version}.tar.xz
Source0: https://invent.kde.org/system/kio-fuse/-/archive/master/kio-fuse-master.tar.bz2?ref_type=heads#/kio-fuse-%{date}.tar.xz
URL: https://invent.kde.org/system/kio-fuse
License: GPL
Group: Graphical desktop/KDE

BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6CoreTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WidgetsTools)
BuildRequires: cmake(Qt6Test)
BuildRequires: pkgconfig(fuse3)

BuildSystem: cmake
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption: -DBUILD_WITH_QT6:BOOL=ON

Requires: fuse >= 3
Supplements: dolphin

%description
KIO module for accessing FUSE filesystems.

%files
%{_tmpfilesdir}/kio-fuse-tmpfiles.conf
%{_libdir}/libexec/kio-fuse
%{_datadir}/dbus-1/services/org.kde.KIOFuse.service
%{_userunitdir}/kio-fuse.service
