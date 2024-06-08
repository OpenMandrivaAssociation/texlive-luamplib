Name:		texlive-luamplib
Version:	71391
Release:	1
Summary:	Use LuaTeX's built-in MetaPost interpreter
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/generic/luamplib
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luamplib.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luamplib.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luamplib.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
