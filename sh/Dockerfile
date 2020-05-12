FROM cern/cc7-base
MAINTAINER Mayank Sharma (mayank.sharma@cern.ch)

ENV SIMPLE_CONFIG_DIR=/etc/simple_grid
ENV HTCONDOR_CE_CONFIG_DIR=/etc/condor-ce
ENV HTCONDOR_CONFIG_DIR=/etc/condor

RUN yum install -y wget
RUN wget https://research.cs.wisc.edu/htcondor/yum/RPM-GPG-KEY-HTCondor
RUN rpm --import RPM-GPG-KEY-HTCondor
WORKDIR /etc/yum.repos.d/
RUN wget https://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-stable-rhel7.repo
RUN yum -y install condor htcondor-ce-condor

## Install certs, CRLs ##
RUN wget -O /etc/yum.repos.d/EGI-third-party.repo \
	http://repository.egi.eu/community/software/third.party.distribution/1.0/releases/repofiles/sl-6-x86_64.repo
RUN echo -e 'protect=1\npriority=1' >> /etc/yum.repos.d/EGI-third-party.repo
RUN yum -y install \
    http://repository.egi.eu/sw/production/umd/4/sl6/x86_64/updates/umd-release-4.1.3-1.el6.noarch.rpm
RUN yum -y --skip-broken install fetch-crl globus-rsl empty-ca-certs ca-policy-egi-core

## Install utils ##
RUN yum install -y vim less

## net tools ##
RUN yum install -y iproute openssh openssh-server openssh-clients openssl-libs
RUN yum install -y net-tools

## default users ##
RUN adduser -m condor_user

ENV container docker
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \
systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;
WORKDIR /etc/condor/
VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/init"]