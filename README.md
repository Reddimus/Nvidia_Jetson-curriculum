# Nvidia Jetson Nano Curriculum

This is a curriculum for learning how to use the Nvidia Jetson platform. This will link to various resource, tutorials, and projects that will help you get started with the Jetson platform.

## Getting Started

Visit the [NVIDIA Jetson Nano Getting Started Page](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit) and follow the first 4 instructions:

1. [Introduction](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#intro)
2. [Prepare for Setup](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#prepare)
3. [Write Image to the microSD Card](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write)
4. [Setup and First Boot](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#setup)

    - During this step you may be asked to setup the power management mode. Choose the default option (5W) for now.

### Setting Up Tools

1. **Install Git**  
   - Update your package list:

     ```bash
     sudo apt-get update
     ```

   - Install Git:

     ```bash
     sudo apt-get install git
     ```

   - Configure Git:

     ```bash
     git config --global user.name "Your Name"
     git config --global user.email "youremail@example.com"
     ```

2. **Install Nvidia Jetson Visual Studio Code**  
   Follow the guide on the [GitHub repository](https://github.com/JetsonHacksNano/installVSCode):
   - Clone the repository and run:

     ```bash
     ./installVSCodeWithPython.sh
     ```

   - After installation, launch VSCode (or type `code` in the terminal), click on the profile/settings icon in the bottom left corner. Then:
     - Sync your settings
     - Turn on cloud extensions
     - Configure your GitHub account
   - Install the following extensions: `Python Extension Pack`, `C/C++ Extension Pack`, and `GitHub Pull Requests`

3. **Setup VNC**  
   VNC provides remote desktop access via the RFB protocol, allowing you to control your Jetson from your laptop. Follow [this guide](https://developer.nvidia.com/embedded/learn/tutorials/vnc-setup) for detailed instructions.

> NOTE: Avoid scripts and commands that use `sudo apt upgrade` as it may break the Jetson platform.

## Projects

1. [Hello AI World](./Hello_AI_World/README.md)
2. []()

Throughout these projects, you will demo pre-trained models. It is strongly recommended to multi task and run different models in parallel with multiple terminal windows to save time.
