FROM ubuntu:18.04

WORKDIR /root

# coloring syntax for headers
ARG CYAN='\033[0;36m'
ARG NO_COLOR='\033[0m'

# install python3.7
RUN echo "\n${CYAN}SETUP PYTHON3.7${NO_COLOR}"; \
    apt update && \
    apt install -y \
        libpython3.7 \
        software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt update && \
    apt install -y python3.7

# install libc6
ADD http://archive.ubuntu.com/ubuntu/pool/main/g/glibc/libc6_2.29-0ubuntu2_amd64.deb .
RUN echo "\n${CYAN}SETUP LIBC6${NO_COLOR}"; \
    dpkg -i libc6_2.29-0ubuntu2_amd64.deb && \
    rm -rf libc6_2.29-0ubuntu2_amd64.deb

# install pyopenvdb C/C++ dependencies
COPY dist-packages/* /usr/local/lib/python3.7/dist-packages/
COPY pyopenvdb.so /usr/lib/python3.7/

# link pyopenvdb.so dependencies
ENV LD_LIBRARY_PATH='/usr/local/lib/python3.7/dist-packages'
