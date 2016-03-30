#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rubytest
Version  : 0.8.1
Release  : 4
URL      : https://rubygems.org/downloads/rubytest-0.8.1.gem
Source0  : https://rubygems.org/downloads/rubytest-0.8.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires : ruby
BuildRequires : rubygem-qed
BuildRequires : rubygem-rdoc

%description
# Rubytest
[Homepage](http://rubyworks.github.com/rubytest) /
[User Guide](http://wiki.github.com/rubyworks/rubytest) /
[Support](http://github.com/rubyworks/rubytest/issues) /
[Development](http://github.com/rubyworks/rubytest)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n rubytest-0.8.1
gem spec %{SOURCE0} -l --ruby > rubygem-rubytest.gemspec

%build
gem build rubygem-rubytest.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
rubytest-0.8.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/rubytest-0.8.1
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/rubytest-0.8.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/.index
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/HISTORY.md
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/README.md
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/demo/01_test.md
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/demo/02_case.md
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/demo/applique/ae.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/demo/applique/rubytest.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/lib/rubytest.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/lib/rubytest.yml
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/lib/rubytest/advice.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/lib/rubytest/autorun.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/lib/rubytest/code_snippet.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/lib/rubytest/config.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/lib/rubytest/core_ext.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/lib/rubytest/core_ext/assertion.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/lib/rubytest/core_ext/exception.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/lib/rubytest/core_ext/file.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/lib/rubytest/core_ext/string.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/lib/rubytest/format/abstract.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/lib/rubytest/format/abstract_hash.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/lib/rubytest/format/dotprogress.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/lib/rubytest/format/test.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/lib/rubytest/recorder.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/lib/rubytest/runner.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/lib/test.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/test/basic_case.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubytest-0.8.1/test/helper.rb
/usr/lib64/ruby/gems/2.3.0/specifications/rubytest-0.8.1.gemspec
