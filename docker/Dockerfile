FROM ubuntu:20.04

WORKDIR /root

# coloring syntax for headers
ARG CYAN='\033[0;36m'
ARG NO_COLOR='\033[0m'

# update ubuntu and install basic dependencies
RUN echo "\n${CYAN}INSTALL GENERIC DEPENDENCIES${NO_COLOR}"; \
    apt update && \
    apt install -y \
        python3-dev \
        software-properties-common

# install python3.7 and pip
ADD https://bootstrap.pypa.io/get-pip.py get-pip.py
RUN echo "\n${CYAN}SETUP PYTHON3.7${NO_COLOR}"; \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt update && \
    apt install -y python3.7 && \
    python3.7 get-pip.py && \
    rm -rf /root/get-pip.py && \
    apt install libpython3.7

# install pyopenvdb
RUN echo "\n${CYAN}INSTALL PYOPENVDB${NO_COLOR}"; \
    pip3.7 install pyopenvdb;

ENV LD_LIBRARY_PATH /usr/local/lib/python3.7/dist-packages
RUN echo "\n${CYAN}ADD LD_LIBRARY_PATH TO BASHRC${NO_COLOR}"; \
    echo 'export LD_LIBRARY_PATH="/usr/local/lib/python3.7/dist-packages"' >> ~/.bashrc

RUN echo "\n${CYAN}TEST PYOPENVDB${NO_COLOR}"; \
    python3.7 -c "import openvdb as vdb; \
                  grid = vdb.FloatGrid(); \
                  grid.fill(min=(0, 0, 0), max=(1, 1, 1), value=0.5); \
                  grid.convertToPolygons(0.5)"
