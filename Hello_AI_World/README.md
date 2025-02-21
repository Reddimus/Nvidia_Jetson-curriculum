# [Hello AI World](https://github.com/dusty-nv/jetson-inference)

This [Hello AI World repository](https://github.com/dusty-nv/jetson-inference) in itself has a comprehensive guide to get you started with Inference. We will be partially following the guide to get you started with the Jetson platform. Please click [here]((https://github.com/dusty-nv/jetson-inference)) to visit the repository.

## Background

`Docker` is heavily used in this repository. `Docker` is a containerization tool that allows you to run applications in isolated environments. Luckily `Docker` is already preinstalled with Nvidia Jetson Nano. Please look at this brief [introduction to Docker](https://docs.docker.com/get-started/docker-overview/) before proceeding and ensure you have a basic understanding of how to navigate the Docker CLI.

`Tensorflow` is a popular open-source machine learning framework developed by Google. It is used for a wide range of tasks such as image classification, object detection, natural language processing, and more.

For the sake of this curriculum, we will be focusing on following system setup in the Hello AI World repository:

1. [Running the Docker Container](./Running_Docker.md)
2. [Building the Project from Source](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md)
    - This will ensure we can build code with tools such as a specialized `Tensorflow` for Nvidia Jetson products and `CMake` for building C++ AI projects on the Jetson platform.
