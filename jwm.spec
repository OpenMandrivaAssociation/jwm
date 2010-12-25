%define name    jwm
%define version	2.0.1
%define theirversion 2.0.1
%define release %mkrel 1

Name:		%{name}
Summary:	Lightweight X11 Window Manager
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Graphical desktop/Window managers

URL:		http://joewing.net/programs/jwm/
Source:		jwm-%{theirversion}.tar.bz2
Patch1:      jwm-recent-fribidi-headers.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:  libxext-devel
BuildRequires:  libxmu-devel
BuildRequires:  libxinerama-devel
BuildRequires:	libxpm-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libxft-devel
BuildRequires:	libfribidi-devel

%description
JWM is a window manager for the X11 Window System. JWM is written in C and
uses only Xlib at a minimum.

%prep
%setup -q
%patch1 -p1

%build
%configure --enable-png --enable-jpeg --enable-xft --enable-xrender --enable-fribidi --enable-xpm --enable-shape --enable-xinerama

make
%makeinstall BINDIR="%{buildroot}/%{_bindir}" SYSCONF="%{buildroot}/etc" MANDIR="%{buildroot}/%{_mandir}"

%files
%{_bindir}/jwm
%{_mandir}/*
/etc/*


