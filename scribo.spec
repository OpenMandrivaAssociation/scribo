Name:		scribo
Summary:	Semantic annotation features
Version:	0.2.0
Release:	1
Group:		Graphical desktop/KDE
Epoch:		2
License:	LGPL
URL:		http://nepomuk.kde.org
# http://websvn.kde.org/trunk/playground/base/nepomuk-kde/
Source:		%name-%{version}.tar.bz2
BuildRequires:	soprano-devel
BuildRequires: kdelibs4-devel
BuildRequires: kdepimlibs4-devel
BuildRequires: kdebase4-runtime-devel
BuildRequires: kdebase4-workspace-devel
BuildRequires: kdebase4-devel
BuildRequires: olena-devel
BuildRequires: strigi-devel
BuildRequires: tesseract-devel
BuildRequires: shared-desktop-ontologies-devel 
BuildRequires: nepomukextras-devel
Requires:	tesseract
Requires:	ginkgo

%description
Scribo enhances the KDE desktop with semi-automatic annotation 
capabilities and with cross application activity management. It introduces 
a new way to deal with tasks at the desktop level, transversaly between 
applications. Nepomuk Scribo annotators take advantage of natural language 
processing technologies.  

%files -f %{name}.lang
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*
%{_kde_datadir}/kde4/*
%{_kde_datadir}/dbus-1/interfaces/org.kde.nepomuk.Scribo.xml
%{_kde_datadir}/dbus-1/interfaces/org.kde.nepomuk.ScriboSession.xml

#---------------------------------------------------------------------------------

%define scribo_major 0
%define libscribo %mklibname scribo %{scribo_major}

%package -n %{libscribo}
Summary:	Nepomuk support library
Group:		System/Libraries

%description -n %{libscribo}
Nepomuk support library.

%files -n %{libscribo}
%{_kde_libdir}/libscribo.so.%{scribo_major}*

#---------------------------------------------------------------------------------

%package devel
Summary:	Devel headers for nepomuk support
Group:		Development/KDE and Qt
Requires:	%{libscribo} = %{EVRD}
Requires:	%{name} = %{EVRD}

%description devel
Devel headers for nepomuk playground

%files devel
%{_kde_includedir}/scribo
%{_kde_libdir}/libscribo.so
%{_kde_datadir}/cmake/Scribo

#---------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --all-name --with-kde


%changelog
* Mon Apr 11 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:0.2.0-1
+ Revision: 652520
- Add epoch to ease upgrade
- Rename to scribo
- Update to scribo 0.2.0

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

  + Funda Wang <fwang@mandriva.org>
    - update url

* Thu Jun 24 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.6.3-8mdv2010.1
+ Revision: 548992
- Fix build
- Fix build
- Update it translations

* Wed May 26 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.6.3-7mdv2010.1
+ Revision: 546172
- New version fixes dolphin crash

* Tue May 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.6.3-6mdv2010.1
+ Revision: 546031
- Add a link to ginkgo

* Tue May 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.6.3-5mdv2010.1
+ Revision: 545986
- Add trunk fix for the plasmoid

* Tue May 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.6.3-4mdv2010.1
+ Revision: 545843
- Add it translations
  CCBUG: 59474

* Mon May 24 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.6.3-3mdv2010.1
+ Revision: 545817
- Suggests ginkgo
- Install translations
  CCBUG: 59302
- Add translations
- Add source
- Go back to 0.6.3

* Tue May 11 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.6.3-2mdv2010.1
+ Revision: 544482
- Remove link part of the patch ( merged upstream )
- New tarball ( bug fix release )

* Mon May 10 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.6.3-1mdv2010.1
+ Revision: 544354
- Update tarball with latest changes from strueg
- Fix build
- Add shared-desktop-ontologies-devel as buildrequire
- New version 0.6.3

* Fri Apr 16 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.6.2-1mdv2010.1
+ Revision: 535425
- New version 0.6.2
  	- Remove merged patches
  	- Fix crash when opening firefox ( Bug #57399)

* Tue Mar 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.6.1-3mdv2010.1
+ Revision: 516991
- Add strueg patch that allow to associate several files at once

* Tue Mar 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.6.1-2mdv2010.1
+ Revision: 516963
- Add strueg patch fixing kmozillahelper crash

  + Stéphane Laurière <slauriere@mandriva.com>
    - updated buildrequires

* Wed Dec 23 2009 Stéphane Laurière <slauriere@mandriva.com> 1:0.6.1-1mdv2010.1
+ Revision: 481757
- v0.6.1 developer release - po files merged with trunk

* Tue Dec 01 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.6.0-4mdv2010.1
+ Revision: 472212
- Increase release
- Add patch to fix build against new kdelibs
  Exclude one more file that move to runtime
- Exclude files moved on runtime

* Wed Oct 28 2009 Stéphane Laurière <slauriere@mandriva.com> 1:0.6.0-2mdv2010.0
+ Revision: 459701
- added patch deactivating the OpenCalais plugin by default

* Wed Oct 28 2009 Stéphane Laurière <slauriere@mandriva.com> 1:0.6.0-1mdv2010.0
+ Revision: 459682
- v0.6.0 developer release

* Tue Oct 27 2009 Stéphane Laurière <slauriere@mandriva.com> 1:0.5.8-1mdv2010.0
+ Revision: 459616
- v0.5.8 developer release
- v0.5.7 developer release

* Mon Oct 26 2009 Stéphane Laurière <slauriere@mandriva.com> 1:0.5.6-1mdv2010.0
+ Revision: 459365
- v0.5.6 developer release
- added l10n files

* Fri Oct 23 2009 Stéphane Laurière <slauriere@mandriva.com> 1:0.5.5-1mdv2010.0
+ Revision: 459034
- added simpleannotator patch
- v0.5.5 developer release

* Thu Oct 22 2009 Stéphane Laurière <slauriere@mandriva.com> 1:0.5.4-1mdv2010.0
+ Revision: 458683
- v0.5.4 developer release
- v0.5.4 developer release
- v0.5.3 developer release

* Thu Oct 15 2009 Stéphane Laurière <slauriere@mandriva.com> 1:0.5.2-11mdv2010.0
+ Revision: 457589
- updated plasmoid.desktop

* Wed Oct 14 2009 Stéphane Laurière <slauriere@mandriva.com> 1:0.5.2-10mdv2010.0
+ Revision: 457369
- reverted to 0.5.2 release 10
- v0.5.3 developer release

* Fri Oct 02 2009 Stéphane Laurière <slauriere@mandriva.com> 1:0.5.2-9mdv2010.0
+ Revision: 452739
- nepomuk-scribo-devel: added requires libkresourcetreeview and libtasktreedialog

* Fri Oct 02 2009 Stéphane Laurière <slauriere@mandriva.com> 1:0.5.2-8mdv2010.0
+ Revision: 452695
- added kresourcetreeview and tasktreedialog libraries
- fixed .so installation for tasktreedialog and kresourcetreeview

* Fri Oct 02 2009 Stéphane Laurière <slauriere@mandriva.com> 1:0.5.2-6mdv2010.0
+ Revision: 452689
- removed installation of static libs (*.a)
- kresoucetreeview and tasktreedialog as shared libs

* Fri Oct 02 2009 Stéphane Laurière <slauriere@mandriva.com> 1:0.5.2-2mdv2010.0
+ Revision: 452467
- v0.5.3 developer release

* Mon Sep 28 2009 Stéphane Laurière <slauriere@mandriva.com> 1:0.5.2-1mdv2010.0
+ Revision: 450704
- v0.5.2 developer release
- v0.5.1 developer release

* Fri Sep 25 2009 Stéphane Laurière <slauriere@mandriva.com> 1:0.5-1mdv2010.0
+ Revision: 448536
- v0.5 developer release

* Thu Sep 24 2009 Stéphane Laurière <slauriere@mandriva.com> 1:0.4-1mdv2010.0
+ Revision: 448328
- v0.4 developer release

* Wed Sep 23 2009 Stéphane Laurière <slauriere@mandriva.com> 1:0.3-1mdv2010.0
+ Revision: 447801
- v0.3 developer release

* Mon Sep 21 2009 Helio Chissini de Castro <helio@mandriva.com> 1:0.2-1mdv2010.0
+ Revision: 446792
- New developers 0.2 release.

* Wed Sep 16 2009 Helio Chissini de Castro <helio@mandriva.com> 1:0.1-3mdv2010.0
+ Revision: 443625
- Fix tesseract detection. Testing was relying in wrong library
- Enable tesseract build

* Wed Sep 16 2009 Helio Chissini de Castro <helio@mandriva.com> 1:0.1-2mdv2010.0
+ Revision: 443553
- Missing line in tasktop install

* Wed Sep 16 2009 Helio Chissini de Castro <helio@mandriva.com> 1:0.1-1mdv2010.0
+ Revision: 443364
- Soo tired.. Another issue in the nepomuk-scribo was preventing build in 64 bit installations.
- First release of nepomuk-scribo
- Requested naming change by nepomuk team

* Mon Jul 27 2009 Helio Chissini de Castro <helio@mandriva.com> 0.1-0.pre1.1mdv2010.0
+ Revision: 400622
- First upstream nepomuk-extras package
- Moving to official package from Nepomuk team

* Mon Jan 26 2009 Helio Chissini de Castro <helio@mandriva.com> 4.2.0-0.916937.2mdv2009.1
+ Revision: 333765
- Remove exceptions for link

  + Funda Wang <fwang@mandriva.org>
    - New snapshot
    - use cmake_kde to build

* Fri Jan 23 2009 Nicolas Vigier <nvigier@mandriva.com> 4.2.0-0.915213.4mdv2009.1
+ Revision: 333093
- move libnepomuklinkwidget.so from nepomuk-kde-devel to nepomuk-kde

* Thu Jan 22 2009 Funda Wang <fwang@mandriva.org> 4.2.0-0.915213.3mdv2009.1
+ Revision: 332613
- fix conflicts between main and devel
- Add missing requires on devel package

* Thu Jan 22 2009 Helio Chissini de Castro <helio@mandriva.com> 4.2.0-0.915213.2mdv2009.1
+ Revision: 332594
- New svn build as requested by nepomuk developers

* Sun Nov 02 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.71-0.878903.2mdv2009.1
+ Revision: 299290
- Fix File list
- workaround pb in buildrequires
- Fix stupid typo
- Fix BuildRequires
- New snapshot

* Thu Aug 28 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.0-0.854049.1mdv2009.0
+ Revision: 277009
- New snapshot

* Sun Aug 24 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.0-0.847779.3mdv2009.0
+ Revision: 275589
- Add obsoletes

* Sat Aug 16 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.0-0.847779.2mdv2009.0
+ Revision: 272732
- Fix file list

* Sat Aug 16 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.0-0.847779.1mdv2009.0
+ Revision: 272568
- Add buildrequires
- New snapshot

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu May 22 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.71-0.811361.1mdv2009.0
+ Revision: 210117
- New snapshot
- Rename accordly kde policy

* Thu Feb 21 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.1-1mdv2008.1
+ Revision: 173696
- import playground-nepomuk-kde

