Name:		texlive-pst-feyn
Version:	48781
Release:	2
Summary:	Draw graphical elements for Feynman diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pst-feyn
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-feyn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-feyn.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
pst-feyn is a set of drawing graphical elements which are used
for Feynman diagrams. The package is based on the macros of the
old package axodraw but uses the capabilities of PSTricks.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pst-feyn
%{_texmfdistdir}/tex/generic/pst-feyn
%{_texmfdistdir}/dvips/pst-feyn
%doc %{_texmfdistdir}/doc/generic/pst-feyn

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
