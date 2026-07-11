%global tl_name newcomputermodern
%global tl_revision 79453

Name:		texlive-%{tl_name}
Epoch:		1
Version:	8.1.1
Release:	%{tl_revision}.1
Summary:	Computer Modern fonts including matching non-latin alphabets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/newcomputermodern
License:	gfl gpl3+fe
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newcomputermodern.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newcomputermodern.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a new assembly of Computer Modern fonts including extensions in
many directions for both Latin based languages, non-Latin based
languages and Mathematics, all compatible in style to CM fonts. In
addition to the Regular weight of Computer Modern, it provides a Book
weight for heavier printing. Regarding license: Some fonts are now
distributed under GPL3+FontException+DistributionException in Chapter7
of the GPL. This is explicitly written and described in the License.txt
file and the documentation of the package.

