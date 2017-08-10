# Generated from term-ansicolor-1.3.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name term-ansicolor

Name: rubygem-%{gem_name}
Version: 1.3.2
Release: 1%{?dist}
Summary: Ruby library that colors strings using ANSI escape sequences
Group: Development/Languages
License: GPL-2
URL: http://flori.github.com/term-ansicolor
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
Requires: rubygem(tins) >= 1.0
Requires: rubygem(tins) < 2
# the following BuildRequires are development dependencies
# BuildRequires: rubygem(gem_hadar) >= 1.3.1
# BuildRequires: rubygem(gem_hadar) < 1.4
# BuildRequires: rubygem(simplecov)
# BuildRequires: rubygem(minitest_tu_shim)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
This library uses ANSI escape sequences to control the attributes of terminal
output.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{_bindir}/cdiff
%{_bindir}/decolor
%{_bindir}/colortab
%{_bindir}/term_mandel
%{_bindir}/term_display
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%{gem_instdir}/CHANGES
%license %{gem_instdir}/COPYING
%{gem_instdir}/VERSION
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/term-ansicolor.gemspec
%{gem_instdir}/tests

%changelog
* Thu Sep 29 2016 Rich Megginson <rmeggins@redhat.com> - 1.3.2-1
- Initial package
