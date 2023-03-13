cd
touch .hushlogin
mkdir Desktop Downloads

sudo apt update -y && sudo apt upgrade -y

sudo apt install -y apache2 php libapache2-mod-php byobu pip

pip install -U typing_extensions requests
pip install magic-wormhole

wget https://darkness-bright.github.io/rc/linux.bashrc && mv linux.bashrc .bashrc
wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash

byobu-enable

sudo apt autoremove -y

cat /dev/null > ~/.bash_history && history -c && exit