# SIPHpy (Scan IP Headers Python)
[![Licence](https://img.shields.io/badge/license-GPLv3-blue.svg?style=flat-square)](https://www.gnu.org/licenses/gpl-3.0.en.html)

__Scan IP adress Headers to find alive servers__

This App is designed to scan for alive hosts on mobile operators with no active data plan. It can be used to find hosts that allow you to connect to the internet without a data plan (free). You should Google a bit if you don't know how to use alive Hosts to create payloads and connect to internet.

This is the fastest App out there.

NEW UPDATE
--------------
Update of 04/02/2019 i rebuild the app from beginning.
Supports up to 100000 threads (If your network bandwith supports it) and time to finish is much lower
To note is that now results wont be saved to a file :(  they will just ptint on screen, however this was the best way to not use RAM which was the cause of crashing on old versions


How to install
--------------

__Termux (Android)__

Install command
```
pkg install wget && wget https://raw.githubusercontent.com/clirimfurriku/SIPHpy/master/install.sh && bash install.sh
```
On Android does not support Python Pool so multithreading is not good, and can crash your phone if you scan too many IPs

__Linux__ (Tested on Ubuntu,Kali)

Install Python and Download resourses
```
sudo apt-get install python3 wget
wget https://raw.githubusercontent.com/clirimfurriku/SIPHpy/master/ip.py
pip3 install httplib2
```
And run using 
```
python3 ip.py
```
__Windows__

If you dont want to use python use a build pachkage and just run it
* [Download SIPHpy prebuild release for windows](https://github.com/clirimfurriku/SIPHpy/releases/)

Or if you want to do it yourself useng python:
Download Python 3.* and add to path
Download [ip.py](https://raw.githubusercontent.com/clirimfurriku/SIPHpy/master/ip.py)
Open CMD and go to the downloaded file directory
Than run commands
```
python -m pip install httplib2
```
And run using 
```
python ip.py
```



