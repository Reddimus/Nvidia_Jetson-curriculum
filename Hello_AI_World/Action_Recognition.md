# [Action Recognition](https://github.com/dusty-nv/jetson-inference/blob/master/docs/actionnet.md)

After building from source, follow [this guide](https://github.com/dusty-nv/jetson-inference/blob/master/docs/actionnet.md) to set up action recognition.

This demo uses a pre-trained AI model to detect human actions in video streams.

Before starting, please ensure:

- Place [og-tennis.mp4](./images/og-tennis.mp4) video into `build/aarch64/bin/images` in the repository. As reference after building from source, we should be in the `build` directory and the `build/aarch64/bin` directory should be present with many python files and `images` folder.

Then after reading guide run the following commands:

```bash
cd aarch64/bin
# Python
./actionnet.py --skip-frames=0 images/og-tennis.mp4 images/test/ar-tennis-action.mp4
```

After running the action net demo, you should see the `an-tennis-action.mp4` video in `build/aarch64/bin/images/test` folder.

The model skips frames by default, so the output video duration may be shorter. However, you will notice that the model is able to detect actions in the video and label it at the top.

Next | [Background Removal](Background_Removal.md)  
Previous | [Building from Source](Building_Source.md)
