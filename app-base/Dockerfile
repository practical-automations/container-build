FROM centos:8

LABEL maintainer "@irix_jp"

RUN dnf update -y && \
    dnf install -y glibc-all-langpacks gcc make git sudo which tree jq openssh-server openssh-clients && \
    dnf module install -y python36:3.6/common && \
    dnf module install -y python36:3.6/build && \
    alternatives --set python /usr/bin/python3 && \
    dnf module install -y mariadb:10.3/client && \
    dnf module install -y mariadb:10.3/server && \
    dnf module install -y nginx:1.16/common && \
    dnf clean all

RUN pip3 install -U pip setuptools 
