Name:           extension-manager
Version:        0.6.5
Release:        2%{?dist}
Summary:        A utility for browsing and installing GNOME Shell Extensions
License:        GPL-3.0-or-later
URL:            https://github.com/mjakeman/extension-manager
Source0:        extension-manager-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  meson gcc blueprint-compiler desktop-file-utils libappstream-glib
BuildRequires:  pkgconfig(gtk4) pkgconfig(libadwaita-1) pkgconfig(libsoup-3.0) pkgconfig(json-glib-1.0)
Requires:       gtk4 libadwaita

%description
A native tool for browsing, installing, and managing GNOME Shell Extensions.

%prep
%autosetup

mkdir -p subprojects
git clone https://github.com/ianlancetaylor/libbacktrace.git subprojects/backtrace

%build
%meson -Dforce_fallback_for=backtrace
%meson_build

%install
%meson_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%license COPYING
%{_bindir}/extension-manager
%{_metainfodir}/*.xml
%{_datadir}/applications/com.mattjakeman.ExtensionManager.desktop
%{_datadir}/glib-2.0/schemas/com.mattjakeman.ExtensionManager.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/com.mattjakeman.ExtensionManager.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.mattjakeman.ExtensionManager-symbolic.svg

%changelog
* Sat Dec 20 2025 Giovanni <giovannirafanan609@gmail.com> - 0.6.5
- bundled libbacktrace correctly, as it not available in Fedora repo's