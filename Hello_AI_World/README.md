# [Hello AI World](https://github.com/dusty-nv/jetson-inference)
  
Welcome to the [Hello AI World](https://github.com/dusty-nv/jetson-inference) project! [This repository](https://github.com/dusty-nv/jetson-inference) demonstrates basic AI applications on the Nvidia Jetson platform. This is a comprehensive guide however we will focus on the key setup to make sure your Nvidia Jetson developer tools are working well.

There are two primary methods to run pre-trained models and applications in this repository:

1. Running the Docker container
2. Building the project from source

You will become familiar with both methods throughout this curriculum, as they are commonly used in open-source Nvidia Jetson projects.

## 1. Docker Setup

- Follow the [Running Docker Container](./Running_Docker.md) guide.
  - This setup will have you run 2 pre-built models including topics in:
    1. Image Classsification
    2. Object Detection
- Docker simplifies dependency management and environment isolation.

## 2. Building from Source

- Follow the [Building the Project from Source](./Building_Source.md) document.
  - This setup will have you run 3 pre-built models including topics in:
    1. [Action Recognition](./Action_Recognition.md)
    2. [Background Removal](./Background_Removal.md)
    3. [Monocular Depth with DepthNet](./Monocular_Depth.md)
- Learn how to configure tools like Nvidia-specific TensorFlow and use CMake for C++ projects.

## Clone the Repository

Now that you have an overview of the project, let's clone the repository to your Jetson device. This will allow you to run the pre-built models and applications.

```bash
# With a new terminal window, clone the repository
git clone --recursive --depth=1 https://github.com/dusty-nv/jetson-inference
cd jetson-inference
```

Great! We are now ready to start running the pre-built models and applications.

Next | [Docker Setup](./Running_Docker.md)  
Previous | [Curriculum Home](../README.md)
