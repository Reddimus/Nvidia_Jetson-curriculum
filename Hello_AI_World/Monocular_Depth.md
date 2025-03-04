# [Monocular Depth with DepthNet](https://github.com/dusty-nv/jetson-inference/blob/master/docs/depthnet.md)

In this section, learn how to estimate depth from a image(s) using a pre-trained AI model. Refer to [this guide](https://github.com/dusty-nv/jetson-inference/blob/master/docs/depthnet.md) to follow along.

## Quick Start

Here is a quick run-through of the steps to get through this guide easily:

### Mono Depth on images

Ensure you are in the correct directory (`cd build/aarch64/bin`) before executing the command:

```bash
./depthnet.py "images/room_*.jpg" images/test/depth_room_%i.jpg
```

![Depthnet room](./images/depthnet-room-0.jpg)

The output images will be saved in the `images/test` directory.

### Mono Depth from Webcam

Make sure your webcam is connected. The model may take several minutes to download and compile on first run.

```bash
./depthnet.py /dev/video0  # csi://0 if using MIPI CSI camera
```

## Getting the Raw Depth Field

Let's learn how to access the raw depth map, you can do so with `depthNet.GetDepthField()`.  This will return a single-channel floating point image that is typically smaller (224x224) than the original input - this represents the raw output of the model.  On the other hand, the colorized depth image used for visualization is upsampled to match the resolution of the original input (or whatever the `--depth-size` scale is set to).

Below is Python code for accessing the raw depth field please copy and paste this code into a new file named `depthtest.py` in the `build/aarch64/bin` directory:

```python
# build/aarch64/bin/depthtest.py
# Testing monocular depth with DepthNet
# This script captures a single image from the webcam, generates a depth map, and saves both.

import jetson.inference
import jetson.utils
import numpy as np
import argparse
import sys
import os
import time

# Parse command line arguments
parser = argparse.ArgumentParser(description="Mono depth estimation demo that captures a single image.")
parser.add_argument("input", type=str, default="", nargs='?', help="URI of the camera (e.g., /dev/video0)")
parser.add_argument("--colormap", type=str, default="viridis-inverted", help="colormap to use for visualization (default is 'viridis-inverted')")
parser.add_argument("--filter-mode", type=str, default="linear", help="filtering mode used during visualization ('point' or 'linear')")
parser.add_argument("--network", type=str, default="", help="pre-trained model to load (optional)")

# Parse the arguments
args = parser.parse_args()

# Create output directory if it doesn't exist
output_dir = "images/test"
os.makedirs(output_dir, exist_ok=True)

# Load mono depth network - this creates a neural network that can estimate depth from a single image
print("Loading depth network...")
if args.network:
    net = jetson.inference.depthNet(args.network)
else:
    net = jetson.inference.depthNet()

# depthNet re-uses the same memory for the depth field,
# so you only need to do this once (not every frame)
depth_field = net.GetDepthField()

# cudaToNumpy() will map the depth field cudaImage to numpy
# this mapping is persistent, so you only need to do it once
depth_numpy = jetson.utils.cudaToNumpy(depth_field)

print(f"depth field resolution is {depth_field.width}x{depth_field.height}, format={depth_field.format}")

# Create video sources
# If input argument is provided, use that specific camera, otherwise use default
print("Creating camera connection...")
if args.input:
    print(f"Using camera: {args.input}")
    input = jetson.utils.videoSource(args.input, argv=sys.argv)
else:
    print("Using default camera")
    input = jetson.utils.videoSource("", argv=sys.argv)

# Capture a single image from the camera
print("Taking a picture from the camera...")
img = input.Capture()

if img is None:
    print("Failed to capture image from camera!")
    exit(1)
    
print(f"Captured image: {img.width}x{img.height} pixels")

# Process the image to estimate depth
print("Processing image with depthNet...")
net.Process(img)

# Wait for GPU to finish processing, so we can use the results on CPU
jetson.utils.cudaDeviceSynchronize()

# Find the min/max values with numpy
min_depth = np.amin(depth_numpy)
max_depth = np.amax(depth_numpy)
print(f"Depth range: min={min_depth:.2f}, max={max_depth:.2f}")

# Colorize the depth map for better visualization
print("Creating visualization...")
colormap = args.colormap  # Using the colormap specified in arguments
filter_mode = args.filter_mode  # Using the filter mode specified in arguments

# Create a composite image that will show both the original and depth side by side
composite = jetson.utils.cudaAllocMapped(width=img.width*2, height=img.height, format=img.format)

# Create an RGB image to hold the colorized depth visualization
depth_visual = jetson.utils.cudaAllocMapped(width=depth_field.width, 
                                           height=depth_field.height,
                                           format="rgb8")  # Create RGB format image

# Visualize the depth map with the colormap (output goes to depth_visual)
net.Visualize(depth_visual, colormap, filter_mode)

# Put the original image on the left side of the composite
jetson.utils.cudaOverlay(img, composite, 0, 0)

# Put the depth visualization on the right side
jetson.utils.cudaOverlay(depth_visual, composite, img.width, 0)

# Generate timestamp for unique filenames
timestamp = time.strftime("%Y%m%d-%H%M%S")

# Save the images
original_path = os.path.join(output_dir, f"original_{timestamp}.jpg")
depth_path = os.path.join(output_dir, f"depth_{timestamp}.jpg")
composite_path = os.path.join(output_dir, f"composite_{timestamp}.jpg")

print(f"Saving original image to {original_path}")
jetson.utils.saveImage(original_path, img)

print(f"Saving depth visualization to {depth_path}")
jetson.utils.saveImage(depth_path, depth_visual)

print(f"Saving composite image to {composite_path}")
jetson.utils.saveImage(composite_path, composite)

print("Processing complete! Images saved to:", output_dir)
```

Then run the script with the following command:

```bash
python3 depthtest.py /dev/video0
```

Trying to measure absolute distances using mono depth can lead to inaccuracies as it's typically more effective at relative depth estimation.  The range of values in the raw depth field can vary depending on the scene, so these are often re-calculated dynamically.  For example, during visualization histogram equalization is performed on the depth field to distribute the colormap more evenly across the range of depth values.

### Understanding the depthtest.py Script

This script demonstrates how to use the Jetson Inference library for monocular depth estimation from a camera input. Below is a concise overview of its key elements:

#### Key Components

- **Depth Network Setup**  
  Creates a neural network for depth estimation and allocates GPU memory for the depth field.

- **Camera Capture**  
  Connects to the specified camera (e.g., `/dev/video0`) and captures a frame.

- **Depth Processing**  
  Processes the captured image through the network and waits for GPU computation to complete.

- **Visualization**  
  Allocates GPU memory for rendering and applies a colormap to the depth data for display.

#### Working with This Code

- **Camera Options:**  
  - Use `/dev/video0`, `/dev/video1`, etc. for USB cameras.  
  - Use `csi://0` for MIPI CSI cameras on Jetson.

- **Colormap Customization:**  
  With `--colormap`, choose from options such as `viridis`, `inferno`, `plasma`, `turbo`, and `magma`.  
  Append `-inverted` to invert the colormap (e.g., `viridis-inverted`).

- **Filter Modes:**  
  - `--filter-mode=linear` (default, smoother visualization)  
  - `--filter-mode=point` (faster, more pixelated output)

- **Depth Network Selection:**  
  - `--network=fcn-mobilenet` (default model)  
  - `--network=fcn-resnet18` (more accurate but slower)

The script ultimately produces a side-by-side display of the original image and its corresponding depth map, making it easier to analyze the model’s output.

## Summary

This model is valuable in robotics and autonomous vehicles, where understanding the environment is crucial. Refer to the guide for details on obtaining raw depth data.

Next | [Curriculum Home](../README.md)  
Previous | [Background Removal](Background_Removal.md)
