#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hexchat
Version  : 2.10.2
Release  : 1
URL      : https://dl.hexchat.net/hexchat/hexchat-2.10.2.tar.xz
Source0  : https://dl.hexchat.net/hexchat/hexchat-2.10.2.tar.xz
Summary  : Header and path for HexChat plugins
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: hexchat-bin
Requires: hexchat-lib
Requires: hexchat-data
Requires: hexchat-locales
Requires: hexchat-doc
BuildRequires : dbus-dev
BuildRequires : gdk-pixbuf
BuildRequires : gdk-pixbuf-dev
BuildRequires : gettext
BuildRequires : gtk+-dev
BuildRequires : intltool
BuildRequires : openssl-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(libpci)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(python-2.7)
BuildRequires : shared-mime-info

%description
# HexChat [![Build Status](https://travis-ci.org/hexchat/hexchat.png)](https://travis-ci.org/hexchat/hexchat) [![Build Status](http://nekomimi.cloudapp.net:8080/job/hexchat/badge/icon)](http://nekomimi.cloudapp.net:8080/job/hexchat/) [![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/hexchat/hexchat/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

%package bin
Summary: bin components for the hexchat package.
Group: Binaries
Requires: hexchat-data

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
Requires: hexchat-lib
Requires: hexchat-bin
Requires: hexchat-data
Provides: hexchat-devel

%description dev
dev components for the hexchat package.


%package doc
Summary: doc components for the hexchat package.
Group: Documentation

%description doc
doc components for the hexchat package.


%package lib
Summary: lib components for the hexchat package.
Group: Libraries
Requires: hexchat-data

%description lib
lib components for the hexchat package.


%package locales
Summary: locales components for the hexchat package.
Group: Default

%description locales
locales components for the hexchat package.


%prep
%setup -q -n hexchat-2.10.2

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang hexchat

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hexchat

%files data
%defattr(-,root,root,-)
/usr/share/appdata/hexchat.appdata.xml
/usr/share/applications/hexchat.desktop
/usr/share/icons/hicolor/48x48/apps/hexchat.png
/usr/share/icons/hicolor/scalable/apps/hexchat.svg

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/hexchat/plugins/checksum.so
/usr/lib64/hexchat/plugins/doat.so
/usr/lib64/hexchat/plugins/fishlim.so
/usr/lib64/hexchat/plugins/perl.so
/usr/lib64/hexchat/plugins/python.so
/usr/lib64/hexchat/plugins/sysinfo.so

%files locales -f hexchat.lang 
%defattr(-,root,root,-)

