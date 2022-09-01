
# MouseCursorTracker
Simple mouse cursor tracker; compatible with Linux, macOS, and MS Windows. It can be used in a variety of research studies such as HCI, psychology, and cognitive studies.

# Dependencies
In order to use MouseCursorTracker, you have to install [PyAutoGUI](https://pypi.org/project/PyAutoGUI/):
```sh
pip install PyAutoGUI==0.9.53
```

# How to Run?
Simply run the below command in a terminal:
```sh
python tracker.py --sampling_rate 50
```
The `--sampling_rate` is optional and by default is 60 Hz. In order to stop recording, press `ctrl-c` in the same terminal you started the tracker.
