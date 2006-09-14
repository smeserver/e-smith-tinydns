Summary: e-smith module to configure tinydns
%define name e-smith-tinydns
Name: %{name}
%define version 1.0.0
%define release 03
Version: %{version}
Release: %{release}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-tinydns-1.0.0.ListenIP.patch
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildRequires: e-smith-devtools
BuildArchitectures: noarch
Requires: e-smith-base
Requires: djbdns
Requires: e-smith-lib >= 1.15.1-19
Requires: e-smith-daemontools >= 1.1.0-02
Requires: iptables
Obsoletes: tinydns-initscripts
AutoReqProv: no

%changelog
* Thu Sep 14 2006 Charlie Brady <charlie_brady@mitel.com> 1.0.0-03
- Ensure that ListenIP property is clear in serveronly mode. [SME: 1912]

* Sun Jul 16 2006 Charlie Brady <charlie_brady@mitel.com> 1.0.0-02
- Make dnslog user creation consistent with e-smith-dnscache. [SME: 1688]

* Fri Mar 17 2006 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-01
- Bump stable stream number to 1.0.0 [SME: 1016]

* Tue Mar 14 2006 Charlie Brady <charlie_brady@mitel.com> 0.6.0-01
- Roll stable stream version. [SME: 1016]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 0.5.0-21
- Remove % from (percent)prep in 0.2.0-01 changelog to keep
  mezzanine/RPM happy. No code change.

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 0.5.0-20
- Bump release number only

* Wed Aug 17 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-19]
- Fix access default property for tinydns. [SF: 1246986]
- Add missing control/2 script, possibly required for ip-change
  event handling.

* Tue Aug 16 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-18]
- Add defaults vals for UDPPort and access. [SF: 1246986]

* Mon Jun  6 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-17]
- Add tinydns stats file digester and pretty printer (from
  http://www.campin.net/DNS/tinydns-readstats.txt).

* Mon Jun  6 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-16]
- Add tinydns log file parser program (from
  http://tinydns.org/tinydns-log.pl.txt).

* Wed Apr 13 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-15]
- Work around ordering problem between template expansion and 
  hosts db migration scripts in e-smith-hosts rpm, by calling
  expand-template from tinydns/control/1. TODO: fix properly
  by moving hosts db munging scripts into migrate fragments.

* Mon Apr 11 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-14]
- Switch to updated calling convention for genfilelist.
- Add control/1 script to rebuild data cdb file. Call ./control/1
  from run script, before starting tinydns.
- Use generic_template_expand action in place of tinydns-conf.
  Update e-smith-lib dependency. [MN00064130]
- Remove unused tinydns-restart.

* Tue Mar 15 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-13]
- Remove unnecessary warning from 20tinydns fragment.
  [MN00035059]

* Thu Mar 10 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-12]
- Always create generic hosts for internal IPs

* Thu Jan 20 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-11]
- Still another couple of fixes required to 20tinydns fragment.
  [charlieb MN00035059]

* Wed Jan  5 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-10]
- Further fix and more simplification to 20tinydns fragment.
  [charlieb MN00035059]

* Mon May 31 2004 Michael Soulier <msoulier@e-smith.com>
- [0.5.0-09]
- Beautified 20tinydns fragment, and s/exit/return, as it was killing
  initialize-default-databases processing in post-install.
  [msoulier MN00035059]

* Thu May 20 2004 Mark Knox <markk@e-smith.com>
- [0.5.0-08]
- Don't die in post-install if there's no host record for the server [markk
  MN00034226]

* Tue Jan 13 2004 Michael Soulier <msoulier@e-smith.com>
- [0.5.0-07]
- Changed the name of the DNSAlias property to ReverseDNS, and reversed the
  logic, to improve readability. [msoulier 10890]

* Tue Jan 13 2004 Michael Soulier <msoulier@e-smith.com>
- [0.5.0-06]
- Added logic to key off of DNSAlias property in hosts db, so that the host
  that the PTR record is configured to for reverse DNS lookups can be
  configured, with the server itself defaulting to its proper name, via a
  migration fragment. [msoulier 10890]

