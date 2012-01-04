# revision 24823
# category Package
# catalog-ctan /macros/luatex/generic/luamplib
# catalog-date 2011-12-11 18:44:11 +0100
# catalog-license pd
# catalog-version 1.09
Name:		texlive-luamplib
Version:	1.09
Release:	2
Summary:	Use LuaTeX's built-in MetaPost interpreter
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/generic/luamplib
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luamplib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luamplib.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luamplib.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables the user to directly incorporate MetaPost
diagrams into a document, using LuaTeX's built-in MetaPost
library. The facility is only available in PDF mode.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/luatex/luamplib/luamplib.lua
%{_texmfdistdir}/tex/luatex/luamplib/luamplib.sty
%doc %{_texmfdistdir}/doc/luatex/luamplib/NEWS
%doc %{_texmfdistdir}/doc/luatex/luamplib/README
%doc %{_texmfdistdir}/doc/luatex/luamplib/luamplib.pdf
%doc %{_texmfdistdir}/doc/luatex/luamplib/test-luamplib-latex.tex
%doc %{_texmfdistdir}/doc/luatex/luamplib/test-luamplib-plain.tex
#- source
%doc %{_texmfdistdir}/source/luatex/luamplib/Makefile
%doc %{_texmfdistdir}/source/luatex/luamplib/luamplib.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
