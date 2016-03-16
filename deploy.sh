#! /bin/bash

HOST=ubuntu@104.131.177.187
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
rsync -avz --exclude listings.db --exclude __pycache__ . $HOST:~/cl-rental
ssh $HOST '/bin/bash -s' < setup_scraper.sh