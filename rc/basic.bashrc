HISTTIMEFORMAT="%F %T "

HISTCONTROL=ignoredups

HISTSIZE=333

HISTFILESIZE=999

shopt -s cdspell
shopt -s dirspell

shopt -s histappend

shopt -s checkwinsize

alias ..='cd ..'

alias ...='cd ../..'

alias ....='cd ../../..'

alias ls='ls --color=auto'
alias list='ls -Sgh'

alias c='clear'
alias clear='clear && cat /dev/null > ~/.bash_history && history -c'

alias d='cd ~/Desktop'

alias df='df -h --total'

alias mov='mv -f'
alias move='rsync --remove-source-files -P -h -r'

alias cop='cp -r'
alias copy='rsync -P -h -r'

alias view='nano -v'
alias nano='nano -S'

alias rem='rm -r'
alias del='rm -r'
alias remove='sudo rm -r'
alias delete='sudo rm -r'

alias server='cd /var/www/html'

alias largest='du -h -x -s -- * | sort -r -h'

PS1='\001\033[0;96m\002\u\001\033[0;35m\002@\h\001\033[0;93m\002\w\001\033[0;96m\002$ '
trap 'printf "\001\033[00m\002"' DEBUG;