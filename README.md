# SnipPy
SnipPy is an open source snipping tool for Windows written in Python. It operates from the command-line with the `snippy` command and allows you to capture a part of the screen, which then gets copied to the Windows clipboard for pasting. The goal of this project is to support other tools which can trigger the tool from the command line and use the output from the Windows clipboard.

## Getting started
### Prequisites
- Python 3.6.4 from https://www.python.org

### Installation
```
pip install git+https://github.com/koenvaneijk/snippy
```

### Usage
Run following command in the command-line:
```
snippy
```

## To do
Implement functionality to 
- export as base64 string to the clipboard or stdout

## Credits
Credits go toward the following people:
- user1129665 on [this stackoverflow answer](https://stackoverflow.com/a/21320589) for providing the reference implementation for the Windows Clipboard
- original snipping tool script by [harupy/snipping-tool](https://github.com/harupy/snipping-tool) on which this repository is largely based.