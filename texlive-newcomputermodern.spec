Name:		texlive-newcomputermodern
Version:	61310
Release:	2
Summary:	Computer Modern fonts including matching non-latin alphabets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/newcomputermodern
License:	gfl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newcomputermodern.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newcomputermodern.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newcomputermodern.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a new assembly of Computer Modern fonts including
extensions in many directions for both Latin based languages,
non-Latin based languages and Mathematics, all compatible in
style to CM fonts. In addition to the Regular weight of
Computer Modern, it provides a Book weight for heavier
printing.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/fonts/newcomputermodern
%{_texmfdistdir}/tex/latex/newcomputermodern
%{_texmfdistdir}/fonts/opentype/public/newcomputermodern
%doc %{_texmfdistdir}/doc/fonts/newcomputermodern

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
