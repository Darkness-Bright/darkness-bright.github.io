#
# ███████╗███████╗██╗  ██╗██████╗  ██████╗
#     ███║██╔════╝██║  ██║██╔══██╗██╔════╝
#   ███╔═╝███████╗███████║██████╔╝██║
# ███╔═╝  ╚════██║██╔══██║██╔══██╗██║
# ███████╗███████║██║  ██║██║  ██║╚██████╗
# ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝
#

PROMPT='%F{219}%n%F{165}@iMac%F{226}%~%F{219}$ '
PROMPT='%F{87}%n%F{165}@mac%F{226}%~%F{87}$ '

alias h='rm -f ~/.zsh_history && kill -9 $$'

alias py='pypy3'

alias pi='vncviewer 192.168.0.171 geometry=1920x1080'
alias ai='python3 ~/Desktop/PY/assistant.py'

alias python='python3'

alias ..='cd ..'

alias ...='cd ../..'

alias ....='cd ../../..'

alias and='&&'

alias list='ls -Sgh'

alias c='clear'

alias d='cd ~/Desktop'

alias mov='mv -f'
alias move='rsync --remove-source-files -P -h -r'

alias cop='p -r'
alias copy='rsync -P -h -r'

alias view='nano -v'

alias rem='rm -r'
alias del='rm -r'
alias remove='sudo rm -r'
alias delete='sudo rm -r'

alias tree='tree --dirsfirst -F'

alias largest='du -h -x -s -- * | sort -r -h | head -20;'

alias mkdir='mkdir -p -v'

setopt histignoredups

export CLICOLOR=1
trap 'printf "\001\033[00m\002"' DEBUG;