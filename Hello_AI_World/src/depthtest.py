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
