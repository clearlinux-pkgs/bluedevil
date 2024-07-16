#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v16
# autospec commit: b858a2a
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : bluedevil
Version  : 6.1.3
Release  : 110
URL      : https://download.kde.org/stable/plasma/6.1.3/bluedevil-6.1.3.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.1.3/bluedevil-6.1.3.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.1.3/bluedevil-6.1.3.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
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
BuildRequires : gnupg
BuildRequires : kcoreaddons-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kjobwidgets-dev
BuildRequires : knotifications-dev
BuildRequires : kservice-dev
BuildRequires : ksvg-dev
BuildRequires : libplasma-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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


%package doc
Summary: doc components for the bluedevil package.
Group: Documentation

%description doc
doc components for the bluedevil package.


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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n bluedevil-6.1.3
cd %{_builddir}/bluedevil-6.1.3
pushd ..
cp -a bluedevil-6.1.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1721143757
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1721143757
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bluedevil
cp %{_builddir}/bluedevil-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/bluedevil/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/bluedevil-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/bluedevil/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/bluedevil-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/bluedevil/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/bluedevil-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/bluedevil/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/bluedevil-%{version}/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/bluedevil/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/bluedevil-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/bluedevil/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/bluedevil-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/bluedevil/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/bluedevil-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/bluedevil/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/bluedevil-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/bluedevil/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/bluedevil-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/bluedevil/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/bluedevil-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/bluedevil/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/bluedevil-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/bluedevil/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang bluedevil
%find_lang kcm_bluetooth
%find_lang plasma_applet_org.kde.plasma.bluetooth
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/bluedevil-sendfile
/V3/usr/bin/bluedevil-wizard
/usr/bin/bluedevil-sendfile
/usr/bin/bluedevil-wizard

%files data
%defattr(-,root,root,-)
/usr/share/applications/kcm_bluetooth.desktop
/usr/share/applications/org.kde.bluedevilsendfile.desktop
/usr/share/applications/org.kde.bluedevilwizard.desktop
/usr/share/bluedevilwizard/pin-code-database.xml
/usr/share/knotifications6/bluedevil.notifyrc
/usr/share/metainfo/org.kde.plasma.bluetooth.appdata.xml
/usr/share/mime-packages/bluedevil-mime.xml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/CompactRepresentation.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/DeviceItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/FullRepresentation.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/MediaPlayerItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/Toolbar.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.bluetooth/metadata.json
/usr/share/qlogging-categories6/bluedevil.categories
/usr/share/remoteview/bluetooth-network.desktop

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kcontrol/bluedevil/index.cache.bz2
/usr/share/doc/HTML/ca/kcontrol/bluedevil/index.docbook
/usr/share/doc/HTML/en/kcontrol/bluedevil/bluetooth-add.png
/usr/share/doc/HTML/en/kcontrol/bluedevil/bluetooth-configure.png
/usr/share/doc/HTML/en/kcontrol/bluedevil/bluetooth-kcm.png
/usr/share/doc/HTML/en/kcontrol/bluedevil/bluetooth-phone.png
/usr/share/doc/HTML/en/kcontrol/bluedevil/bluetooth-tray.png
/usr/share/doc/HTML/en/kcontrol/bluedevil/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol/bluedevil/index.docbook
/usr/share/doc/HTML/en/kcontrol/bluedevil/list-remove.png
/usr/share/doc/HTML/en/kcontrol/bluedevil/network-connect.png
/usr/share/doc/HTML/en/kcontrol/bluedevil/network-disconnect.png
/usr/share/doc/HTML/es/kcontrol/bluedevil/index.cache.bz2
/usr/share/doc/HTML/es/kcontrol/bluedevil/index.docbook
/usr/share/doc/HTML/it/kcontrol/bluedevil/index.cache.bz2
/usr/share/doc/HTML/it/kcontrol/bluedevil/index.docbook
/usr/share/doc/HTML/nl/kcontrol/bluedevil/index.cache.bz2
/usr/share/doc/HTML/nl/kcontrol/bluedevil/index.docbook
/usr/share/doc/HTML/ru/kcontrol/bluedevil/index.cache.bz2
/usr/share/doc/HTML/ru/kcontrol/bluedevil/index.docbook
/usr/share/doc/HTML/sv/kcontrol/bluedevil/index.cache.bz2
/usr/share/doc/HTML/sv/kcontrol/bluedevil/index.docbook
/usr/share/doc/HTML/tr/kcontrol/bluedevil/index.cache.bz2
/usr/share/doc/HTML/tr/kcontrol/bluedevil/index.docbook
/usr/share/doc/HTML/uk/kcontrol/bluedevil/bluetooth-add.png
/usr/share/doc/HTML/uk/kcontrol/bluedevil/bluetooth-configure.png
/usr/share/doc/HTML/uk/kcontrol/bluedevil/bluetooth-kcm.png
/usr/share/doc/HTML/uk/kcontrol/bluedevil/bluetooth-phone.png
/usr/share/doc/HTML/uk/kcontrol/bluedevil/bluetooth-tray.png
/usr/share/doc/HTML/uk/kcontrol/bluedevil/index.cache.bz2
/usr/share/doc/HTML/uk/kcontrol/bluedevil/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt6/plugins/kf6/kded/bluedevil.so
/V3/usr/lib64/qt6/plugins/kf6/kio/kio_bluetooth.so
/V3/usr/lib64/qt6/plugins/kf6/kio/kio_obexftp.so
/V3/usr/lib64/qt6/plugins/plasma/kcms/systemsettings/kcm_bluetooth.so
/V3/usr/lib64/qt6/qml/org/kde/plasma/private/bluetooth/libbluetoothplugin.so
/usr/lib64/qt6/plugins/kf6/kded/bluedevil.so
/usr/lib64/qt6/plugins/kf6/kio/kio_bluetooth.so
/usr/lib64/qt6/plugins/kf6/kio/kio_obexftp.so
/usr/lib64/qt6/plugins/plasma/kcms/systemsettings/kcm_bluetooth.so
/usr/lib64/qt6/qml/org/kde/plasma/private/bluetooth/bluetoothplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/plasma/private/bluetooth/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/plasma/private/bluetooth/libbluetoothplugin.so
/usr/lib64/qt6/qml/org/kde/plasma/private/bluetooth/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bluedevil/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/bluedevil/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/bluedevil/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/bluedevil/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/bluedevil/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/bluedevil/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/bluedevil/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/bluedevil/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/bluedevil/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f bluedevil.lang -f kcm_bluetooth.lang -f plasma_applet_org.kde.plasma.bluetooth.lang
%defattr(-,root,root,-)

