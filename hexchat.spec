#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB3C7CE210DE76DFC (tingping@fedoraproject.org)
#
Name     : hexchat
Version  : 2.14.3
Release  : 33
URL      : https://dl.hexchat.net/hexchat/hexchat-2.14.3.tar.xz
Source0  : https://dl.hexchat.net/hexchat/hexchat-2.14.3.tar.xz
Source1  : https://dl.hexchat.net/hexchat/hexchat-2.14.3.tar.xz.asc
Summary  : Header and path for HexChat plugins
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: hexchat-bin = %{version}-%{release}
Requires: hexchat-data = %{version}-%{release}
Requires: hexchat-lib = %{version}-%{release}
Requires: hexchat-license = %{version}-%{release}
Requires: hexchat-locales = %{version}-%{release}
Requires: hexchat-man = %{version}-%{release}
BuildRequires : appstream-glib
BuildRequires : buildreq-meson
BuildRequires : dbus-dev
BuildRequires : desktop-file-utils
BuildRequires : gdk-pixbuf
BuildRequires : gdk-pixbuf-dev
BuildRequires : gtk+-dev
BuildRequires : intltool
BuildRequires : libnotify-dev
BuildRequires : lua-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : pkgconfig(libcanberra)
BuildRequires : pkgconfig(libpci)
BuildRequires : pkgconfig(libproxy-1.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : python3-dev

%description
# HexChat [![Build Status](http://img.shields.io/travis/hexchat/hexchat/master.svg?style=flat)](https://travis-ci.org/hexchat/hexchat) [![Build Status](https://img.shields.io/appveyor/ci/TingPing/hexchat/master.svg?style=flat)](https://ci.appveyor.com/project/TingPing/hexchat)

%package bin
Summary: bin components for the hexchat package.
Group: Binaries
Requires: hexchat-data = %{version}-%{release}
Requires: hexchat-license = %{version}-%{release}

%description bin
bin components for the hexchat package.


%package data
Summary: data components for the hexchat package.
Group: Data

%description data
data components for the hexchat package.


%package dev
Summary: dev components for the hexchat package.
Group: Development
Requires: hexchat-lib = %{version}-%{release}
Requires: hexchat-bin = %{version}-%{release}
Requires: hexchat-data = %{version}-%{release}
Provides: hexchat-devel = %{version}-%{release}
Requires: hexchat = %{version}-%{release}

%description dev
dev components for the hexchat package.


%package lib
Summary: lib components for the hexchat package.
Group: Libraries
Requires: hexchat-data = %{version}-%{release}
Requires: hexchat-license = %{version}-%{release}

%description lib
lib components for the hexchat package.


%package license
Summary: license components for the hexchat package.
Group: Default

%description license
license components for the hexchat package.


%package locales
Summary: locales components for the hexchat package.
Group: Default

%description locales
locales components for the hexchat package.


%package man
Summary: man components for the hexchat package.
Group: Default

%description man
man components for the hexchat package.


%prep
%setup -q -n hexchat-2.14.3
cd %{_builddir}/hexchat-2.14.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1577381391
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dwith-gtk=true -Dwith-ssl=true -Dwith-dbus=true -Dwith-libproxy=true -Dwith-libnotify=true -Dwith-libcanberra=true -Dwith-python=python3 -Dwith-lua=false -Dwith-perl=false  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/hexchat
cp %{_builddir}/hexchat-2.14.3/COPYING %{buildroot}/usr/share/package-licenses/hexchat/0549952c48f2e28659ed9ea9fb459d9608ddeb62
cp %{_builddir}/hexchat-2.14.3/plugins/fishlim/LICENSE %{buildroot}/usr/share/package-licenses/hexchat/1a7f659398a364d762c133a5d3b19221a18d7e74
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang hexchat

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hexchat

%files data
%defattr(-,root,root,-)
/usr/share/applications/io.github.Hexchat.desktop
/usr/share/dbus-1/services/org.hexchat.service.service
/usr/share/icons/hicolor/48x48/apps/hexchat.png
/usr/share/icons/hicolor/scalable/apps/hexchat.svg
/usr/share/metainfo/io.github.Hexchat.appdata.xml

%files dev
%defattr(-,root,root,-)
/usr/include/hexchat-plugin.h
/usr/lib64/pkgconfig/hexchat-plugin.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/hexchat/plugins/checksum.so
/usr/lib64/hexchat/plugins/fishlim.so
/usr/lib64/hexchat/plugins/python.so
/usr/lib64/hexchat/plugins/sysinfo.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/hexchat/0549952c48f2e28659ed9ea9fb459d9608ddeb62
/usr/share/package-licenses/hexchat/1a7f659398a364d762c133a5d3b19221a18d7e74

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/hexchat.1

%files locales -f hexchat.lang
%defattr(-,root,root,-)

