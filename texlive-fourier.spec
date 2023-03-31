Name:		texlive-fourier
Version:	61937
Release:	2
Summary:	Using Utopia fonts in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/fourier-GUT
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fourier.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fourier.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex

%description
Fourier-GUTenberg is a LaTeX typesetting system which uses
Adobe Utopia as its standard base font. Fourier-GUTenberg
provides all complementary typefaces needed to allow Utopia
based TeX typesetting, including an extensive mathematics set
and several other symbols. The system is absolutely stand-
alone: apart from Utopia and Fourier, no other typefaces are
required. The fourier fonts will also work with Adobe Utopia
Expert fonts, which are only available for purchase. Utopia is
a registered trademark of Adobe Systems Incorporated.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/fourier
%{_texmfdistdir}/fonts/map/dvips/fourier
%{_texmfdistdir}/fonts/opentype/public/fourier
%{_texmfdistdir}/fonts/tfm/public/fourier
%{_texmfdistdir}/fonts/type1/public/fourier
%{_texmfdistdir}/fonts/vf/public/fourier
%{_texmfdistdir}/tex/latex/fourier
%_texmf_updmap_d/fourier
%doc %{_texmfdistdir}/doc/fonts/fourier

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/fourier <<EOF
Map fourier-utopia-expert.map
Map fourier.map
EOF
