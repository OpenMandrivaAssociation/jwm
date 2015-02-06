Name:		jwm
Summary:	Lightweight X11 Window Manager
Version:	2.1.0
Release:	2
License:	GPL
Group:		Graphical desktop/Other
URL:		http://joewing.net/programs/jwm/
Source:		http://joewing.net/programs/jwm/releases/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		jwm-destdir.patch
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xpm)

%description
JWM is a window manager for the X11 Window System. JWM is written in C and uses
only Xlib at a minimum. The following libraries can also be used if available:

* libXext for the shape extension
* libXext for the render extension
* libXmu for drawing rounded windows (shape extension also needed)
* libXinerama for Xinerama support
* libXpm for XPM backgrounds and icons
* libjpeg for JPEG backgrounds and icons
* libpng for PNG backgrounds and icons
* libxft for antialiased and true type fonts
* libfribidi for right-to-left language support

JWM supports MWM and Extended Window Manager Hints (EWMH).

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x --enable-debug
%make
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/xsessions
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/xsessions/

%files
%doc LICENSE README todo.txt
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/system.jwmrc
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/%{name}.*

