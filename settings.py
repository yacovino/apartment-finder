import os

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = 1500

# The maximum rent you want to pay per month.
MAX_PRICE = 2000

## Location preferences

# What craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
AREAS = ["eby", "sfc", "sby", "nby"]

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
    "adams_point": [
        [37.81589,	-122.26081],
        [37.80789, -122.25000]
    ],
    "piedmont": [
        [37.83237, -122.25386],
        [37.82240, -122.24768]
    ],
    "rockridge": [
        [37.84680, -122.25944],
        [37.83826, -122.24073]
    ],
    "berkeley": [
        [37.86781, -122.26502],
        [37.86226, -122.25043]
    ],
    "north_berkeley": [
        [37.87655, -122.28974],
        [37.86425, -122.26330]
    ],
    "pac_heights": [
        [37.79850, -122.44784],
        [37.79124, -122.42381]
    ],
    "lower_pac_heights": [
        [37.78873, -122.44544],
        [37.78554, -122.42878]
    ],
    "haight": [
        [37.77086, -122.45401],
        [37.77059, -122.42688]
    ],
    "sunset": [
        [37.76258, -122.50825],
        [37.75451, -122.46422]
    ],
    "richmond": [
        [37.78029, -122.51005],
        [37.77188, -122.47263]
    ],
    "presidio": [
        [37.78829, -122.47151],
        [37.77805, -122.43959]
    ]
}

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
NEIGHBORHOODS = ["berkeley north", "berkeley", "rockridge", "adams point", "oakland lake merritt", "cow hollow", "piedmont", "pac hts", "pacific heights", "lower haight", "inner sunset", "outer sunset", "presidio", "palo alto", "richmond / seacliff", "haight ashbury", "alameda", "twin peaks", "noe valley", "bernal heights", "glen park", "sunset", "mission district", "potrero hill", "dogpatch"]

## Transit preferences

# The farthest you want to live from a transit stop.
MAX_TRANSIT_DIST = 2 # kilometers

# Transit stations you want to check against.  Every coordinate here will be checked against each listing,
# and the closest station name will be added to the result and posted into Slack.
TRANSIT_STATIONS = {
    "oakland_19th_bart": [37.8118051,-122.2720873],
    "macarthur+bart": [37.8265657,-122.2686705],
    "rockridge_bart": [37.841286,-122.2566329],
    "downtown_berkeley_bart": [37.8629541,-122.276594],
    "north_berkeley_bart": [37.8713411,-122.2849758]
}

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 20 * 60 # 20 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#cheaperhousing"

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")

# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass