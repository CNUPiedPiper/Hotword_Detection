# Hotword Detection
Hotword detection using Snowboy(based on DNN)

## Dependency
### Access Microphone
```
$ sudo apt-get install python-pyaudio python3-pyaudio sox
$ pip2 install pyaudio
```
### Change your '~/.asoundrc' file to:
```
pcm.!default {
  type asym
   playback.pcm {
     type plug
     slave.pcm "hw:0,0"
   }
   capture.pcm {
     type plug
     slave.pcm "hw:1,0"
   }
}
```

## Running a Demo
```
$ python2 demo.py haru.pmdl
```
or
```
$ python2 hotword_test.py
```
