# SIPHpy (Scan IP Headers Python)
[![Licence](https://img.shields.io/badge/license-GPLv3-blue.svg?style=flat-square)](https://www.gnu.org/licenses/gpl-3.0.en.html)

__Scan IP adresses find alive servers__

This App is designed to scan for alive hosts that respond through proxy. It can be used to find hosts that allow you to connect to the internet even when you are not supposed to ;)

This is the fastest App out there for this job. (It was the fastest until I rebuild it in GO)
<br />
<br />

Will I open source the GO version?
\
Maybe.


## __How to install__
--------------

__Termux (Android)__

Install command
```shell
pkg install -y wget && wget https://raw.githubusercontent.com/clirimfurriku/SIPHpy/master/install.sh && bash install.sh
```
And run using 
```shell
siphpy
```

__Linux__

Install Python and Download resourses
```shell
sudo apt-get install python3-dev wget
wget https://raw.githubusercontent.com/clirimfurriku/SIPHpy/master/ip.py
pip3 install ping3 tqdm
```
And run using 
```shell
python3 ip.py
```

__Windows__

If you dont want to use python use a build pachkage and just run it
* [Download SIPHpy prebuild release for windows](https://github.com/clirimfurriku/SIPHpy/releases/)

Or if you want to do it yourself useng python:
Download Python 3.* and add to path
Download [ip.py](https://raw.githubusercontent.com/clirimfurriku/SIPHpy/master/ip.py)
Open CMD and go to the downloaded file directory

And run using command
```
python ip.py
```



