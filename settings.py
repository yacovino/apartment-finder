import os

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = 1500

# The maximum rent you want to pay per month.
MAX_PRICE = 2000

## Bedrooms

# Number of bedrooms
BEDROOMS = 1

## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'newyork'

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREAS = ["brk"]

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
    "park_slope": [
        [-73.992406,    40.657472],
        [-73.970175,    40.684611],
    ],
    "gowanus": [
        [-73.997211,    40.66508],
        [-73.984938,    40.678165],
    ],
    "prospect_heights": [
        [-73.97275,     40.671004],
        [-73.959618,    40.681875],
    ],
    "west_crown_heights": [
        [-73.962193,    40.663778],
        [-73.947773,    40.679792],
    ],
    "fort_greene": [
        [-73.978415,    40.682786],
        [-73.970175,    40.693394],
    ],
    "clinton_hill": [
        [-73.969488,    40.68207],
        [-73.959017,    40.693622],
    ],
    "west_bed_stuy": [
        [-73.959446,    40.67875],
        [-73.947344,    40.694745],
    ],
    "south_slope": [
        [-73.987341,    40.642875],
        [-73.970947,    40.660913],
    ],
    "boerum hill": [
        [-73.994293,     40.680638],
        [-73.977975,     40.690344],
    ],
    "carroll gardens": [
        [-74.00341,     40.671976],
        [-73.989144,    40.686447],
    ],
    "cobble hill": [
        [-74.0007037,   40.683754],
        [-73.9923513,   40.6915438],
    ],
    "downtown brooklyn": [
        [-73.992383,    40.686561],
        [-73.978586,    40.701431],
    ],
    "brooklyn heights": [
        [-74.000205,    40.689705],
        [-73.990441,    40.703001],
    ],
    "dumbo": [
        [-73.9945775,   40.7014434],
        [-73.9845085,   40.7055669],
    ],
    "ditmas park": [
        [-73.972728,    40.637225],
        [-73.964725,    40.64649],
    ],
    "west lefferts gardens": [
        [-73.962728,    40.65572],
        [-73.956592,    40.662068],
    ],
    "kensington": [
        [-73.980232,    40.630663],
        [-73.97099,     40.650006],
    ],
    "prospect park south": [
        [-73.971234,    40.643559],
        [-73.964124,    40.650592],
    ]
}

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
NEIGHBORHOODS = ["park slope",
                 "gowanus",
                 "fort greene",
                 "clinton hill",
                 "crown heights",
                 "bed-stuy"
                 "bedstuy",
                 "south slope",
                 "bedford-stuyvesant",
                 "prospect heights",
                 "carroll gardens",
                 "boerum hill",
                 "dumbo",
                 "brooklyn heights",
                 "ditmas park",
                 "ditmas",
                 "lefferts",
                 "lefferts gardens",
                 "plg",
                 "kensington",
                 "prospect park south"]

## Transit preferences

# The farthest you want to live from a transit stop.
MAX_TRANSIT_DIST = 2 # kilometers

