# [Background Removal](https://github.com/dusty-nv/jetson-inference/blob/master/docs/backgroundnet.md)

Let us continue seeing what other artificial intelligence related tasks we can do with the Hello AI World project. In this section, we will explore how to remove the background from a video stream using a pre-trained AI model. Please follow the guide [here](https://github.com/dusty-nv/jetson-inference/blob/master/docs/backgroundnet.md).

In short we can remove the background of a video or a video stream.

Lets try it out with an image first.

```bash
./aarch64/bin/backgroundnet.py images/bird_0.jpg images/test/bird_mask.png                              # remove the background (with alpha)
./aarch64/bin/backgroundnet.py --replace=images/snow.jpg images/bird_0.jpg images/test/bird_replace.jpg # replace the background
```

Lets try it out with our webcam.

```bash
./aarch64/bin/backgroundnet /dev/video0                             # remove the background
```

> Note: This is ran by source code. Make sure you built from source correctly.
