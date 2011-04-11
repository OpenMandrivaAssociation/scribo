Name: scribo
Summary: Scribo semantic annotation features
Version: 0.2.0
Release: 1
Group:   Graphical desktop/KDE
Epoch:   2
License: LGPL
URL: http://nepomuk.kde.org
# http://websvn.kde.org/trunk/playground/base/nepomuk-kde/
Source: %name-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: soprano-devel >= 4:2.3.71
BuildRequires: kdelibs4-devel >= 2:4.3.80
BuildRequires: kdepimlibs4-devel >= 4.3.80
BuildRequires: kdebase4-runtime-devel >= 1:4.3.80
BuildRequires: kdebase4-workspace-devel >= 2:4.3.80
BuildRequires: kdebase4-devel >= 1:4.3.80
BuildRequires: olena-devel >= 1.0-3
BuildRequires: strigi-devel
BuildRequires: tesseract-devel >= 2.04-4
BuildRequires: shared-desktop-ontologies-devel 
BuildRequires: nepomukextras-devel
Requires: tesseract
Requires: ginkgo
Obsoletes: playground-nepomuk-kde
Obsoletes: nepomuk-kde
Obsoletes: nepomuk-extras < 0.1-1:0.1 
Provides: nepomuk-extras = %{epoch}:%{version}-%{release}

%description
Scribo enhances the KDE desktop with semi-automatic annotation 
capabilities and with cross application activity management. It introduces 
a new way to deal with tasks at the desktop level, transversaly between 
applications. Nepomuk Scribo annotators take advantage of natural language 
processing technologies.  

%files -f %name.lang
%defattr(-,root,root)
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*
%{_kde_datadir}/kde4/*
%{_kde_datadir}/dbus-1/interfaces/org.kde.nepomuk.Scribo.xml
%{_kde_datadir}/dbus-1/interfaces/org.kde.nepomuk.ScriboSession.xml

#---------------------------------------------------------------------------------

%define scribo_major 0
%define libscribo %mklibname scribo %{scribo_major}

%package -n %{libscribo}
Summary: Nepomuk support library
Group: System/Libraries

%description -n %{libscribo}
Nepomuk support library.

%files -n %{libscribo}
%defattr(-,root,root,-)
%{_kde_libdir}/libscribo.so.%{scribo_major}*

#---------------------------------------------------------------------------------

%package devel
Summary: Devel headers for nepomuk support
Group: Development/KDE and Qt
Requires: %{libscribo} = %epoch:%version-%release
Requires: %{name} = %epoch:%version-%release

%description devel
Devel headers for nepomuk playground

%files devel
%defattr(-,root,root,-)
%_kde_includedir/scribo
%_kde_libdir/libscribo.so
%_kde_datadir/cmake/Scribo

#---------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%find_lang %name --all-name --with-kde

%clean 
rm -rf %buildroot

