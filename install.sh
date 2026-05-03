#!/data/data/com.termux/files/usr/bin/bash
pkg update && pkg upgrade -y
pkg install python git termux-api -y
pip install pyTelegramBotAPI requests
termux-wake-lock
echo "python ~/seekerr2.0/seeker.py &" >> ~/.bashrc
chmod +x seeker.py
print "Орнату аяқталды! Енді python seeker.py жаз."
