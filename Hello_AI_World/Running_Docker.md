# [Running the Docker Container](https://github.com/dusty-nv/jetson-inference/blob/master/docs/aux-docker.md)

Docker simplifies dependency management and environment isolation, allowing you to quickly run pre-built models and applications from the Hello AI World repository. This is one of two ways to run pre-trained models and applications in the repository; the other is building from source.

We will be following the [Running the Docker Container](https://github.com/dusty-nv/jetson-inference/blob/master/docs/aux-docker.md) guide to set up a Docker container with the pre-built models and applications.

**In short we can run the following commands to get through this Docker guide:**

Start the Docker container, run in the terminal:

```bash
docker/run.sh
```

Then, navigate to the following directory *inside the Docker container*:

```bash
cd build/aarch64/bin
```

## Launching the video viewer application

Great the docker container is running, now we can test the video viewer application. All the applications are located in the `build/aarch64/bin` directory.

```bash
./video-viewer /dev/video0
```

![video-viewer](./images/video-viewer.gif)

## Classify a jellyfish

Next, test the imagenet classification application to classify an image of a jellyfish. The application will classify the image then write what it thinks the image is to the image and save it to the `build/aarch64/bin/images/test` directory.

```bash
./imagenet images/jellyfish.jpg images/test/jellyfish.jpg
```

![jellyfish](./images/jellyfish.jpg)
![classified-jellyfish](./images/classified-jellyfish.jpg)

## Detect objects in an image

Lastly, test the detectnet application to detect objects in an image. The application will detect the objects in the image and write the labels to the image and save it to the `build/aarch64/bin/images/test` directory.

```bash
./detectnet images/peds_0.jpg images/test/peds_0.jpg
```

![multiple-people](./images/multiple-people.jpg)
![detected-multiple-people](./images/detected-multiple-people.jpg)

Next | [Building from Source](Building_Source.md)  
Previous | [Hello AI World Hello World](./README.md)
