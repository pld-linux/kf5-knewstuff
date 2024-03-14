#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.115
%define		qtver	5.15.2
%define		kfname	knewstuff

Summary:	Framework for downloading and sharing additional application data
Name:		kf5-%{kfname}
Version:	5.115.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	32e234371b5454850f17441d15b5748e
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	kf5-attica-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-karchive-devel >= %{version}
BuildRequires:	kf5-kcompletion-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kdesignerplugin-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kiconthemes-devel >= %{version}
BuildRequires:	kf5-kio-devel >= %{version}
BuildRequires:	kf5-kitemviews-devel >= %{version}
BuildRequires:	kf5-kpackage-devel >= %{version}
BuildRequires:	kf5-kservice-devel >= %{version}
BuildRequires:	kf5-ktextwidgets-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf5-kxmlgui-devel >= %{version}
BuildRequires:	kf5-syndication-devel >= %{version}
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
Requires:	kf5-attica >= %{version}
Requires:	kf5-dirs
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
Requires:	cmake >= 3.16
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
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


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
%{_libdir}/libKF5NewStuff.so.*.*.*
%ghost %{_libdir}/libKF5NewStuffCore.so.5
%{_libdir}/libKF5NewStuffCore.so.5.*.*
%ghost %{_libdir}/libKF5NewStuffWidgets.so.5
%{_libdir}/libKF5NewStuffWidgets.so.5.*.*
%{_datadir}/kf5/kmoretools
%{_datadir}/qlogging-categories5/knewstuff.categories
%{_libdir}/qt5/qml/org/kde/newstuff/libnewstuffqmlplugin.so
%dir %{_libdir}/qt5/qml/org/kde/newstuff
%{_libdir}/qt5/qml/org/kde/newstuff/Action.qml
%{_libdir}/qt5/qml/org/kde/newstuff/Button.qml
%{_libdir}/qt5/qml/org/kde/newstuff/Dialog.qml
%{_libdir}/qt5/qml/org/kde/newstuff/DialogContent.qml
%{_libdir}/qt5/qml/org/kde/newstuff/DownloadItemsSheet.qml
%{_libdir}/qt5/qml/org/kde/newstuff/EntryDetails.qml
%{_libdir}/qt5/qml/org/kde/newstuff/NewStuffItem.qml
%{_libdir}/qt5/qml/org/kde/newstuff/NewStuffList.qml
%{_libdir}/qt5/qml/org/kde/newstuff/Page.qml
%{_libdir}/qt5/qml/org/kde/newstuff/QuestionAsker.qml
%{_libdir}/qt5/qml/org/kde/newstuff/UploadPage.qml
%dir %{_libdir}/qt5/qml/org/kde/newstuff/private
%{_libdir}/qt5/qml/org/kde/newstuff/private/ConditionalLoader.qml
%{_libdir}/qt5/qml/org/kde/newstuff/private/EntryCommentDelegate.qml
%{_libdir}/qt5/qml/org/kde/newstuff/private/EntryCommentsPage.qml
%{_libdir}/qt5/qml/org/kde/newstuff/private/EntryScreenshots.qml
%{_libdir}/qt5/qml/org/kde/newstuff/private/ErrorDisplayer.qml
%{_libdir}/qt5/qml/org/kde/newstuff/private/GridTileDelegate.qml
%{_libdir}/qt5/qml/org/kde/newstuff/private/MessageBoxSheet.qml
%{_libdir}/qt5/qml/org/kde/newstuff/private/Rating.qml
%{_libdir}/qt5/qml/org/kde/newstuff/private/Shadow.qml
%dir %{_libdir}/qt5/qml/org/kde/newstuff/private/entrygriddelegates
%{_libdir}/qt5/qml/org/kde/newstuff/private/entrygriddelegates/BigPreviewDelegate.qml
%{_libdir}/qt5/qml/org/kde/newstuff/private/entrygriddelegates/FeedbackOverlay.qml
%{_libdir}/qt5/qml/org/kde/newstuff/private/entrygriddelegates/ThumbDelegate.qml
%{_libdir}/qt5/qml/org/kde/newstuff/private/entrygriddelegates/TileDelegate.qml
%{_libdir}/qt5/qml/org/kde/newstuff/qmldir
%attr(755,root,root) %{_bindir}/knewstuff-dialog
%{_datadir}/qlogging-categories5/knewstuff.renamecategories
%{_libdir}/qt5/plugins/designer/knewstuffwidgets.so
%{_desktopdir}/org.kde.knewstuff-dialog.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KMoreTools
%{_includedir}/KF5/KNewStuff3
%{_libdir}/cmake/KF5NewStuff
%{_libdir}/cmake/KF5NewStuffCore
%{_libdir}/cmake/KF5NewStuffQuick
%{_libdir}/libKF5NewStuff.so
%{_libdir}/libKF5NewStuffCore.so
%{_libdir}/libKF5NewStuffWidgets.so
%{qt5dir}/mkspecs/modules/qt_KNewStuff.pri
%{_libdir}/qt5/mkspecs/modules/qt_KNewStuffCore.pri
