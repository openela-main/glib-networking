%define glib2_version 2.55.1

Name:           glib-networking
Version:        2.56.1
Release:        1.1%{?dist}
Summary:        Networking support for GLib

License:        LGPLv2+
URL:            http://www.gnome.org
Source0:        http://download.gnome.org/sources/glib-networking/2.56/%{name}-%{version}.tar.xz

# https://bugzilla.redhat.com/show_bug.cgi?id=1179295
Patch0:         fedora-crypto-policy.patch

BuildRequires:  gettext
BuildRequires:  glib2-devel >= %{glib2_version}
BuildRequires:  libproxy-devel
BuildRequires:  gnutls-devel
BuildRequires:  ca-certificates
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  meson
BuildRequires:  systemd

Requires:       ca-certificates
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gsettings-desktop-schemas

%description
This package contains modules that extend the networking support in
GIO. In particular, it contains libproxy- and GSettings-based
GProxyResolver implementations and a gnutls-based GTlsConnection
implementation.

%package tests
Summary: Tests for the glib-networking package
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The glib-networking-tests package contains tests that can be used to verify
the functionality of the installed glib-networking package.

%prep
%autosetup -p1

%build
%meson -Dinstalled_tests=true
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc NEWS README
%{_libdir}/gio/modules/libgiolibproxy.so
%{_libdir}/gio/modules/libgiognomeproxy.so
%{_libdir}/gio/modules/libgiognutls.so
%{_libexecdir}/glib-pacrunner
%{_datadir}/dbus-1/services/org.gtk.GLib.PACRunner.service
%{_userunitdir}/glib-pacrunner.service

%files tests
%{_libexecdir}/installed-tests/glib-networking
%{_datadir}/installed-tests

