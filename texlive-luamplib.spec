%global tl_name luamplib
%global tl_revision 79640

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.42.4
Release:	%{tl_revision}.1
Summary:	Use LuaTeXs built-in MetaPost interpreter
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/luamplib
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luamplib.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luamplib.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luamplib.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enables the user to specify MetaPost diagrams (which may
include colour specifications from the color or xcolor packages) into a
document, using LuaTeX's built-in MetaPost library. The facility is only
available in PDF mode.

