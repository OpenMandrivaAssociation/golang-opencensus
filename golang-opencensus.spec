# Bootstrap for google.golang.org/api
%bcond_with bootstrapping
# Run tests in check section
%bcond_without check

%global goipath         go.opencensus.io
%global forgeurl        https://github.com/census-instrumentation/opencensus-go
Version:                0.18.0

%global common_description %{expand:
OpenCensus Go is a Go implementation of OpenCensus, a toolkit for collecting 
application performance and behavior monitoring data. Currently it consists 
of three major components: tags, stats, and tracing.}

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        A stats collection and distributed tracing framework
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/openzipkin/zipkin-go/model)
BuildRequires: golang(github.com/openzipkin/zipkin-go/reporter)
BuildRequires: golang(github.com/prometheus/client_golang/prometheus)
BuildRequires: golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires: golang(golang.org/x/net/context)
%if %{without bootstrapping}
BuildRequires: golang(google.golang.org/api/support/bundler)
%endif
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: golang(google.golang.org/grpc/codes)
BuildRequires: golang(google.golang.org/grpc/grpclog)
BuildRequires: golang(google.golang.org/grpc/metadata)
BuildRequires: golang(google.golang.org/grpc/stats)
BuildRequires: golang(google.golang.org/grpc/status)
%if %{with check}
BuildRequires: golang(github.com/google/go-cmp/cmp)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup
%if %{with bootstrapping}
rm -rf exporter/stackdriver/*.go
rm -rf exporter/jaeger
%endif


%install
%goinstall "trace/trace_go11.go"


%if %{with check}
%check
# Fails on i686, armv7hl
%gochecks -d zpages
%endif



%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md AUTHORS


%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.18.0-1
- Release 0.18.0

* Tue Jul 17 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.14.0-1
- Bump to 0.14.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.13.0-1
- Bump to 0.13.0

* Mon Apr 23 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.0-3
- Unbootstrap

* Thu Mar 22 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.0-2
- Fix bootstrap

* Thu Mar 22 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.0-1
- First package for Fedora

