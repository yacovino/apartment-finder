import os

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = 1000

# The maximum rent you want to pay per month.
MAX_PRICE = 2100

## Bedrooms

# Number of bedrooms
BEDROOMS = 2

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
     [40.657472,     -73.992406],
     [40.684611,     -73.970175],
    ],
    "gowanus": [
        [40.66508,      -73.997211],
        [40.678165,     -73.984938],
    ],
    "prospect_heights": [
        [40.671004,     -73.97275],
        [40.681875,     -73.959618],
    ],
    "crown_heights": [
        [40.663778,     -73.962193],
        [40.679792,     -73.947773],
    ],
    "fort_greene": [
        [40.682786,     -73.978415],
        [40.693394,     -73.970175],
    ],
    "clinton_hill": [
        [40.68207,      -73.969488],
        [40.693622,     -73.959017],
    ],
    "bed_stuy": [
        [40.67875,      -73.959446],
        [40.694745,     -73.947344],
    ],
    "south_slope": [
        [40.642875,     -73.987341],
        [40.660913,     -73.970947],
    ],
    "boerum hill": [
        [40.680638,     -73.994293],
        [40.690344,     -73.977975],
    ],
    "carroll gardens": [
        [40.671976,     -74.00341],
        [40.686447,     -73.989144],
    ],
    "cobble hill": [
        [40.683754,     -74.0007037],
        [40.6915438,    -73.9923513],
    ],
    "downtown brooklyn": [
        [40.686561,     -73.992383],
        [40.701431,     -73.978586],
    ],
    "brooklyn heights": [
        [40.689705,     -74.000205],
        [40.703001,     -73.990441],
    ],
    "dumbo": [
        [40.7014434,    -73.9945775],
        [40.7055669,    -73.9845085],
    ],
    "ditmas park": [
        [40.637225,     -73.972728],
        [40.64649,      -73.964725],
    ],
    "west lefferts gardens": [
        [40.65572,      -73.962728],
        [40.662068,     -73.956592],
    ],
    "kensington": [
        [40.630663,     -73.980232],
        [40.650006,     -73.97099],
    ],
    "prospect park south": [
        [40.643559,     -73.971234],
        [40.650592,     -73.964124],
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
                 "prospect heights"#,
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
                 "prospect park south"
                ]

## Transit preferences

# The farthest you want to live from a transit stop.
MAX_TRANSIT_DIST = 0.55 # kilometers

