# revision 15878
# category Package
# catalog-ctan /fonts/fourier-GUT
# catalog-date 2008-12-13 14:57:21 +0100
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-fourier
Version:	1.3
Release:	4
Summary:	Using Utopia fonts in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/fourier-GUT
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fourier.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fourier.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fourier.source.tar.xz
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
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-alt-black.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-alt-bold.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-alt-boldita.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-alt-ita.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-alt-semi.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-alt-semiita.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-alt.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-bb.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-mcl.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-mex.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-ml.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-mlb.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-mlit.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-mlitb.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-ms.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-orns.afm
%{_texmfdistdir}/fonts/map/dvips/fourier/fourier-utopia-expert.map
%{_texmfdistdir}/fonts/map/dvips/fourier/fourier.map
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt-black.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt-bold-sl.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt-boldita.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt-ita.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt-semi-sl.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt-semi.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt-semiita.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt-sl.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-bb.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-mcl.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-mex.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-ml.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-mlb.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-mlit.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-mlitb.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-ms.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-orns.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futb8c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futb8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futb9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futb9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futb9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbi8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbi9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbi9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbi9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbo8c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbo8t.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbo8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbo9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbo9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbo9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futboorn.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futborn.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futc8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futc9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futc9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futc9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futcorn.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futmi.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futmib.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futmii.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futmiib.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futr8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futr8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futr9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futr9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futr9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futrc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futrc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futrc9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futrc9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futrd8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futrd8t.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futri8c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futri8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futri8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futri9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futri9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futri9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futro8c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futro8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futro8t.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futro8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futro9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futro9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futro9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futroorn.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futrorn.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futs8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futs8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futs9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futs9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futs9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsc9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsc9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsi8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsi9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsi9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsi9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futso8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futso8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futso9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futso9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futso9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsoorn.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsorn.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsy.tfm
%{_texmfdistdir}/fonts/type1/public/fourier/fourier-alt-black.pfb
%{_texmfdistdir}/fonts/type1/public/fourier/fourier-alt-bold.pfb
%{_texmfdistdir}/fonts/type1/public/fourier/fourier-alt-boldita.pfb
%{_texmfdistdir}/fonts/type1/public/fourier/fourier-alt-ita.pfb
%{_texmfdistdir}/fonts/type1/public/fourier/fourier-alt-semi.pfb
%{_texmfdistdir}/fonts/type1/public/fourier/fourier-alt-semiita.pfb
%{_texmfdistdir}/fonts/type1/public/fourier/fourier-alt.pfb
%{_texmfdistdir}/fonts/type1/public/fourier/fourier-bb.pfb
%{_texmfdistdir}/fonts/type1/public/fourier/fourier-mcl.pfb
%{_texmfdistdir}/fonts/type1/public/fourier/fourier-mex.pfb
%{_texmfdistdir}/fonts/type1/public/fourier/fourier-ml.pfb
%{_texmfdistdir}/fonts/type1/public/fourier/fourier-mlb.pfb
%{_texmfdistdir}/fonts/type1/public/fourier/fourier-mlit.pfb
%{_texmfdistdir}/fonts/type1/public/fourier/fourier-mlitb.pfb
%{_texmfdistdir}/fonts/type1/public/fourier/fourier-ms.pfb
%{_texmfdistdir}/fonts/type1/public/fourier/fourier-orns.pfb
%{_texmfdistdir}/fonts/vf/public/fourier/futb8c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futb8t.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futb9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futb9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futb9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbc8t.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbi8c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbi8t.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbi9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbi9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbi9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbo8c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbo8t.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbo9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbo9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbo9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futboorn.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futborn.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futc9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futc9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futc9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futcorn.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futmi.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futmib.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futmii.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futmiib.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futr8c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futr8t.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futr9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futr9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futr9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futrc8t.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futrc9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futrc9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futrd8t.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futri8c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futri8t.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futri9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futri9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futri9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futro8c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futro8t.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futro9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futro9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futro9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futroorn.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futrorn.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futs9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futs9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futs9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsc9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsc9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsi9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsi9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsi9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futso9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futso9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futso9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsoorn.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsorn.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsy.vf
%{_texmfdistdir}/tex/latex/fourier/fmlfutm.fd
%{_texmfdistdir}/tex/latex/fourier/fmlfutmi.fd
%{_texmfdistdir}/tex/latex/fourier/fmsfutm.fd
%{_texmfdistdir}/tex/latex/fourier/fmxfutm.fd
%{_texmfdistdir}/tex/latex/fourier/fourier-orns.sty
%{_texmfdistdir}/tex/latex/fourier/fourier.sty
%{_texmfdistdir}/tex/latex/fourier/t1futj.fd
%{_texmfdistdir}/tex/latex/fourier/t1futs.fd
%{_texmfdistdir}/tex/latex/fourier/t1futx.fd
%{_texmfdistdir}/tex/latex/fourier/ts1futj.fd
%{_texmfdistdir}/tex/latex/fourier/ts1futs.fd
%{_texmfdistdir}/tex/latex/fourier/ts1futx.fd
%{_texmfdistdir}/tex/latex/fourier/ufuts.fd
%_texmf_updmap_d/fourier
%doc %{_texmfdistdir}/doc/fonts/fourier/README
%doc %{_texmfdistdir}/doc/fonts/fourier/fourier-doc-en.pdf
%doc %{_texmfdistdir}/doc/fonts/fourier/fourier-doc-en.tex
%doc %{_texmfdistdir}/doc/fonts/fourier/fourier-orns.pdf
%doc %{_texmfdistdir}/doc/fonts/fourier/fourier-orns.tex
#- source
%doc %{_texmfdistdir}/source/fonts/fourier/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/fourier <<EOF
Map fourier-utopia-expert.map
Map fourier.map
EOF


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 752087
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 718497
- texlive-fourier
- texlive-fourier
- texlive-fourier
- texlive-fourier

