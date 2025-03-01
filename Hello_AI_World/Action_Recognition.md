# [Action Recognition](https://github.com/dusty-nv/jetson-inference/blob/master/docs/actionnet.md)

After building from source, follow [this guide](https://github.com/dusty-nv/jetson-inference/blob/master/docs/actionnet.md) to set up action recognition.

## Quick start

This demo uses a pre-trained AI model to detect human actions in video streams.

Before starting, please ensure:

- The [og-tennis.mp4](./images/og-tennis.mp4) video is placed in `build/aarch64/bin/images` directory of the Hello_AI_World repository.

Then after reading guide run the following command from the `build/aarch64/bin` directory of the Hello_AI_World repository:

```bash
# Python
./actionnet.py --skip-frames=0 images/og-tennis.mp4 images/test/an-tennis.mp4
```

The `an-tennis.mp4` video will be saved in the `build/aarch64/bin/images/test` directory.

The model skips frames by default, so the output video duration may be shorter. However, you will notice that the model is able to detect actions in the video and label it at the top.

Next | [Background Removal](Background_Removal.md)  
Previous | [Building from Source](Building_Source.md)
