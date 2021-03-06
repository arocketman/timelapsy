# timelapsy

Timelapsy is a python project to create your own DIY timelapse using your phone camera running ip webcam.
It is written in python and uses opencv to capture frames. 

## Features

* Configurable frequency of capture of the image
* Automatic creation of video with the desired FPS

## Requirements

* You will need a phone 📱 running [Ip Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en)
  * You can also use a webcam 📷 or other supported streams (RTSP, HTTP) Ip camera, see: [OpenCV](https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-videocapture)
* Python 3+ installed (Tested with 3.7) 

## Usage
```
Usage: app.py [OPTIONS]

Options:
  --address TEXT            Address of stream, can also be webcam device id
                            (e.g: http://192.168.1.166:8080/video) for ip
                            camera

  --save-frequency INTEGER  Saves frame/image every X seconds
  --save-path TEXT          Directory where to store files
  --help                    Show this message and exit.
```
