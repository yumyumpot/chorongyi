#!/bin/bash

set -e

BUILD_DIR=".pixi/build"
mkdir -p "$BUILD_DIR" && cd "$BUILD_DIR"

echo 'Install OpenCV with CUDA support'

PYTHON_EXECUTABLE=$(which python)
PYTHON_PREFIX=$(python -c "import sys; print(sys.prefix)")
PYTHON_SITE_PACKAGES=$(python -c "import site; print(site.getsitepackages()[0])")

echo  $PYTHON_EXECUTABLE
echo  $PYTHON_PREFIX
echo  $PYTHON_SITE_PACKAGES

sudo apt-get update
sudo apt-get install -y build-essential cmake git pkg-config libgtk-3-dev libavcodec-dev libavformat-dev libswscale-dev

git clone https://github.com/opencv/opencv.git || true
git clone https://github.com/opencv/opencv_contrib.git || true

mkdir -p opencv/build && cd opencv/build

cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX="${PYTHON_PREFIX}" \
      -D WITH_CUDA=ON \
      -D WITH_CUDNN=ON \
      -D CUDA_ARCH_BIN=8.9 \
      -D OPENCV_DNN_CUDA=ON \
      -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
      -D BUILD_opencv_python3=ON \
      -D PYTHON3_EXECUTABLE="${PYTHON_EXECUTABLE}" \
      -D PYTHON3_PACKAGES_PATH="${PYTHON_SITE_PACKAGES}" \
      -D BUILD_TESTS=OFF \
      -D BUILD_PERF_TESTS=OFF \
      -D BUILD_EXAMPLES=OFF \
      -D OPENCV_ENABLE_NONFREE=OFF \
      ..

make -j"$(nproc)"
sudo make install

echo 'Build completed.'