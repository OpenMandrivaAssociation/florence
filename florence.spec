%define gstapi 1.0

%define api 1.0
%define major 1
%define libname %mklibname %{name} %{api} %{major}
%define devname %mklibname %{name} -d

Summary:	Extensible scalable on-screen virtual keyboard
Name:		florence
Version:	0.6.3
Release:	3
Group:		System/X11
License:	GPLv2+ and GFDL
Url:		http://florence.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		florence-0.6.0-desktop.patch
Patch1:		florence-0.6.2-linkage.patch
Patch2:		florence-0.6.3-ld-no-undefined.patch
BuildRequires:	intltool
BuildRequires:	rarian
BuildRequires:	pkgconfig(atspi-2)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gstreamer-%{gstapi})
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xtst)

%description
Florence is an extensible scalable virtual keyboard.

It's designed for GNOME but can be used in any DE (without some features).

You need it if you can't use a real hardware keyboard, for example because
you are disabled, your keyboard is broken or because you use a tablet PC,
but you must be able to use a pointing device (as a mouse, a trackball or
a touchscreen).

In GNOME Florence stays out of your way when you don't need it: it appears
on the screen only when you need it.

A Timer-based auto-click functionality is available to help disabled people
having difficulties to click.

If you have problems switching keyboard layout (language) in KDE4, reconfigure
layouts in KDE4 settings once and it should work.

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING COPYING-DOCS NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.*
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/pixmaps/%{name}.svg
%{_mandir}/man1/%{name}*.1*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
Shared library for %{name}.

%files -n %{libname}
%{_libdir}/libflorence-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%{_includedir}/florence-%{api}/florence.h
%{_libdir}/libflorence-%{api}.so
%{_libdir}/pkgconfig/florence-%{api}.pc

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
autoreconf -fi
%configure \
	--without-panelapplet \
	--without-xrecord \
	--without-notification \
	--disable-static
%make_build

%install
%make_install

%find_lang %{name} --with-gnome

