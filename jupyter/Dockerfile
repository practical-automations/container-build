FROM centos:8

LABEL maintainer "@irix_jp"

ENV JP_CONF_PATH /jupyter/.jupyter

RUN dnf update -y && \
    dnf install -y glibc-all-langpacks gcc make rpm-build git sudo which tree jq autoconf automake libcurl-devel && \
    dnf install -y epel-release && dnf install -y czmq-devel crudini && \
    dnf module install -y python36:3.6/common && \
    dnf module install -y python36:3.6/build && \
    dnf module install -y nodejs:10/common && \
    alternatives --set python /usr/bin/python3 && \
    dnf clean all

RUN dnf install -y 'dnf-command(config-manager)' && \
    dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo && \
    dnf install -y docker-ce-cli && \
    dnf clean all

RUN pip3 install -U pip setuptools && \
    pip install ansible ansible-lint yamllint yq 'molecule[docker]' python-gitlab && \
    pip install jupyterlab && \
    pip install "https://github.com/ansible/awx/archive/12.0.0.tar.gz#egg=awxkit&subdirectory=awxkit"

RUN jupyter labextension install -y @jupyterlab/toc

RUN useradd jupyter -m -d /jupyter && \
    mkdir -p /notebooks && \
    chown -R jupyter:jupyter /notebooks && \
    echo 'jupyter ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
    usermod -a -G root jupyter
USER jupyter
WORKDIR /jupyter

COPY --chown=jupyter:jupyter jupyter/assets/.jupyter /jupyter/.jupyter
COPY --chown=jupyter:jupyter jupyter/assets/.ansible.cfg /jupyter/.ansible.cfg
COPY --chown=jupyter:jupyter jupyter/assets/.tower_cli.cfg /jupyter/.tower_cli.cfg
COPY --chown=jupyter:jupyter jupyter/assets/.python-gitlab.cfg /jupyter/.python-gitlab.cfg

RUN ansible-galaxy collection install awx.awx

RUN echo "alias ls='ls --color'" >> /jupyter/.bashrc  && \
    echo "alias ll='ls -alF --color'" >> /jupyter/.bashrc

EXPOSE 8888
CMD ["jupyter", "lab", "--ip", "0.0.0.0", "--port", "8888", "--no-browser"]
