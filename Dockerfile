FROM ubuntu:19.04

WORKDIR /root

# coloring syntax for headers
ARG CYAN='\033[0;36m'
ARG NO_COLOR='\033[0m'

# install python3.7
RUN echo "\n${CYAN}SETUP PYTHON3.7${NO_COLOR}"; \
    apt update && \
    apt install -y \
    python3.7 \
    python3-dev

# install pyopenvdb C/C++ dependencies
COPY dist-packages/* /usr/local/lib/python3.7/dist-packages/
COPY pyopenvdb.so /usr/lib/python3.7/

# link pyopenvdb.so dependencies
ENV LD_LIBRARY_PATH='/usr/local/lib/python3.7/dist-packages'
