Apartment finder
-------------------

This repo contains the code for a bot that will scrape Craigslist for real-time listings matching specific criteria, then alert you in Slack.  This will let you quickly see the best new listings, and contact the owners.  You can adjust the settings to change your price range, what neighborhoods you want to look in, and what transit stations and other points of interest you'd like to be close to.

It's recommended to use Docker to run the program.

Settings
--------------------

Look in `settings.py` for a full list of all the configuration options.  Here's a high level overview:

* `MIN_PRICE` -- the minimum listing price you want to search for.
* `MAX_PRICE` -- the minimum listing price you want to search for.
* `CRAIGSLIST_SITE` -- the regional Craigslist site you want to search in.
* `AREAS` -- a list of areas of the regional Craiglist site that you want to search in.
* `BOXES` -- coordinate boxes of the neighborhoods you want to look in.
* `NEIGHBORHOODS` -- if the listing doesn't have coordinates, a list of neighborhoods to match on.
* `MAX_TRANSIT_DISTANCE` -- the farthest you want to be from a transit station.
* `TRANSIT_STATIONS` -- the coordinates of transit stations.
* `CRAIGSLIST_HOUSING_SECTION` -- the subsection of Craigslist housing that you want to look in.
* `SLACK_CHANNEL` -- the Slack channel you want the bot to post in.

Configuration
--------------------

## Docker

* Create a folder called `config`, then put a file called `private.py` inside.
* Specify new values for any of the settings above in `private.py`.
    * For example, you could put `AREAS = ['sfc']` in `private.py` to only look in San Francisco.

## Manual

* Create a file called `private.py`.
* Add a value called `SLACK_TOKEN` that contains your Slack API token.
* Add any other values you want.

Installation + Usage
--------------------

## Docker

* Install Docker by following [these instructions](https://docs.docker.com/engine/installation/).
* To run the program with the default configuration:
    * `docker run -d -e SLACK_TOKEN={YOUR_SLACK_TOKEN} dataquestio/apartment-finder`
* To run the program with your own configuration:
    * `docker run -d -e SLACK_TOKEN={YOUR_SLACK_TOKEN} -v {PATH_TO_YOUR_CONFIG_FOLDER}:/opt/wwc/apartment-finder/config dataquestio/apartment-finder`
    
## Manual

* Look in the Dockerfile, and make sure you install any of the apt packages there.
* Install the Python requirements with `pip install -r requirements.txt`.
* Run the program with `python main_loop.py`.

Troubleshooting
---------------------

## Docker

* Use `docker ps` to get the id of the container.
* Run `docker exec -it {YOUR_CONTAINER_ID} /bin/bash`
* Try `sqlite listings.db` to inspect the database state (the only table is also called `listings`).
    * If nothing is in the database, you may need to wait for a bit, or verify that your settings aren't too restrictive and aren't finding any listings.
* Inspect the logs using `tail -f -n 1000 /opt/wwc/logs/afinder.log`.

## Manual

* Look at the stdout of the main program.
* Inspect `listings.db` to ensure listings are being added.

Deploying
---------------------

* Create a server that has Docker installed.
* Follow the configuration + installation instructions for docker above.