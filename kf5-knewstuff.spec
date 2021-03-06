%define		kdeframever	5.79
%define		qtver	5.9.0
%define		kfname	knewstuff

Summary:	Framework for downloading and sharing additional application data
Name:		kf5-%{kfname}
Version:	5.79.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	a07e2d9babf366a29656d21e4ee66cf6
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= 5.2.0
BuildRequires:	Qt5DBus-devel >= 5.2.0
BuildRequires:	Qt5Gui-devel >= 5.3.1
BuildRequires:	Qt5Network-devel >= 5.2.0
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-attica-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-karchive-devel >= %{version}
BuildRequires:	kf5-kauth-devel >= %{version}
BuildRequires:	kf5-kbookmarks-devel >= %{version}
BuildRequires:	kf5-kcodecs-devel >= %{version}
BuildRequires:	kf5-kcompletion-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kconfigwidgets-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kdbusaddons-devel >= %{version}
BuildRequires:	kf5-kglobalaccel-devel >= %{version}
BuildRequires:	kf5-kguiaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kiconthemes-devel >= %{version}
BuildRequires:	kf5-kio-devel >= %{version}
BuildRequires:	kf5-kitemviews-devel >= %{version}
BuildRequires:	kf5-kjobwidgets-devel >= %{version}
BuildRequires:	kf5-kservice-devel >= %{version}
BuildRequires:	kf5-ktextwidgets-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf5-kwindowsystem-devel >= %{version}
BuildRequires:	kf5-kxmlgui-devel >= %{version}
BuildRequires:	kf5-solid-devel >= %{version}
BuildRequires:	kf5-sonnet-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
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
%attr(755,root,root) %ghost %{_libdir}/libKF5NewStuff.so.5
%attr(755,root,root) %{_libdir}/libKF5NewStuff.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5NewStuffCore.so.5
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
%attr(755,root,root) %{_libdir}/libKF5NewStuff.so
%attr(755,root,root) %{_libdir}/libKF5NewStuffCore.so
%{qt5dir}/mkspecs/modules/qt_KNewStuff.pri
%{_libdir}/qt5/mkspecs/modules/qt_KNewStuffCore.pri
