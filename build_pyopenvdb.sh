# relevant links:
#   https://www.openvdb.org/documentation/doxygen/dependencies.html
#   https://github.com/AcademySoftwareFoundation/openvdb
#   https://github.com/mikrosimage/openvdb_dev/blob/master/openvdb/INSTALL
#   https://github.com/lukasgartmair/pyopenvdb_build_guide

apt update
apt install -y \
    clang \
    cmake \
    g++-6 \
    gcc-6 \
    git \
    libblosc-dev \
    libboost-iostreams-dev \
    libboost-numpy-dev \
    libboost-python-dev \
    libboost-system-dev \
    libboost-thread-dev \
    libglfw3-dev \
    libilmbase-dev \
    libjemalloc-dev \
    liblog4cplus-dev \
    libopenexr-dev \
    libtbb-dev \
    libz-dev \
    python3-dev \
    python3-numpy \
    wget \
    zlibc \
    vim \
    parallel

wget https://bootstrap.pypa.io/get-pip.py get-pip.py && \
python3.7 get-pip.py && \
pip3.7 install \
    numpy==1.16.6 \
    blosc

export CC=clang
export CXX=clang++

git clone https://github.com/AcademySoftwareFoundation/openvdb.git
mkdir /root/openvdb/build
cd /root/openvdb/openvdb
# mv /root/openvdb/openvdb/Makefile /root/Makefile.backup
vim Makefile # insert new Makefile here
make

cp /root/openvdb/openvdb/libopenvdb.so.7.1.0 /usr/local/lib/python3.7/dist-packages/libopenvdb.so.7.1
cp /root/openvdb/openvdb/pyopenvdb.so /usr/lib/python3.7/
export LD_LIBRARY_PATH='/usr/local/lib/python3.7/dist-packages'
python3.7 -c 'import pyopenvdb'
