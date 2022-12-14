# ReadMe

# What is this repository for?
* Carrying out image adjustments on a batch of images.

# Summary
Only changing image brightness is implimented so far, but the structure of the classes is set up such that further adjustments may be added without much work.

# Getting started
* Drop images into `imgs/in`.
* Inspect `main.py` lines 89-93 and edit brighness value as desired.
* Ensure a python version > 3.0.0 is installed by running:
```
    python3 -V
```
* Create a virtual environment with:
```
    python -m venv .venv
```
* Activtate the virtual enviornment with:
On Mac:
```
    source .venv/bin/activate
```
or on windows:
```
    .venv/Scripts/activate
```
* Install dependencies with:
```
    pip install -r requirements.txt
```
* Run `main.py` with:
```
    python main.py
```
* The adjusted images will be found in the `imgs/out` folder.