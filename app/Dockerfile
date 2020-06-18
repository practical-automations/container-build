FROM centos:8

LABEL maintainer "@irix_jp"

RUN dnf update -y && \
    dnf install -y glibc-all-langpacks gcc make rpm-build git sudo which tree jq autoconf automake libcurl-devel && \
    dnf install -y epel-release && \
    dnf module install -y python36:3.6/common && \
    dnf module install -y python36:3.6/build && \
    alternatives --set python /usr/bin/python3 && \
    dnf clean all

RUN pip3 install -U pip setuptools 

EXPOSE 80
