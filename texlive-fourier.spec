%global tl_name fourier
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4
Release:	%{tl_revision}.1
Summary:	Using Utopia fonts in LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/fourier-GUT
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fourier.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fourier.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Fourier-GUTenberg is a LaTeX typesetting system which uses Adobe Utopia
as its standard base font. Fourier-GUTenberg provides all complementary
typefaces needed to allow Utopia based TeX typesetting, including an
extensive mathematics set and several other symbols. The system is
absolutely stand-alone: apart from Utopia and Fourier, no other
typefaces are required. The fourier fonts will also work with Adobe
Utopia Expert fonts, which are only available for purchase. Utopia is a
registered trademark of Adobe Systems Incorporated.

