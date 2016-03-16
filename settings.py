MAX_BART_DIST = 2
SLEEP_INTERVAL = 60 * 60 # 1 hour

AREAS = ["eby", "sfc"] # , "sby", "nby",

BART_STATIONS = {
    "oakland_19th": [37.8118051,-122.2720873],
    "macarthur": [37.8265657,-122.2686705],
    "rockridge": [37.841286,-122.2566329],
    "downtown_berkeley": [37.8629541,-122.276594],
    "north_berkeley": [37.8713411,-122.2849758]
}

NEIGHBORHOODS = ["berkeley north", "berkeley", "rockridge", "adams point", "oakland lake merritt", "cow hollow", "piedmont", "pac hts", "pacific heights"]

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
    ]
}

try:
    from private import *
except Exception:
    pass