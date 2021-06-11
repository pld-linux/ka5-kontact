%define		kdeappsver	21.04.2
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kontact
Summary:	kontact
Name:		ka5-%{kaname}
Version:	21.04.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	7f076a9cde6c4bd330e4e12bc4ef9613
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5Positioning-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5WebChannel-devel >= 5.11.1
BuildRequires:	Qt5WebEngine-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-grantleetheme-devel >= %{kdeappsver}
BuildRequires:	ka5-kontactinterface-devel >= %{kdeappsver}
BuildRequires:	ka5-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka5-libkdepim-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kontact is the integrated solution to your personal information
management (PIM) needs. It combines well-known KDE applications like
KMail, KOrganizer and KAddressBook into a single interface to provide
easy access to mail, scheduling, address book and other PIM
functionality.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kontact
%ghost %{_libdir}/libkontactprivate.so.5
%attr(755,root,root) %{_libdir}/libkontactprivate.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kontact.so
%{_desktopdir}/org.kde.kontact.desktop
%{_datadir}/config.kcfg/kontact.kcfg
%{_iconsdir}/hicolor/128x128/apps/kontact.png
%{_iconsdir}/hicolor/16x16/apps/kontact.png
%{_iconsdir}/hicolor/22x22/apps/kontact.png
%{_iconsdir}/hicolor/32x32/apps/kontact.png
%{_iconsdir}/hicolor/48x48/apps/kontact.png
%{_iconsdir}/hicolor/64x64/apps/kontact.png
%{_iconsdir}/hicolor/scalable/apps/kontact.svg
%attr(755,root,root) %{_datadir}/kconf_update/kontact-15.08-kickoff.sh
%{_datadir}/kconf_update/kontact.upd
%{_datadir}/kservices5/kontactconfig.desktop
%{_datadir}/messageviewer/about/default/introduction_kontact.html
%{_datadir}/messageviewer/about/default/loading_kontact.html
%{_datadir}/metainfo/org.kde.kontact.appdata.xml
%{_datadir}/dbus-1/services/org.kde.kontact.service
%{_datadir}/qlogging-categories5/kontact.categories
%{_datadir}/qlogging-categories5/kontact.renamecategories
