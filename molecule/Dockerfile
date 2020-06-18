FROM centos:8

LABEL maintainer "@irix_jp"

RUN dnf update -y && \
    dnf install -y glibc-all-langpacks gcc make git sudo which tree jq && \
    dnf install -y epel-release && dnf install -y crudini && \
    dnf module install -y python36:3.6/common && \
    dnf module install -y python36:3.6/build && \
    alternatives --set python /usr/bin/python3 && \
    dnf clean all

RUN dnf install -y 'dnf-command(config-manager)' && \
    dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo && \
    dnf install -y docker-ce-cli && \
    dnf clean all

RUN pip3 install -U pip setuptools && \
    pip install ansible ansible-lint yamllint yq 'molecule[docker]' python-gitlab && \
    pip install "https://github.com/ansible/awx/archive/12.0.0.tar.gz#egg=awxkit&subdirectory=awxkit"

RUN ansible-galaxy collection install awx.awx
