#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : bluedevil
Version  : 5.25.3
Release  : 69
URL      : https://download.kde.org/stable/plasma/5.25.3/bluedevil-5.25.3.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.25.3/bluedevil-5.25.3.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.25.3/bluedevil-5.25.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: bluedevil-bin = %{version}-%{release}
Requires: bluedevil-data = %{version}-%{release}
Requires: bluedevil-lib = %{version}-%{release}
Requires: bluedevil-license = %{version}-%{release}
Requires: bluedevil-locales = %{version}-%{release}
BuildRequires : bluez-qt-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : extra-cmake-modules-data
BuildRequires : ki18n-dev
BuildRequires : kirigami2-dev
BuildRequires : plasma-framework-dev

%description
BlueDevil runtime dependencies:
-bluez5
-General Bluetooth management
-bluez-obexd
-Be able to "Browse File" aka kio_obexftp
-Be able to "Send Files" (bluedevil-sendfile)
-Be able to receive files

%package bin
Summary: bin components for the bluedevil package.
Group: Binaries
Requires: bluedevil-data = %{version}-%{release}
Requires: bluedevil-license = %{version}-%{release}

%description bin
bin components for the bluedevil package.


%package data
Summary: data components for the bluedevil package.
Group: Data

%description data
data components for the bluedevil package.


%package lib
Summary: lib components for the bluedevil package.
Group: Libraries
Requires: bluedevil-data = %{version}-%{release}
Requires: bluedevil-license = %{version}-%{release}

%description lib
lib components for the bluedevil package.


%package license
Summary: license components for the bluedevil package.
Group: Default

%description license
license components for the bluedevil package.


%package locales
Summary: locales components for the bluedevil package.
Group: Default

%description locales
locales components for the bluedevil package.


%prep
%setup -q -n bluedevil-5.25.3
cd %{_builddir}/bluedevil-5.25.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657635148
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1657635148
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bluedevil
cp %{_builddir}/bluedevil-5.25.3/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/bluedevil/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/bluedevil-5.25.3/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/bluedevil/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/bluedevil-5.25.3/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/bluedevil/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/bluedevil-5.25.3/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/bluedevil/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/bluedevil-5.25.3/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/bluedevil/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/bluedevil-5.25.3/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/bluedevil/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/bluedevil-5.25.3/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/bluedevil/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/bluedevil-5.25.3/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/bluedevil/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/bluedevil-5.25.3/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/bluedevil/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/bluedevil-5.25.3/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/bluedevil/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/bluedevil-5.25.3/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/bluedevil/e458941548e0864907e654fa2e192844ae90fc32
pushd clr-build
%make_install
popd
%find_lang bluedevil
%find_lang kcm_bluetooth
%find_lang plasma_applet_org.kde.plasma.bluetooth

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bluedevil-sendfile
/usr/bin/bluedevil-wizard

%files data
%defattr(-,root,root,-)
/usr/share/applications/kcm_bluetooth.desktop
/usr/share/applications/org.kde.bluedevilsendfile.desktop
/usr/share/applications/org.kde.bluedevilwizard.desktop
/usr/share/bluedevilwizard/pin-code-database.xml
/usr/share/knotifications5/bluedevil.notifyrc
/usr/share/kpackage/kcms/kcm_bluetooth/contents/ui/Device.qml
/usr/share/kpackage/kcms/kcm_bluetooth/contents/ui/General.qml
/usr/share/kpackage/kcms/kcm_bluetooth/contents/ui/main.qml
/usr/share/kservices5/plasma-applet-org.kde.plasma.bluetooth.desktop
/usr/share/metainfo/org.kde.plasma.bluetooth.appdata.xml
/usr/share/mime-packages/bluedevil-mime.xml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/CompactRepresentation.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/DeviceItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/FullRepresentation.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/MediaPlayerItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/Toolbar.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/logic.js
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/metadata.json
/usr/share/qlogging-categories5/bluedevil.categories
/usr/share/remoteview/bluetooth-network.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kf5/kded/bluedevil.so
/usr/lib64/qt5/plugins/kf5/kio/kio_bluetooth.so
/usr/lib64/qt5/plugins/kf5/kio/kio_obexftp.so
/usr/lib64/qt5/plugins/plasma/kcms/systemsettings/kcm_bluetooth.so
/usr/lib64/qt5/qml/org/kde/plasma/private/bluetooth/libbluetoothplugin.so
/usr/lib64/qt5/qml/org/kde/plasma/private/bluetooth/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bluedevil/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/bluedevil/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/bluedevil/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/bluedevil/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/bluedevil/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/bluedevil/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/bluedevil/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/bluedevil/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f bluedevil.lang -f kcm_bluetooth.lang -f plasma_applet_org.kde.plasma.bluetooth.lang
%defattr(-,root,root,-)

