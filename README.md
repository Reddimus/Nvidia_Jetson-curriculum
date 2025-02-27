# Nvidia Jetson Nano Curriculum

This is a curriculum for learning how to use the Nvidia Jetson platform. This will link to various resource, tutorials, and projects that will help you get started with the Jetson platform.

## Getting Started

Visit the [NVIDIA Jetson Nano Getting Started Page](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit) and follow the instructions.

> **Note:** For the Nvidia Jetson **Orin** Developer Kit, refer to the [Initial Setup Guide for Jetson Orin Nano Developer Kit](https://www.jetson-ai-lab.com/initial_setup_jon.html).
> The Nvidia Jetson Nano 2GB Developer Kit may work for some projects, but the 4GB version is recommended.

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

## Projects

1. [Hello AI World](./Hello_AI_World/README.md)
