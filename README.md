# Remote Trackpad

## Why?

In my desktop setup I have three monitors, two keyboards, one mouse and a lack of space for using a second mouse. So, I needed a touchpad, just like a laptop. But... It **is** expensive, at least for Brazilian reality. And also it is very hard to find one.

So, I decided to use a touch device that I already have - an old Android Smartphone. After around 10 hours working, I decided upload this into GitHub, firstly as a case study for my students and also to help someone who have similar needs.

## How?

The software consists in a local server, that should run in a desktop machine. Right now this is just a POC, and I need to move some configurations to another file, in order to facilitate the process of running by yourself.

At this moment, this is working fine on Windows 10 and this version probably won't work on Linux or Mac. The reason behind this is that I had to use an internal call from the *mouse* Python library, since the library itself doesn't allow horizontal scrolling (and this is something I wanted).

## Dependencies

Besides the Node dependencies listed on [package.json] file, the following Python 3 libraries are needed:
- [mouse](https://pypi.org/project/mouse/)
- [pyautogui](https://pypi.org/project/PyAutoGUI/)
- [websockets](https://pypi.org/project/websockets/)