%changelog
* Tue Nov 20 2018 Dan Winship <danw@redhat.com> - 2.56.1-1.1
- Use system crypto policy (#1640534)

* Tue May 22 2018 Kalev Lember <klember@redhat.com> - 2.56.1-1
- Update to 2.56.1

* Sun Mar 11 2018 Kalev Lember <klember@redhat.com> - 2.56.0-1
- Update to 2.56.0

* Wed Feb 28 2018 Michael Catanzaro <mcatanzaro@igalia.com> - 2.55.90-1
- Update to 2.55.90

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.55.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Kalev Lember <klember@redhat.com> - 2.55.2-1
- Update to 2.55.2
- Switch to the meson build system

* Wed Nov 01 2017 Kalev Lember <klember@redhat.com> - 2.54.1-1
- Update to 2.54.1

* Wed Sep 13 2017 Kalev Lember <klember@redhat.com> - 2.54.0-1
- Update to 2.54.0

* Tue Aug 15 2017 Kalev Lember <klember@redhat.com> - 2.53.90-1
- Update to 2.53.90
- Rebase fedora-crypto-policy.patch

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.50.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.50.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.50.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 2.50.0-1
- Update to 2.50.0
- Don't set group tags

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 2.49.90-1
- Update to 2.49.90

* Tue Jul  5 2016 Ville Skyttä <ville.skytta@iki.fi> - 2.48.2-3
- Remove scriptlets handled by glib2's file triggers

* Wed Jun 15 2016 Michael Catanzaro <mcatanzaro@gnome.org> - 2.48.2-2
- Comply with Fedora system-wide crypto policy

* Mon May 09 2016 Kalev Lember <klember@redhat.com> - 2.48.2-1
- Update to 2.48.2

* Thu Apr 28 2016 Michael Catanzaro <mcatanzaro@gnome.org> - 2.48.1-1
- Update to 2.48.1
- Add patch for GNOME #765317

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 2.48.0-1
- Update to 2.48.0

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 2.47.90-1
- Update to 2.47.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Kalev Lember <klember@redhat.com> - 2.47.1-1
- Update to 2.47.1

* Mon Oct 12 2015 Kalev Lember <klember@redhat.com> - 2.46.1-1
- Update to 2.46.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 2.46.0-1
- Update to 2.46.0
- Use make_install macro

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.45.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Kalev Lember <kalevlember@gmail.com> - 2.45.1-1
- Update to 2.45.1

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 2.44.0-1
- Update to 2.44.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 2.43.92-1
- Update to 2.43.92

* Tue Mar 03 2015 Kalev Lember <kalevlember@gmail.com> - 2.43.91-1
- Update to 2.43.91
- Use the %%license macro for the COPYING file

* Tue Nov 25 2014 Kalev Lember <kalevlember@gmail.com> - 2.43.1-1
- Update to 2.43.1

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 2.42.0-1
- Update to 2.42.0

* Mon Sep 15 2014 Kalev Lember <kalevlember@gmail.com> - 2.41.92-1
- Update to 2.41.92

* Thu Sep  4 2014 Vadim Rutkovsky <vrutkovs@redhat.com> - 2.41.4-3
- Build installed tests

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.41.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 2.41.4-1
- Update to 2.41.4

* Tue Jun 24 2014 Richard Hughes <rhughes@redhat.com> - 2.41.3-1
- Update to 2.41.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.40.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Kalev Lember <kalevlember@gmail.com> - 2.40.1-1
- Update to 2.40.1

* Sat Apr 05 2014 Kalev Lember <kalevlember@gmail.com> - 2.40.0-2
- Update dep versions

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 2.40.0-1
- Update to 2.40.0

* Tue Feb 18 2014 Richard Hughes <rhughes@redhat.com> - 2.39.90-1
- Update to 2.39.90

* Tue Dec 17 2013 Richard Hughes <rhughes@redhat.com> - 2.39.3-1
- Update to 2.39.3

* Mon Nov 25 2013 Richard Hughes <rhughes@redhat.com> - 2.39.1-1
- Update to 2.39.1

* Thu Nov 14 2013 Richard Hughes <rhughes@redhat.com> - 2.38.2-1
- Update to 2.38.2

* Mon Oct 28 2013 Richard Hughes <rhughes@redhat.com> - 2.38.1-1
- Update to 2.38.1

* Tue Sep 24 2013 Kalev Lember <kalevlember@gmail.com> - 2.38.0-1
- Update to 2.38.0

* Fri Aug 09 2013 Kalev Lember <kalevlember@gmail.com> - 2.37.5-1
- Update to 2.37.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.37.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 02 2013 Kalev Lember <kalevlember@gmail.com> - 2.37.2-1
- Update to 2.37.2

* Sat May 04 2013 Kalev Lember <kalevlember@gmail.com> - 2.37.1-1
- Update to 2.37.1

* Tue Apr 16 2013 Richard Hughes <rhughes@redhat.com> - 2.36.1-1
- Update to 2.36.1

* Mon Mar 25 2013 Kalev Lember <kalevlember@gmail.com> - 2.36.0-1
- Update to 2.36.0

* Thu Mar  7 2013 Matthias Clasen <mclasen@redhat.com> - 2.35.9-1
- Update to 2.35.9

* Thu Feb 21 2013 Kalev Lember <kalevlember@gmail.com> - 2.35.8-1
- Update to 2.35.8

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 2.35.6-1
- Update to 2.35.6

* Tue Jan 15 2013 Matthias Clasen <mclasen@redhat.com> - 2.35.4-1
- Update to 2.35.4

* Thu Dec 20 2012 Kalev Lember <kalevlember@gmail.com> - 2.35.3-1
- Update to 2.35.3

* Fri Nov 09 2012 Kalev Lember <kalevlember@gmail.com> - 2.35.1-1
- Update to 2.35.1

* Tue Sep 25 2012 Kalev Lember <kalevlember@gmail.com> - 2.34.0-1
- Update to 2.34.0

* Tue Sep 18 2012 Kalev Lember <kalevlember@gmail.com> - 2.33.14-1
- Update to 2.33.14

* Wed Sep  5 2012 Debarshi Ray <rishi@fedoraproject.org> - 2.33.12-1
- Update to 2.33.12

* Mon Sep  3 2012 Matthias Clasen <mclasen@redhat.com> - 2.33.10-1
- Update to 2.33.10

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.33.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Richard Hughes <hughsient@gmail.com> - 2.33.3-1
- Update to 2.33.3

* Sat May 05 2012 Kalev Lember <kalevlember@gmail.com> - 2.33.2-1
- Update to 2.33.2
- Use --disable-static instead of removing built static libs in %%install

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 2.32.1-1
- Update to 2.32.1

* Wed Mar 28 2012 Richard Hughes <hughsient@gmail.com> - 2.32.0-1
- Update to 2.32.0

* Tue Mar 27 2012 Matthias Clasen <mclasen@redhat.com> - 2.32.0-1
- Update to 2.32.0

* Tue Mar 20 2012 Kalev Lember <kalevlember@gmail.com> - 2.31.22-1
- Update to 2.31.22

* Mon Mar  5 2012 Matthias Clasen <mclasen@redhat.com> - 2.31.20-1
- Update to 2.31.20

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 2.31.16-1
- Update to 2.31.16

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Matthias Clasen <mclasen@redhat.com> - 2.31.6
- Update to 2.31.6

* Mon Nov 21 2011 Matthias Clasen <mclasen@redhat.com> - 2.31.2
- Update to 2.31.2

* Wed Nov  2 2011 Matthias Clasen <mclasen@redhat.com> - 2.31.0
- Update to 2.31.0

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30.1-2
- Rebuilt for glibc bug#747377

* Mon Oct 17 2011 Matthias Clasen <mclasen@redhat.com> - 2.30.1-1
- Update to 2.30.1

* Mon Sep 26 2011 Ray <rstrode@redhat.com> - 2.30.0-1
- Update to 2.30.0

* Mon Sep 19 2011 Matthias Clasen <mclasen@redhat.com> 2.29.92-1
- Update to 2.29.92

* Tue Jul 05 2011 Bastien Nocera <bnocera@redhat.com> 2.29.9-1
- Update to 2.29.9

* Wed Apr 27 2011 Dan Winship <danw@redhat.com> - 2.28.6.1-2
- Require gsettings-desktop-schemas, for GNOME proxy support

* Tue Apr 26 2011 Matthias Clasen <mclasen@redhat.com> - 2.28.6.1-1
- Update to 2.28.6.1

* Mon Apr 25 2011 Matthias Clasen <mclasen@redhat.com> - 2.28.6-1
- Update to 2.28.6

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> - 2.28.5-1
- Update to 2.28.5

* Tue Mar 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.28.4-1
- Update to 2.28.4

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Dan Winship <danw@redhat.com> - 2.27.90-1
- Update to 2.27.90, including TLS support

* Mon Nov  1 2010 Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Thu Oct  7 2010 Matthias Clasen <mclasen@redhat.com> - 2.25.0-1
- Initial packaging
