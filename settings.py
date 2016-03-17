MAX_BART_DIST = 2
SLEEP_INTERVAL = 20 * 60 # 20 mins
MIN_PRICE = 1800
MAX_PRICE = 2900

SLACK_CHANNEL = "#cheaperhousing"

AREAS = ["eby", "sfc", "sby"] # "nby",

BART_STATIONS = {
    "oakland_19th": [37.8118051,-122.2720873],
    "macarthur": [37.8265657,-122.2686705],
    "rockridge": [37.841286,-122.2566329],
    "downtown_berkeley": [37.8629541,-122.276594],
    "north_berkeley": [37.8713411,-122.2849758]
}

NEIGHBORHOODS = ["berkeley north", "berkeley", "rockridge", "adams point", "oakland lake merritt", "cow hollow", "piedmont", "pac hts", "pacific heights", "lower haight", "inner sunset", "outer sunset", "presidio", "palo alto", "richmond / seacliff", "haight ashbury", "alameda", "twin peaks", "noe valley", "bernal heights", "glen park", "sunset", "mission district", "potrero hill", "dogpatch"]

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

try:
    from private import *
except Exception:
    pass