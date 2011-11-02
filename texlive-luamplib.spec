Name:		texlive-luamplib
Version:	1.08
Release:	1
Summary:	Use LuaTeX's built-in MetaPost interpreter
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/generic/luamplib
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luamplib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luamplib.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luamplib.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package enables the user to directly incorporate MetaPost
diagrams into a document, using LuaTeX's built-in MetaPost
library. The facility is only available in PDF mode.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