# Transit stations you want to check against.  Every coordinate here will be checked against each listing,
# and the closest station name will be added to the result and posted into Slack.
TRANSIT_STATIONS = {
    "Bergen St 2-3": [40.6808621368295, -73.974999151168],
    "Pennsylvania Ave 3": [40.6647144514356, -73.8948859115406],
    "Kingston - Throop Aves C": [40.679918999416, -73.9408589987126],
    "DeKalb Ave B-Q-R": [40.6906481199697, -73.9817709444094],
    "Chauncey St J-Z": [40.682851300878, -73.9103835703337],
    "Union St R": [40.6773156673509, -73.9831099990967],
    "Ralph Ave C": [40.6788220008733, -73.920785999333],
    "Franklin Ave 2-3-4-5": [40.6707651534489, -73.9580997367769],
    "Winthrop St 2-5": [40.6566593137607, -73.9500793459099],
    "Van Siclen Ave 3-4": [40.6655179630596, -73.889404917301],
    "Prospect Park B-Q-S": [40.6616334551018, -73.962031304266],
    "55th St D": [40.6314787609374, -73.9953488259574],
    "Ditmas Ave F": [40.6361186666629, -73.9781719996516],
    "Classon Ave G": [40.6888890002645, -73.9599900013721],
    "Broadway G": [40.7061265762741, -73.9503122560662],
    "Lorimer St L": [40.7140720006471, -73.9502479999697],
    "Sutter Ave L": [40.6691450006139, -73.9019160004208],
    "Wilson Ave L": [40.6888665424602, -73.9039586049186],
    "Halsey St J": [40.6864152707043, -73.9166388842194],
    "Lorimer St J-M": [40.703844000042, -73.947354998842],
    "8th Ave N": [40.6349709996471, -74.0115159977215],
    "Park Pl S": [40.6747716668526, -73.9576240007463],
    "Ocean Pkwy Q": [40.5763116670809, -73.9685009997517],
    "Bedford - Nostrand Aves G": [40.6896270015844, -73.9535220006402],
    "15th St - Prospect Park F-G": [40.6600356881002, -73.9797358059287],
    "7th Ave F-G": [40.6662446900198, -73.9802511790094],
    "Ft Hamilton Pkwy F-G": [40.6507816680341, -73.9757759991747],
    "Church Ave F-G": [40.6442720001299, -73.9797211622908],
    "Beverly Rd Q": [40.6439045986041, -73.9643577962312],
    "Church Ave B-Q": [40.6504932464648, -73.9628824619211],
    "Newkirk Ave B-Q": [40.6351419373378, -73.9626948683726],
    "Parkside Ave Q": [40.6550730416371, -73.9614534398764],
    "Grand Army Plaza 2-3-4": [40.6752946951032, -73.9709563319228],
    "Atlantic Av - Barclay's Center 2-3-4-5": [40.6844201652676, -73.9775499353938],
    "Rockaway Ave A-C": [40.6783399998835, -73.9119459972661],
    "Fulton St G": [40.6871189995077, -73.9753749983314],
    "Clinton - Washington Aves G": [40.6880940010605, -73.9667959986695],
    "7th Ave B-Q": [40.6771021798329, -73.9728527919102],
    "Atlantic Av - Barclay's Center B-Q": [40.6844883234536, -73.9767834396316],
    "Atlantic Av - Barclay's Center D-N-R": [40.6836656672794, -73.9788099995676],
    "Borough Hall 4-5": [40.692403999991, -73.9901510009053],
    "Nostrand Ave A-C": [40.6804380000622, -73.9504260009968],
    "Nevins St 2-3-4-5": [40.6883105801902, -73.9804067987457],
    "Eastern Pkwy - Bklyn Museum 2-3-4": [40.6720322354592, -73.9642220374842],
    "Beverly Rd 2-5": [40.6451235189437, -73.948847983817],
    "Church Ave 2-5": [40.6508606878022, -73.9494551403533],
    "Newkirk Ave 2-5": [40.6399912427531, -73.948299908224],
    "Brooklyn College - Flatbush Ave 2-5": [40.6328424070074, -73.947541207344],
    "Sterling St 2-5": [40.6627729934283, -73.9507289112493],
    "Crown Hts - Utica Ave 3-4": [40.668978311078, -73.9329325608185],
    "Kingston Ave 3-4": [40.6694814486497, -73.9421597839296],
    "Nassau Ave G": [40.7244799978082, -73.9511830001652],
    "Greenpoint Ave G": [40.7312669997146, -73.9544250014623],
    "Marcy Ave J-M-Z": [40.7083830000179, -73.9578320007572],
    "Hewes St J-M": [40.706889998054, -73.9534880003845],
    "Metropolitan Ave G": [40.7127740007342, -73.9514239994525],
    "Grand St L": [40.7115760006482, -73.9404969987464],
    "Graham Ave L": [40.7145759983636, -73.9439439986903],
    "Bedford Ave L": [40.7171739985889, -73.9566649980652],
    "Montrose Ave L": [40.7073910643845, -73.939792847135],
    "Atlantic Ave L": [40.675344666408, -73.9030969995401],
    "Halsey St L": [40.6955180011487, -73.9039340011863],
    "Myrtle - Wyckoff Aves L": [40.6994710624271, -73.9109757182647],
    "New Lots Ave 3": [40.6663149325969, -73.8841107080032],
    "Van Siclen Ave C": [40.672709999061, -73.8903580002471],
    "Cleveland St J": [40.6797779989611, -73.8851940021643],
    "Livonia Ave L": [40.6640572709464, -73.9005623722605],
    "Junius St 3": [40.6635890018172, -73.9024486418356],
    "Rockaway Ave 3": [40.6626174881522, -73.9089583358444],
    "Canarsie - Rockaway Pkwy L": [40.6466536673952, -73.9018500001728],
    "E 105th St L": [40.6504687854469, -73.8995476938872],
    "Saratoga Ave 3": [40.6615297898075, -73.9163302500794],
    "Sutter Ave - Rutland Road 3": [40.6647667887749, -73.92252118536],
    "New Lots Ave L": [40.6589147736852, -73.8992779605714],
    "Broadway Junction J-Z": [40.6793660014736, -73.9042899974641],
    "Alabama Ave J": [40.6769980000037, -73.8985260015965],
    "Shepherd Ave C": [40.6741300014559, -73.8807499974726],
    "Crescent St J-Z": [40.6831526570773, -73.8739292521577],
    "Cypress Hills J": [40.6896160008387, -73.8733219988299],
    "Myrtle - Wyckoff Aves M": [40.6994540009083, -73.912178999396],
    "Seneca Ave M": [40.702918998949, -73.9075819988542],
    "DeKalb Ave L": [40.7036929996164, -73.9182320021972],
    "Botanic Garden S": [40.6703426665843, -73.9592449994569],
    "Bushwick - Aberdeen L": [40.6828606255118, -73.905261763051],
    "Broadway Junction L": [40.6784562484286, -73.9031175792068],
    "Franklin Ave - Fulton St S": [40.6805956659826, -73.9558270011042],
    "Utica Ave A-C": [40.6793639995054, -73.9307289991402],
    "Kosciuszko St J": [40.693172001292, -73.9285089992741],
    "Gates Ave J-Z": [40.6895839990139, -73.9221560015075],
    "Central Ave M": [40.6978730001183, -73.9272429990283],
    "Knickerbocker Ave M": [40.698660001238, -73.9197200018862],
    "Jefferson St L": [40.7066066659887, -73.9229130000312],
    "Morgan Ave L": [40.7061516668072, -73.933147000242],
    "18th Ave F": [40.6297546663858, -73.9769709996579],
    "77th St R": [40.6297416668869, -74.0255099996266],
    "Bay Ridge Ave R": [40.6349666668237, -74.0233769995072],
    "50th St D": [40.6362608909613, -73.9946587805514],
    "Ft Hamilton Pkwy N": [40.6313856672244, -74.0053510004627],
    "25th Ave D": [40.5977036669585, -73.9868290001147],
    "Bay Pky D": [40.6019504615723, -73.9936762000529],
    "20th Ave N": [40.617108999866, -73.9845219984611],
    "18th Ave N": [40.62068699768, -73.9904539986599],
    "Bay Ridge - 95th St R": [40.6166216672595, -74.0308760008576],
    "86th St R": [40.6226866671502, -74.0283979999864],
    "79th St D": [40.6131589256951, -74.000582874315],
    "71st St D": [40.6192587097727, -73.9988409485068],
    "20th Ave D": [40.6046769981693, -73.9981743215756],
    "18th Ave D": [40.6077357317174, -74.001592592394],
    "62nd St D": [40.6262244629221, -73.9968572499486],
    "New Utrecht Ave N": [40.6248416672588, -73.9963530002596],
    "Ave U F": [40.5959248255174, -73.9733764197488],
    "Kings Hwy F": [40.6032584051282, -73.9723553085244],
    "Brighton Beach B-Q": [40.5777101966424, -73.9613537859879],
    "Sheepshead Bay B-Q": [40.5865475470753, -73.954057912579],
    "Ave U Q": [40.5993089509547, -73.955811223163],
    "Kings Hwy B-Q": [40.608638645396, -73.9576087353808],
    "Ave U N": [40.5972359999204, -73.9790840009942],
    "Kings Hwy N": [40.6040589998049, -73.9803730022934],
    "Neptune Ave F": [40.5807387584914, -73.974592728188],
    "Ave X F": [40.5894496666252, -73.974265999689],
    "Bay 50th St D": [40.5888406665193, -73.9837650004594],
    "Gravesend - 86th St N": [40.5924650008885, -73.9781889993627],
    "Ave P F": [40.6088428089499, -73.9730028152875],
    "Ave N F": [40.6143567119088, -73.9740485087314],
    "Bay Pky F": [40.6207316231678, -73.9752569782215],
    "Ave M Q": [40.6173977444437, -73.9592431052215],
    "Bay Pky N": [40.61145578989, -73.9817800106929],
    "Ave I F": [40.6250174401914, -73.9760693317092],
    "Ave J Q": [40.6250228199151, -73.9606931624692],
    "Ave H Q": [40.6292083775896, -73.9615179394249],
    "Neck Rd Q": [40.5953216911169, -73.9550782749376],
    "Myrtle-Willoughby Aves G": [40.6946189990376, -73.9490669989015],
    "Flushing Ave G": [40.7003766662215, -73.9502340010257],
    "Hoyt - Schermerhorn Sts A-C-G": [40.6884084758064, -73.9850362403413],
    "Jay St - MetroTech A-C-F": [40.692470636847, -73.9872181526731],
    "Flushing Ave J-M": [40.7004044029811, -73.9413773483836],
    "Myrtle Ave J-M-Z": [40.6971950005145, -73.9356230012996],
    "4th Av - 9th St F-G": [40.6702716672849, -73.9897789993889],
    "Smith - 9th Sts F-G": [40.6736410609041, -73.9958917279093],
    "Bergen St F-G": [40.6861105472597, -73.9907564957356],
    "Jay St - MetroTech R": [40.6922553964532, -73.9860566785461],
    "Court St R": [40.6941964807769, -73.9918183090112],
    "Prospect Ave R": [40.6654136671297, -73.9928720006742],
    "4th Av - 9th St R": [40.6708466668427, -73.9883019997451],
    "Liberty Ave C": [40.6745419998708, -73.8965480010392],
    "Broadway Junction A-C": [40.6783336660802, -73.9053160005534],
    "59th St N-R": [40.6413616662838, -74.0178809995398],
    "45th St R": [40.6489386666128, -74.0100060007493],
    "36th St D-N-R": [40.6551436663388, -74.003548999518],
    "9th Ave D": [40.6464840772663, -73.994448744512],
    "53rd St R": [40.6450686673598, -74.0140339998631],
    "Ft Hamilton Pkwy D": [40.6409127114446, -73.9942022375285],
    "25th St R": [40.6603966669232, -73.9980909997429],
    "Carroll St F-G": [40.6802733517017, -73.9949469799884],
    "Hoyt St 2-3": [40.6905441853547, -73.9850637957564],
    "Borough Hall 2-3": [40.693218999611, -73.9899979996068],
    "Nostrand Ave 3": [40.6699381509305, -73.9504262489579],
    "Clark St 2-3": [40.6974659999646, -73.9930859982196],
    "Franklin Ave C": [40.6813796665874, -73.9568480001461],
    "Clinton - Washington Aves C": [40.6832629991264, -73.9658379985727],
    "York St F": [40.6997426676915, -73.9868849999367],
    "High St A-C": [40.6993369997788, -73.9905310006545],
    "Lafayette Ave C": [40.6861130002056, -73.973945998494],
    "President St 2-5": [40.6678836035368, -73.950589200222],
    "Cortelyou Rd Q": [40.6409401651401, -73.9637900550549],
    "Coney Island - Stillwell Av D-F-N-Q": [40.5772810000675, -73.9812359981396]
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
SLACK_CHANNEL = "#apartments_no_fee"

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
