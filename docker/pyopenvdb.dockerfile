FROM ubuntu:19.04

WORKDIR /root

# coloring syntax for headers
ARG CYAN='\033[0;36m'
ARG NO_COLOR='\033[0m'

# install apt dependencies
RUN echo "\n${CYAN}INSTALL DEPENDENCIES${NO_COLOR}"; \
    apt update && \
    apt install -y --fix-missing \
        cmake \
        git \
        libblosc-dev \
        libglfw3-dev \
        libilmbase-dev \
        libjemalloc-dev \
        liblog4cplus-dev \
        libopenexr-dev \
        libtbb-dev \
        libz-dev \
        parallel \
        patchelf \
        python3-dev \
        python3-numpy \
        python3-pip \
        unzip \
        zlibc

# install python dependencies
COPY dev_requirements.txt /root/dev_requirements.txt
RUN echo "\n${CYAN}INSTALL PYTHON DEPENDENCIES${NO_COLOR}"; \
    pip3 install -r /root/dev_requirements.txt

ADD https://dl.bintray.com/boostorg/release/1.68.0/source/boost_1_68_0.tar.gz boost.tar.gz
RUN echo "\n${CYAN}DOWNLOAD BOOST${NO_COLOR}"; \
    tar xzf /root/boost.tar.gz && \
    echo "using python"                  >> /root/user-config.jam && \
    echo "    : 3.8"                     >> /root/user-config.jam && \
    echo "    : /usr/bin/python3.8"      >> /root/user-config.jam && \
    echo "    : /usr/include/python3.8" >> /root/user-config.jam && \
    echo "    : /usr/local/lib"          >> /root/user-config.jam && \
    echo "    : <toolset>gcc;"           >> /root/user-config.jam

ENV CC=gcc
ENV CXX=g++

# build boost (this takes forever)
WORKDIR /root/boost_1_68_0
RUN echo "\n${CYAN}BUILD BOOST LIBRARIES${NO_COLOR}"; \
     ./bootstrap.sh \
        --with-python=python3.8 \
        --with-python-version=3.8 \
        --with-python-root=/usr && \
    ./b2

# build pyopenvdb
WORKDIR /root
RUN echo "\n${CYAN}CLONE OPENVDB${NO_COLOR}"; \
    git clone https://github.com/AcademySoftwareFoundation/openvdb.git
WORKDIR /root/openvdb/openvdb
COPY Makefile /root/openvdb/openvdb/Makefile
RUN echo "\n${CYAN}BUILD PYOPENVDB${NO_COLOR}"; \
    make python

# # install pyopenvdb C/C++ dependencies
# RUN echo "\n${CYAN}INSTALL PYOPENVDB${NO_COLOR}"; \
#     cp /root/openvdb/openvdb/libopenvdb.so.7.1.0 /usr/local/lib/python3.8/dist-packages/libopenvdb.so.7.1 && \
#     cp /root/openvdb/openvdb/pyopenvdb.so /usr/lib/python3.8/pyopenvdb.so

# # link pyopenvdb.so dependencies
# ENV LD_LIBRARY_PATH='/usr/local/lib/python3.8/dist-packages'

# RUN echo "\n${CYAN}TEST PYOPENVDB${NO_COLOR}"; \
#     python3.8 -c 'import pyopenvdb'
