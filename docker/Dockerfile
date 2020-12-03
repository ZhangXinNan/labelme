<<<<<<< HEAD
FROM ubuntu:xenial

# http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    mkdir -p /etc/sudoers.d && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer
=======
FROM ubuntu:bionic
LABEL maintainer "Kentaro Wada <www.kentaro.wada@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
>>>>>>> upstream/master

RUN \
  apt-get update -qq && \
  apt-get install -qq -y \
    git \
    python3 \
<<<<<<< HEAD
    python3-pip

RUN \
  apt-get install -qq -y \
    python3-matplotlib \
    python3-pyqt5

RUN pip3 install -v git+https://github.com/wkentaro/labelme.git
=======
    python3-pip \
    python3-matplotlib \
    python3-pyqt5 \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install -U pip setuptools wheel

RUN python3 -m pip install -v git+https://github.com/wkentaro/labelme.git

RUN mkdir /root/workdir

ENV LANG en-US
>>>>>>> upstream/master

WORKDIR /root/workdir
ENTRYPOINT [ "labelme" ]
