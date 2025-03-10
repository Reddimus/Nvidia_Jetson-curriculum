# [Building the Project from Source](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md)

This guide explains how to build Hello AI World project(s) from source. Building from source lets you tailor the setup to your needs and ensures compatibility with Nvidia's optimized libraries, including a specialized version of TensorFlow for the Jetson platform and CMake for C++ projects.

## Prerequisites

Before building, exit any Docker container (`exit`) and install dependencies:

```bash
sudo apt-get update
sudo apt install -y build-essential ninja-build
sudo apt-get install git cmake libpython3-dev python3-numpy
```

## Build Steps

Now follow [this guide](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md) to build the project(s) from source starting from the `Python Development Packages` section.

If the `build/aarch64/bin` already exists with many python files, you can skip the `Building the Project from Source` section and proceed to the next section.

Alternatively, you can use the following commands to build the project(s) from source assuming the `Hello_AI_World` repository is already cloned:

```bash
git submodule update --init
mkdir build
cd build
```

```bash
cmake ../
make -j$(nproc)
sudo make install
```

```bash
sudo ldconfig
```

Now that we have built the project(s) from source, we can run the same test as before but let's run different projects instead.

Next | [Action Recognition](Action_Recognition.md)  
Previous | [Running Docker Container](./Running_Docker.md)
