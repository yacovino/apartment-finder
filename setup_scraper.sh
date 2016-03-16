#! /bin/bash

cd ~/cl-rental

sudo apt-get update
sudo apt-get install python3-pip -y
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev zip git-core -y
sudo pip3 install -r requirements.txt

sudo service scraper stop || true
sudo cp scraper.conf /etc/init/scraper.conf
sudo service scraper start