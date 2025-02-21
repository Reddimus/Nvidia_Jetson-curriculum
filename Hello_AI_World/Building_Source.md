# [Building the Project from Source](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md)

This guide explains how to build Hello AI World project(s) from source. Building from source lets you tailor the setup to your needs and ensures compatibility with Nvidia's optimized libraries, including a specialized version of TensorFlow for the Jetson platform and CMake for C++ projects.

## Prerequisites

Before building, exit any Docker container (`exit`) and install dependencies:

```bash
sudo apt-get update
sudo apt install build-essential ninja-build 
sudo apt-get install git cmake libpython3-dev python3-numpy
```

## Build Steps

Now follow [this guide](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md) to build the project(s) from source starting from the `Python Development Packages` section.
