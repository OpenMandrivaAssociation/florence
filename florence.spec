Name:		florence
Version:	0.6.0
Release:	1
Summary:	Extensible scalable on-screen virtual keyboard

Group:		System/X11
License:	GPLv2+ and GFDL
URL:		http://florence.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		florence-0.6.0-desktop.patch
BuildRequires:	intltool
BuildRequires:	rarian
BuildRequires:	pkgconfig(atspi-2)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xtst)

%description
Florence is an extensible scalable virtual keyboard.

It's designed for GNOME but can be used in any DE (without some features).

You need it if you can't use a real hardware keyboard, for
example because you are disabled, your keyboard is broken or
because you use a tablet PC, but you must be able to use a pointing
device (as a mouse, a trackball or a touchscreen).

In GNOME Florence stays out of your way when you don't need it:
it appears on the screen only when you need it. 

A Timer-based auto-click functionality is available 
to help disabled people having difficulties to click.

If you have problems switching keyboard layout (language) in KDE4,
reconfigure layouts in KDE4 settings once and it should work.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x \
      --without-panelapplet \
      --without-xrecord \
      --without-notification
%make


%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING COPYING-DOCS NEWS README 
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.*
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/pixmaps/%{name}.svg
%{_mandir}/man1/%{name}*.1*

%changelog
* Mon Oct 10 2011 Andrey Bondrov <abondrov@mandriva.org> 0.5.1-1mdv2012.0
+ Revision: 704092
- New version 0.5.1
- Update BuildRequires and rebuild

* Sat Sep 10 2011 Andrey Bondrov <abondrov@mandriva.org> 0.5.0-1
+ Revision: 699201
- imported package florence


* Sat Sep 10 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.5.0-1mdv2011.0
- Initial package for Mandriva
- Add patch 1 to fix segfaults on some xkb events
