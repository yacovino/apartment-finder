#! /bin/bash

HOST=ubuntu@104.131.177.187m
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
rsync -avz $(dirname "${DIR}")/ $HOST:~/cl-rental
ssh $HOST 'bash -s' < setup_scraper.sh