# Transit stations you want to check against.  Every coordinate here will be checked against each listing,
# and the closest station name will be added to the result and posted into Slack.
TRANSIT_STATIONS = {
    "Bergen St 2-3": [-73.974999151168, 40.6808621368295],
    "Kingston - Throop Aves C": [-73.9408589987126, 40.679918999416],
    "DeKalb Ave B-Q-R": [-73.9817709444094, 40.6906481199697],
    "Chauncey St J-Z": [-73.9103835703337, 40.682851300878],
    "Union St R": [-73.9831099990967, 40.6773156673509],
    "Ralph Ave C": [-73.920785999333, 40.6788220008733],
    "Franklin Ave 2-3-4-5": [-73.9580997367769, 40.6707651534489],
    "Winthrop St 2-5": [-73.9500793459099, 40.6566593137607],
    "Prospect Park B-Q-S": [-73.962031304266, 40.6616334551018],
    "Ditmas Ave F": [-73.9781719996516, 40.6361186666629],
    "Classon Ave G": [-73.9599900013721, 40.6888890002645],
    "Broadway G": [-73.9503122560662, 40.7061265762741],
    "Halsey St J": [-73.9166388842194, 40.6864152707043],
    "Lorimer St J-M": [-73.947354998842, 40.703844000042],
    "Park Pl S": [-73.9576240007463, 40.6747716668526],
    "Ocean Pkwy Q": [-73.9685009997517, 40.5763116670809],
    "Bedford - Nostrand Aves G": [-73.9535220006402, 40.6896270015844],
    "15th St - Prospect Park F-G": [-73.9797358059287, 40.6600356881002],
    "7th Ave F-G": [-73.9802511790094, 40.6662446900198],
    "Ft Hamilton Pkwy F-G": [-73.9757759991747, 40.6507816680341],
    "Church Ave F-G": [-73.9797211622908, 40.6442720001299],
    "Beverly Rd Q": [-73.9643577962312, 40.6439045986041],
    "Church Ave B-Q": [-73.9628824619211, 40.6504932464648],
    "Newkirk Ave B-Q": [-73.9626948683726, 40.6351419373378],
    "Parkside Ave Q": [-73.9614534398764, 40.6550730416371],
    "Grand Army Plaza 2-3-4": [-73.9709563319228, 40.6752946951032],
    "Fulton St G": [-73.9753749983314, 40.6871189995077],
    "Clinton - Washington Aves G": [-73.9667959986695, 40.6880940010605],
    "7th Ave B-Q": [-73.9728527919102, 40.6771021798329],
    "Atlantic Av - Barclay's Center B-Q-D-N-R-2-3-4-5": [-73.9767834396316, 40.6844883234536],
    "Borough Hall 4-5": [-73.9901510009053, 40.692403999991],
    "Nostrand Ave A-C": [-73.9504260009968, 40.6804380000622],
    "Nevins St 2-3-4-5": [-73.9804067987457, 40.6883105801902],
    "Eastern Pkwy - Bklyn Museum 2-3-4": [-73.9642220374842, 40.6720322354592],
    "Beverly Rd 2-5": [-73.948847983817, 40.6451235189437],
    "Church Ave 2-5": [-73.9494551403533, 40.6508606878022],
    "Newkirk Ave 2-5": [-73.948299908224, 40.6399912427531],
    "Brooklyn College - Flatbush Ave 2-5": [-73.947541207344, 40.6328424070074],
    "Sterling St 2-5": [-73.9507289112493, 40.6627729934283],
    "Crown Hts - Utica Ave 3-4": [-73.9329325608185, 40.668978311078],
    "Kingston Ave 3-4": [-73.9421597839296, 40.6694814486497],
    "Nassau Ave G": [-73.9511830001652, 40.7244799978082],
    "Greenpoint Ave G": [-73.9544250014623, 40.7312669997146],
    "Marcy Ave J-M-Z": [-73.9578320007572, 40.7083830000179],
    "Hewes St J-M": [-73.9534880003845, 40.706889998054],
    "Metropolitan Ave G": [-73.9514239994525, 40.7127740007342],
    "Botanic Garden S": [-73.9592449994569, 40.6703426665843],
    "Franklin Ave - Fulton St S": [-73.9558270011042, 40.6805956659826],
    "Utica Ave A-C": [-73.9307289991402, 40.6793639995054],
    "Kosciuszko St J": [-73.9285089992741, 40.693172001292],
    "Gates Ave J-Z": [-73.9221560015075, 40.6895839990139],
    "18th Ave F": [-73.9769709996579, 40.6297546663858],
    "Ft Hamilton Pkwy N": [-74.0053510004627, 40.6313856672244],
    "25th Ave D": [-73.9868290001147, 40.5977036669585],
    "Myrtle-Willoughby Aves G": [-73.9490669989015, 40.6946189990376],
    "Flushing Ave G": [-73.9502340010257, 40.7003766662215],
    "Hoyt - Schermerhorn Sts A-C-G": [-73.9850362403413, 40.6884084758064],
    "Jay St - MetroTech A-C-F": [-73.9872181526731, 40.692470636847],
    "Flushing Ave J-M": [-73.9413773483836, 40.7004044029811],
    "Myrtle Ave J-M-Z": [-73.9356230012996, 40.6971950005145],
    "4th Av - 9th St F-G": [-73.9897789993889, 40.6702716672849],
    "Smith - 9th Sts F-G": [-73.9958917279093, 40.6736410609041],
    "Bergen St F-G": [-73.9907564957356, 40.6861105472597],
    "Jay St - MetroTech R": [-73.9860566785461, 40.6922553964532],
    "Court St R": [-73.9918183090112, 40.6941964807769],
    "Prospect Ave R": [-73.9928720006742, 40.6654136671297],
    "4th Av - 9th St R": [-73.9883019997451, 40.6708466668427],
    "59th St N-R": [-74.0178809995398, 40.6413616662838],
    "45th St R": [-74.0100060007493, 40.6489386666128],
    "36th St D-N-R": [-74.003548999518, 40.6551436663388],
    "9th Ave D": [-73.994448744512, 40.6464840772663],
    "Ft Hamilton Pkwy D": [-73.9942022375285, 40.6409127114446],
    "25th St R": [-73.9980909997429, 40.6603966669232],
    "Carroll St F-G": [-73.9949469799884, 40.6802733517017],
    "Hoyt St 2-3": [-73.9850637957564, 40.6905441853547],
    "Borough Hall 2-3": [-73.9899979996068, 40.693218999611],
    "Nostrand Ave 3": [-73.9504262489579, 40.6699381509305],
    "Clark St 2-3": [-73.9930859982196, 40.6974659999646],
    "Franklin Ave C": [-73.9568480001461, 40.6813796665874],
    "Clinton - Washington Aves C": [-73.9658379985727, 40.6832629991264],
    "York St F": [-73.9868849999367, 40.6997426676915],
    "High St A-C": [-73.9905310006545, 40.6993369997788],
    "Lafayette Ave C": [-73.973945998494, 40.6861130002056],
    "President St 2-5": [-73.950589200222, 40.6678836035368],
    "Cortelyou Rd Q": [-73.9637900550549, 40.6409401651401]
}


## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = 'nfa'

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 20 * 60 # 20 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#housing"

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
