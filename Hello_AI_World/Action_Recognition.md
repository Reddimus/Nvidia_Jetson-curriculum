# [Action Recognition](https://github.com/dusty-nv/jetson-inference/blob/master/docs/actionnet.md)

After building from source, follow [this guide](https://github.com/dusty-nv/jetson-inference/blob/master/docs/actionnet.md) to set up action recognition.

This demo uses a pre-trained AI model to detect human actions in video streams.

Before starting, please ensure:

- The [og-tennis.mp4](./images/og-tennis.mp4) video is placed in the root directory of the Hello_AI_World repository.

Then after reading guide run the following command from the `Hello Ai World` repository root:

```bash
# Python
./aarch64/bin/actionnet.py --skip-frames=0 og-tennis.mp4 an-tennis.mp4
```

> Note: The model skips frames by default, so the output video duration may be shorter.
