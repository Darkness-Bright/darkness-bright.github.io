#
# ██████╗  █████╗ ███████╗██╗  ██╗██████╗  ██████╗
# ██╔══██╗██╔══██╗██╔════╝██║  ██║██╔══██╗██╔════╝
# ██████╔╝███████║███████╗███████║██████╔╝██║
# ██╔══██╗██╔══██║╚════██║██╔══██║██╔══██╗██║
# ██████╔╝██║  ██║███████║██║  ██║██║  ██║╚██████╗
# ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝


HISTTIMEFORMAT="%F %T "

HISTCONTROL=ignoredups

HISTSIZE=333

HISTFILESIZE=999

shopt -s cdspell
shopt -s dirspell

shopt -s histappend

shopt -s checkwinsize

alias gs='git status'

alias ga='git add'

alias gaa='git add --all'

alias gc='git commit'

alias gl='git log --oneline'

alias gb='git checkout -b'

alias gd='git diff'

alias ..='cd ..'

alias ...='cd ../..'

alias ....='cd ../../..'

alias and='&&'

alias ls='ls --color=auto'
alias list='ls -Sgh'

alias c='clear'
alias cc='cat /dev/null > ~/.bash_history && history -c && exit'

alias d='cd ~/Desktop'

alias up='sudo apt update && sudo apt upgrade'

alias df='sudo df -h --total'

alias sd='env SUDO_ASKPASS=/usr/lib/piclone/pwdpic.sh sudo -AE dbus-launch piclone'

alias apt='sudo apt'

alias mov='sudo mv -f'
alias move='sudo rsync --remove-source-files -P -h -r'

alias cop='sudo cp -r'
alias copy='sudo rsync -P -h -r'

alias view='sudo nano -v'
alias nano='sudo nano -S'

alias rem='rm -r'
alias del='rm -r'
alias remove='sudo rm -r'
alias delete='sudo rm -r'

alias reboot='sudo reboot'

alias down='sudo shutdown -h now'

alias tree='sudo tree --dirsfirst -F'

alias mark='sudo mount.cifs //192.168.0.6/mark $HOME/Desktop/mark/ -o username=mark,password=mark123'

alias mkdir='sudo mkdir -p -v'

alias server='cd /var/www/html'

alias whisperen='whisper --model tiny.en'
alias whisperenglish='whisper --model base.en'

alias largest='sudo du -h -x -s -- * | sort -r -h'

alias temp='sudo vcgencmd measure_temp'

alias fm='sudo $HOME/fm_transmitter/fm_transmitter -f 88'

function backup() {
    echo Backup starting. Sit back and relax for 1 hour!
    echo Seriously. Would you just wait for ONE FULL HOUR.
    echo Never mind any errors! It usually works fine.
    echo Deleting all TIMESHIFT backups and snapshots!
    sudo timeshift --delete-all
    sudo umount -f -q $HOME/Desktop/mark
    sudo rm -r /var/log/journal/*
    sudo "$HOME/Pi-Power-Tools/functions/image-shrink" "$HOME/backup.img" $((1024*1024))
    sudo "$HOME/Pi-Power-Tools/functions/milliways-image-backup" "$HOME/backup.img"
    sudo "$HOME/Pi-Power-Tools/functions/image-shrink" "$HOME/backup.img" 0
    echo Complete. backup.img should be in home directory. 
}

function git_branch() {
    if [ -d .git ] ; then
        printf "%s" "($(git branch 2> /dev/null | awk '/\*/{print $2}'))";
    fi
}

function git_init() {
    if [ -z "$1" ]; then
        printf "%s\n" "Please provide a directory name.";
    else
        mkdir "$1";
        builtin cd "$1";
        pwd;
        git init;
        touch readme.md .gitignore LICENSE;
        echo "# $(basename $PWD)" >> readme.md
    fi
}

function info() {
    printf "\n"
    printf "%s\n" "IP ADDR: $(curl -s ifconfig.me)"
    printf "%s\n" "USER: $(whoami)"
    printf "%s\n" "DATE: $(date)"
    printf "%s\n" "CPU: $(sudo cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq)"
    printf "%s\n" "TEMP: $(sudo vcgencmd measure_temp)"
    printf "%s\n" "UPTIME: $(uptime -p)"
    printf "%s\n" "HOSTNAME: $(hostname -f)"
    printf "\n"
}

PS1='\001\033[0;96m\002\u\001\033[0;35m\002@\h\001\033[0;93m\002\w\001\033[0;96m\002$ '

trap 'printf "\001\033[00m\002"' DEBUG;

export PATH="$HOME/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games"