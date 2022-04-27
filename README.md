## clockword 🍊

A relaxed customizable clock which conveys your system time lyrically.

<img src=demo.png>


## Patchnotes
|Release|Notes|
|-|-|
|1.0.3|Binary release|
|1.0.2|+ enabled dark mode <br> + opacity adjustment (Windows only) <br> + added taskbar icon|

## Run in Python
```bash
# option 1: Run from terminal
python main.py 
```
```python
# option 2: Import
from main import clockword
clockword(background='#000', foreground='#fff', font=('Times New Roman', 20), opacity=0.7)
```

## Build .exe
Run the build script
```bash
python build.py
```
the binary will be located in the `/bin` directory.