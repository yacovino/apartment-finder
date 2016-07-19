Apartment finder
-------------------

This repo contains the code for a Slack bot that will scrape Craigslist for listings matching specific criteria, then alert you when they go live.

Installation
--------------------

* `pip install -r requirements.txt`

Usage
--------------------

* `python scrape_loop.py`

Deploying
---------------------

* Initialize server
* Add ssh key to your local agent using `ssh-add`
* If your server username is `USER`, and the IP is `HOST`, you should be able to ssh into it using `ssh USER@HOST`
* `deploy.sh USER@HOST`
    * For example, `deploy.sh ubuntu@104.236.15.55`
