#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : bluedevil
Version  : 5.19.1
Release  : 40
URL      : https://download.kde.org/stable/plasma/5.19.1/bluedevil-5.19.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.19.1/bluedevil-5.19.1.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.19.1/bluedevil-5.19.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.1
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
BuildRequires : kded-dev
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
%setup -q -n bluedevil-5.19.1
cd %{_builddir}/bluedevil-5.19.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592339070
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1592339070
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bluedevil
cp %{_builddir}/bluedevil-5.19.1/COPYING %{buildroot}/usr/share/package-licenses/bluedevil/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/bluedevil-5.19.1/COPYING.LIB %{buildroot}/usr/share/package-licenses/bluedevil/01a6b4bf79aca9b556822601186afab86e8c4fbf
pushd clr-build
%make_install
popd
%find_lang bluedevil
%find_lang plasma_applet_org.kde.plasma.bluetooth

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bluedevil-sendfile
/usr/bin/bluedevil-wizard

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.bluedevilsendfile.desktop
/usr/share/applications/org.kde.bluedevilwizard.desktop
/usr/share/bluedevilwizard/pin-code-database.xml
/usr/share/knotifications5/bluedevil.notifyrc
/usr/share/kservices5/bluedeviladapters.desktop
/usr/share/kservices5/bluedevildevices.desktop
/usr/share/kservices5/bluedevilglobal.desktop
/usr/share/kservices5/bluetooth.protocol
/usr/share/kservices5/obexftp.protocol
/usr/share/kservices5/plasma-applet-org.kde.plasma.bluetooth.desktop
/usr/share/metainfo/org.kde.plasma.bluetooth.appdata.xml
/usr/share/mime-packages/bluedevil-mime.xml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/BluetoothApplet.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/CompactRepresentation.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/DeviceItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/FullRepresentation.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/Header.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/MediaPlayerItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/SwitchButton.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/Toolbar.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/logic.js
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/metadata.json
/usr/share/remoteview/bluetooth-network.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kcm_bluedeviladapters.so
/usr/lib64/qt5/plugins/kcm_bluedevildevices.so
/usr/lib64/qt5/plugins/kcm_bluedevilglobal.so
/usr/lib64/qt5/plugins/kf5/kded/bluedevil.so
/usr/lib64/qt5/plugins/kio_bluetooth.so
/usr/lib64/qt5/plugins/kio_obexftp.so
/usr/lib64/qt5/qml/org/kde/plasma/private/bluetooth/libbluetoothplugin.so
/usr/lib64/qt5/qml/org/kde/plasma/private/bluetooth/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bluedevil/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/bluedevil/4cc77b90af91e615a64ae04893fdffa7939db84c

%files locales -f bluedevil.lang -f plasma_applet_org.kde.plasma.bluetooth.lang
%defattr(-,root,root,-)