* Tue Jan 13 2004 Michael Soulier <msoulier@e-smith.com>
- [0.5.0-05]
- Modified the previous fix to ensure that each IP resolves to only one
  hostname, followed by zero or more aliases. [msoulier 10890]

* Mon Jan 12 2004 Michael Soulier <msoulier@e-smith.com>
- [0.5.0-04]
- Fixed broken reverse DNS lookups for configured hosts. [msoulier 10890]

* Thu Aug 28 2003 Michael Soulier <msoulier@e-smith.com>
- [0.5.0-03]
- Added K* init symlinks for runlevels 0, 1 and 6. [msoulier 9761]

* Thu Aug 21 2003 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-02]
- Replace tinydns-conf-startup action with default db fragments.
  [charlieb 9553]

* Thu Aug 21 2003 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-01]
- Changing version to development stream number - 0.5.0

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [0.4.0-01]
- Changing version to stable stream number - 0.4.0

* Wed Jun 25 2003 Charlie Brady <charlieb@e-smith.com>
- [0.3.5-05]
- Various fixes to 00functions fragment of tinydns data file. Eliminate
  duplicate records for local domain. Fix non-empty output of fragment.
  Re-organise. [charlieb 9169]

* Wed Jun  4 2003 Charlie Brady <charlieb@e-smith.com>
- [0.3.5-04]
- Add Requires header to ensure that %pre script can run. [charlieb 6033]

* Tue Jun  3 2003 Charlie Brady <charlieb@e-smith.com>
- [0.3.5-03]
- Change %pre script which creates required userid, so that it uses
  preferred userids. [charlieb 6033]

* Mon Jun  2 2003 Charlie Brady <charlieb@e-smith.com>
- [0.3.5-02]
- Remove deprecated LocalDomainPrefix handling. [charlieb 4812]

* Thu Apr 10 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.3.5-01]
- Clean out handling of domains now in domains db [gordonr 8097]

* Tue Dec 31 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.3.4-15]
- Also use plain A records for domain entries [gordonr 4058]

* Tue Dec 31 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.3.4-14]
- Use A, not A/PTR records for the hostname aliases [gordonr 4058]

* Tue Dec 31 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.3.4-13]
- Renamed conf-tinydns{,-startup} to tinydns-conf{,-startup} to match
  tinydns-restart [gordonr 4058]

* Tue Dec 31 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.3.4-12]
- Added use esmith::util to tinydns-restart [gordonr 4058]

* Tue Dec 31 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.3.4-11]
- Standardised log/run script with mailfront/qmail/etc. [gordonr 4058]

* Tue Dec 31 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.3.4-10]
- Add missing pipe in genfilelist call so sticky bit preserverved
  on /var/service/tinydns [gordonr 4058]

* Wed Dec  4 2002 Charlie Brady <charlieb@e-smith.com>
- [0.3.4-09]
- Add name server record for local reverse domain. [charlieb 4058]

* Tue Dec  3 2002 Charlie Brady <charlieb@e-smith.com>
- [0.3.4-08]
- Add sticky bit to tinydns service directory, so that svscan starts logging.
  [charlieb 4058]

* Thu Nov 21 2002 Charlie Brady <charlieb@e-smith.com>
- [0.3.4-07]
- Remove bogus reverse DNS records from tinydns/root/data template - the
  correct records are implicit in "=" records. [charlieb 4058]
- Remove A records for generic hostnames from all except the primary domain.
  This change is provisional - we will need to discuss the implications of
  doing this. [charlieb 5805]

* Wed Nov 20 2002 Charlie Brady <charlieb@e-smith.com>
- [0.3.4-06]
- Eliminate use of deprecated db_get_prop from templates for env files.
  [charlieb 4058]

* Wed Nov 20 2002 Charlie Brady <charlieb@e-smith.com>
- [0.3.4-05]
- Create "down" file to prevent scsvan from starting tinydns at initial
  boot time (before it is configured), and add rc7.d symlink to bring
  it up after bootstrap console runs. [charlieb 4058]

* Fri Nov 15 2002 Charlie Brady <charlieb@e-smith.com>
- [0.3.4-04]
- Change default listen address to 127.0.0.1 [charlieb 4058]
- Hide irrelevant output in %pre script.

