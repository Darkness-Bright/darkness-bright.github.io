# Start the Management Utility
/usr/local/sbin/emhttp &

echo "shopt -s cdspell">>/etc/profile
echo "shopt -s dirspell">>/etc/profile
echo "shopt -s histappend">>/etc/profile
echo "shopt -s checkwinsize">>/etc/profile

# Aliases

echo "alias bashrc='nano /boot/config/go'">>/etc/profile
echo "alias c='clear'">>/etc/profile
echo "alias clear='clear && cat /dev/null > ~/.bash_history && history -c'">>/etc/profile

echo "alias ..='cd ..'">>/etc/profile
echo "alias ...='cd ../..'">>/etc/profile
echo "alias ....='cd ../../..'">>/etc/profile

echo "alias ls='ls --color=auto'">>/etc/profile
echo "alias list='ls -Sgh'">>/etc/profile

echo "alias df='df -h --total'">>/etc/profile

echo "alias mov='mv -f'">>/etc/profile
echo "alias cop='cp -r'">>/etc/profile

echo "alias rem='rm'">>/etc/profile
echo "alias del='rm'">>/etc/profile
echo "alias remove='rm -r'">>/etc/profile
echo "alias delete='rm -r'">>/etc/profile

echo "alias largest='du -h -x -s -- * | sort -r -h'">>/etc/profile
echo "alias server='cd /mnt/disks/SSD/www/'">>/etc/profile