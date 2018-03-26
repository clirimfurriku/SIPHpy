#!/data/data/com.termux/files/usr/bin/bash
echo ____________________________________
echo installing plugins
termux-setup-storage
pkg install -y wget && pkg install -y python && pkg install -y curl 
echo _____________________________________
echo installing commands
echo ______________________________________
wget https://raw.githubusercontent.com/clirimfurriku/payloader/master/clirimfurriku

cp /data/data/com.termux/files/home/clirimfurriku /data/data/com.termux/files/usr/bin/clirimfurriku

wget https://raw.githubusercontent.com/clirimfurriku/payloader/master/ip.py

cp /data/data/com.termux/files/home/ip.py /data/data/com.termux/files/usr/bin/ip.py

chmod +x /data/data/com.termux/files/usr/bin/clirimfurriku

chmod +x x /data/data/com.termux/files/usr/bin/ip.py

rm -f /data/data/com.termux/files/home/ip.py
rm -f /data/data/com.termux/files/home/clirimfurriku

echo. ____________________________________________
echo finished installing
echo ____________________________________________
echo to start enter command "clirimfurriku"