* Wed Nov 13 2002 Charlie Brady <charlieb@e-smith.com>
- [0.3.4-03]
- Add %pre actions to create dns and dnslog users if required.
- Move root/data templates into correct directory and change
  conf-tinydns action script accordingly.
- Create ROOT environment file required by tinydns
- Create /service symlink.
- Remove requirement on e-smith-packetfilter.
- All changes done to get into running state. [charlieb 4058]

* Tue Nov 12 2002 Charlie Brady <charlieb@e-smith.com>
- [0.3.4-02]
- Add template fragments for local domain tinydns configuration (from
  Zac's e-smith-djbdns contrib). [charlieb 4058]
- Convert all code to use current preferred APIs. [charlieb 4058]
- Update Copyright notices in action scripts.
- Change Copyright RPM header to License.
- Remove masq template fragment as we now use connection tracking.
  [charlieb 4499]

* Tue Jul 23 2002 Charlie Brady <charlieb@e-smith.com>
- [0.3.4-01]
- Convert packet filter fragment to iptables syntax [charlieb 1268]

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.3.3-01]
- RPM rebuild forced by cvsroot2rpm

* Mon Mar 18 2002 Charlie Brady <charlieb@e-smith.com>
- [0.3.2-01]
- Add missing /var/service/tinydns run scripts.
- Add /var/service/tinydns/root directory.

* Mon Mar 18 2002 Charlie Brady <charlieb@e-smith.com>
- [0.3.1-01]
- Rebuild with .../env/IP and .../env/DATASIZE templates included.

* Wed Mar 13 2002 Charlie Brady <charlieb@e-smith.com>
- [0.3.0-01]
- Don't use tinydns-conf, instead include files and templates.
- Move config db init to conf-tinydns-startup.
- Remove tinydns-startup script.
- Reorganise %build to create init symlink, and to build log
  directory.

* Wed Mar 13 2002 Charlie Brady <charlieb@e-smith.com>
- [0.2.2-01]
- Fix '' quoting of variable in restart script.
- Remove SL specific code.

* Wed Mar 13 2002 Charlie Brady <charlieb@e-smith.com>
- [0.2.1-01]
- Test build to verify CVS conversion.

* Wed Mar 13 2002 Charlie Brady <charlieb@e-smith.com>
- [0.2.0-01]
- rollRPM: Rolled version number to 0.2.0-01. Includes patches up to 0.1.5-02.
- added mkdir commands to prep section to create all required empty
  directories.

* Fri Oct 12 2001 Charlie Brady <charlieb@e-smith.com>
- [0.1.5-02]
- Trim changelog previous to 0.1.5-01.

* Fri Oct 12 2001 Charlie Brady <charlieb@e-smith.com>
- [0.1.5-01]
- Rolled version number to 0.1.5-01. Includes patches upto 0.1.4-05.

%description
SME server enhancement to configure and run the tinydns
components of djbdns.

%prep
%setup
%patch0 -p1

%build
perl createlinks
ln -s /var/service/tinydns root/service
mkdir -p root/var/log/tinydns
rm -f %{name}-%{version}-%{release}-filelist

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --dir /var/service/tinydns 'attr(0755,root,root)' \
    --dir /var/service/tinydns/log 'attr(0755,root,root)' \
    --file /var/service/tinydns/run 'attr(0750,root,root)' \
    --file /var/service/tinydns/tinydns-log.pl 'attr(0750,root,root)' \
    --file /var/service/tinydns/tinydns-readstats 'attr(0750,root,root)' \
    --file /var/service/tinydns/control/1 'attr(0750,root,root)' \
    --file /var/service/tinydns/control/2 'attr(0750,root,root)' \
    --file /var/service/tinydns/log/run 'attr(0750,root,root)' \
    --dir /var/log/tinydns 'attr(02755,dnslog,dnslog)' \
    > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/sbin/e-smith/create-system-user dns 53 "Name server" /var/service/tinydns /bin/false
/sbin/e-smith/create-system-user dnslog 411 "DNS log user" /var/log /bin/false
exit 0

%preun

%post

%postun

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
