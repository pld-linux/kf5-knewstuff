%define		kdeframever	5.82
%define		qtver	5.14.0
%define		kfname	knewstuff

Summary:	Framework for downloading and sharing additional application data
Name:		kf5-%{kfname}
Version:	5.82.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	c19a7239fc2ed40a6304053438f81e06
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 3.5
BuildRequires:	kf5-attica-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-karchive-devel >= %{version}
BuildRequires:	kf5-kcompletion-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kiconthemes-devel >= %{version}
BuildRequires:	kf5-kio-devel >= %{version}
BuildRequires:	kf5-kitemviews-devel >= %{version}
BuildRequires:	kf5-kpackage-devel >= %{version}
BuildRequires:	kf5-kservice-devel >= %{version}
BuildRequires:	kf5-ktextwidgets-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf5-kxmlgui-devel >= %{version}
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5Core >= %{qtver}
Requires:	Qt5Gui >= %{qtver}
Requires:	Qt5Qml >= %{qtver}
Requires:	Qt5Widgets >= %{qtver}
Requires:	Qt5Xml >= %{qtver}
Requires:	kf5-dirs
Requires:	kf5-attica >= %{version}
Requires:	kf5-karchive >= %{version}
Requires:	kf5-kcompletion >= %{version}
Requires:	kf5-kconfig >= %{version}
Requires:	kf5-kcoreaddons >= %{version}
Requires:	kf5-ki18n >= %{version}
Requires:	kf5-kiconthemes >= %{version}
Requires:	kf5-kio >= %{version}
Requires:	kf5-kitemviews >= %{version}
Requires:	kf5-kpackage >= %{version}
Requires:	kf5-kservice >= %{version}
Requires:	kf5-ktextwidgets >= %{version}
Requires:	kf5-kwidgetsaddons >= %{version}
Requires:	kf5-kxmlgui >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration
Services specification.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Widgets-devel >= %{qtver}
Requires:	Qt5Xml-devel >= %{qtver}
Requires:	cmake >= 3.5
Requires:	kf5-attica-devel >= %{version}
Requires:	kf5-kservice-devel >= %{version}
Requires:	kf5-kxmlgui-devel >= %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}5

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5.lang
%defattr(644,root,root,755)
%doc README.md
%ghost %{_libdir}/libKF5NewStuff.so.5
%attr(755,root,root) %{_libdir}/libKF5NewStuff.so.*.*.*
%ghost %{_libdir}/libKF5NewStuffCore.so.5
%attr(755,root,root) %{_libdir}/libKF5NewStuffCore.so.5.*.*
%{_datadir}/kf5/kmoretools
%{_datadir}/qlogging-categories5/knewstuff.categories
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/newstuff/libnewstuffqmlplugin.so
%dir %{_libdir}/qt5/qml/org/kde/newstuff
%dir %{_libdir}/qt5/qml/org/kde/newstuff/qml
%dir %{_libdir}/qt5/qml/org/kde/newstuff/qml/private
%dir %{_libdir}/qt5/qml/org/kde/newstuff/qml/private/entrygriddelegates
%{_libdir}/qt5/qml/org/kde/newstuff/qml/*.qml
%{_libdir}/qt5/qml/org/kde/newstuff/qml/private/*.qml
%{_libdir}/qt5/qml/org/kde/newstuff/qmldir
%{_libdir}/qt5/qml/org/kde/newstuff/qml/private/entrygriddelegates/*.qml
%attr(755,root,root) %{_bindir}/knewstuff-dialog
%{_datadir}/qlogging-categories5/knewstuff.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KNewStuff3
%{_includedir}/KF5/knewstuff_version.h
%{_includedir}/KF5/knewstuffcore_version.h
%{_includedir}/KF5/knewstuffquick_version.h
%{_libdir}/cmake/KF5NewStuff
%{_libdir}/cmake/KF5NewStuffCore
%{_libdir}/cmake/KF5NewStuffQuick
%{_libdir}/libKF5NewStuff.so
%{_libdir}/libKF5NewStuffCore.so
%{qt5dir}/mkspecs/modules/qt_KNewStuff.pri
%{_libdir}/qt5/mkspecs/modules/qt_KNewStuffCore.pri
