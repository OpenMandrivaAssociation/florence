Name:           florence
Version:        0.5.1
Release:        %mkrel 1
Summary:        Extensible scalable on-screen virtual keyboard

Group:          System/X11
License:        GPLv2+ and GFDL
URL:            http://florence.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		florence-0.5.0-nullcallback.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:    gtk2-devel
BuildRequires:    libxml2-devel
BuildRequires:    libglade2-devel
BuildRequires:    at-spi-devel
BuildRequires:    librsvg2-devel
BuildRequires:    cairo-devel
BuildRequires:    libgnome2-devel
BuildRequires:    libGConf2-devel
BuildRequires:    desktop-file-utils
BuildRequires:    scrollkeeper
BuildRequires:    intltool
BuildRequires:    libnotify-devel
#BuildRequires:    libpanelappletmm-devel
BuildRequires:    gnome-doc-utils
BuildRequires:    libxtst-devel
%if %mdvver >= 201100
#Not yet. We want Florence to be in Main but at-spi2-core is in Contrib now
#BuildRequires:    at-spi2-core-devel
%endif

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
%patch0 -p1 -b .nullcallbackfix

rm -f gconf-refresh
ln -sf /bin/true gconf-refresh

sed -i 's|Icon=%{name}.svg|Icon=%{name}|g' data/%{name}.desktop.in.in


%build
%configure \
      --without-panelapplet \
      --without-xrecord \
      --without-notification \
      --disable-schemas-install
%make


%install
rm -rf %{buildroot}

%makeinstall_std

desktop-file-install \
        --delete-original \
        --remove-category="Application" \
        --add-category="Utility" \
        --dir=%{buildroot}%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/%{name}.desktop

mkdir -p %{buildroot}%{_datadir}/pixmaps/ 

install -p -m 0644 data/%{name}.svg \
    %{buildroot}%{_datadir}/pixmaps/%{name}.svg

%find_lang %{name}


%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=$(gconftool-2 --get-default-source)
    gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
fi


%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=$(gconftool-2 --get-default-source)
    gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
fi

%post
scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :

export GCONF_CONFIG_SOURCE=$(gconftool-2 --get-default-source)
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :

%postun
scrollkeeper-update -q || :

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING COPYING-DOCS NEWS README 
%{_datadir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.*
%{_datadir}/gnome/help/%{name}/
%{_datadir}/omf/%{name}/
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_datadir}/pixmaps/%{name}.svg

