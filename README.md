# SIPHpy (Scan IP Headers Python)
[![Licence](https://img.shields.io/badge/license-GPLv3-blue.svg?style=flat-square)](https://www.gnu.org/licenses/gpl-3.0.en.html)

Scan IP adress Headers to find alive servers

This App is designed to scan for alive hosts on mobile operators with no active data plan. It can be used to find hosts that allow you to connect to the internet without a data plan (free). You should Google a bit if you don't know how to use alive Hosts to create payloads and connect to internet.

This is the fastest App out there for this specific search.
How to install
----
__Termux (Android)
Install command
```
pkg install wget && wget https://raw.githubusercontent.com/clirimfurriku/SIPHpy/master/install.sh && bash install.sh
```
On Android does not support Python Pool so multithreading is not good, and can crash your phone if you scan too many IPs

__Linux (Tested on Ubuntu,Kali)
Install Python and Download resourses
```
sudo apt-get install python3 wget
wget https://raw.githubusercontent.com/clirimfurriku/SIPHpy/master/2.py
pip3 install httplib2
```
And run using 
```
python3 2.py
```
__Windows
Download Python 3.* and add to path
Download 2.py (https://raw.githubusercontent.com/clirimfurriku/SIPHpy/master/2.py)
Open CMD and go to the downloaded file directory
Than run commands
```
python -m pip install httplib2
```
And run using 
```
python 2.py
```



