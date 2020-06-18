#!/data/data/com.termux/files/usr/bin/bash
echo ____________________________________
echo installing plugins
termux-setup-storage
pkg install -y wget && pkg install -y python
pip install tqdm
pip install ping3
echo _____________________________________
echo installing commands
echo ______________________________________
wget https://raw.githubusercontent.com/clirimfurriku/SIPHpy/master/siphpy

cp /data/data/com.termux/files/home/siphpy /data/data/com.termux/files/usr/bin/siphpy

wget https://raw.githubusercontent.com/clirimfurriku/payloader/master/ip.py

cp /data/data/com.termux/files/home/ip.py /data/data/com.termux/files/usr/bin/ip.py

chmod +x /data/data/com.termux/files/usr/bin/siphpy

chmod +x /data/data/com.termux/files/usr/bin/ip.py

rm -f /data/data/com.termux/files/home/ip.py
rm -f /data/data/com.termux/files/home/siphpy

echo ____________________________________________
echo finished installing
echo ____________________________________________
echo to start enter command "siphpy"
echo  
