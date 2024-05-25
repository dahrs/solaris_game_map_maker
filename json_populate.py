import json
from random import randint
from collections import defaultdict
from typing import Union, List, Tuple, Dict, Callable


def star_natural_resources(a_key: str = 'default') -> Dict:
    nr = {
        'default': {
            "economy": randint(10, 50),
            "industry": randint(10, 50),
            "science": randint(10, 50)
                                  },
        'capitals': {
            "economy": 50,
            "industry": 50,
            "science": 50
                                  },
        'binaries': {
            "economy": randint(10, 50),
            "industry": randint(100, 150),
            "science": randint(10, 50)
                                  },
        'nebulas': {
            "economy": randint(40, 80),
            "industry": randint(10, 50),
            "science": randint(100, 170)
                                  },
        'asteroidfields': {
            "economy": randint(10, 50),
            "industry": randint(10, 50),
            "science": randint(10, 50)
                                  },
        'blackholes': {
            "economy": randint(1, 30),
            "industry": randint(1, 30),
            "science": randint(1, 30)
                                  },
        'pulsars': {
            "economy": randint(10, 50),
            "industry": randint(10, 50),
            "science": randint(10, 50)
                                  },
        'wormholes': {
            "economy": randint(10, 50),
            "industry": randint(10, 50),
            "science": randint(10, 50)
                                  },
        'stars': {
            "economy": randint(10, 50),
            "industry": randint(10, 50),
            "science": randint(10, 50)
                                  },
    }
    return nr[a_key]


def set_natural_resources(int_or_func: Union[int, Callable[[], int], ]) -> Dict:
    a_dict = {
        "economy": int_or_func,
        "industry": int_or_func,
        "science": int_or_func
    }
    return a_dict


def make_dictionary(capitals: List[Tuple[int, int]],
                    binaries: List[Tuple[int, int]],
                    nebulas: List[Tuple[int, int]],
                    asteroidfields: List[Tuple[int, int]],
                    blackholes: List[Tuple[int, int]],
                    pulsars: List[Tuple[int, int]],
                    wormholes: List[Tuple[int, int]],
                    stars: List[Tuple[int, int]],
                    warpgates: List[Tuple[int, int]],
                    players_stars: List[List[Tuple[int, int]]]
                    ) -> Dict:
    a_dict = defaultdict(lambda: {"id": None,
                                  "playerId": None,
                                  "homeStar": False,
                                  "location": {
                                      "x": None,
                                      "y": None},
                                  "naturalResources": {},
                                  "warpGate": False,
                                  "isNebula": False,
                                  "isAsteroidField": False,
                                  "isBinaryStar": False,
                                  "isBlackHole": False,
                                  "isPulsar": False,
                                  "wormHoleToStarId": None,
                                  "specialistId": None
                                  })
    ind = 0
    # capitals
    for cap in capitals:
        a_dict[cap]['id'] = ind
        a_dict[cap]['homeStar'] = True
        a_dict[cap]['location'] = {'x': cap[0], 'y': cap[1]}
        a_dict[cap]['naturalResources'] = star_natural_resources('binaries')
        ind += 1
    # binaries
    for st in binaries:
        a_dict[st]['id'] = ind
        a_dict[st]['isBinaryStar'] = True
        a_dict[st]['location'] = {'x': st[0], 'y': st[1]}
        a_dict[st]['naturalResources'] = star_natural_resources('binaries')
        ind += 1
    # nebulas
    for st in nebulas:
        a_dict[st]['id'] = ind
        a_dict[st]['isNebula'] = True
        a_dict[st]['location'] = {'x': st[0], 'y': st[1]}
        a_dict[st]['naturalResources'] = star_natural_resources('nebulas')
        ind += 1
    # asteroid fields
    for st in asteroidfields:
        a_dict[st]['id'] = ind
        a_dict[st]['isAsteroidField'] = True
        a_dict[st]['location'] = {'x': st[0], 'y': st[1]}
        a_dict[st]['naturalResources'] = star_natural_resources('asteroidfields')
        ind += 1
    # black holes
    for st in blackholes:
        a_dict[st]['id'] = ind
        a_dict[st]['isBlackHole'] = True
        a_dict[st]['location'] = {'x': st[0], 'y': st[1]}
        a_dict[st]['naturalResources'] = star_natural_resources('blackholes')
        ind += 1
    # pulsars
    for st in pulsars:
        a_dict[st]['id'] = ind
        a_dict[st]['isPulsar'] = True
        a_dict[st]['location'] = {'x': st[0], 'y': st[1]}
        a_dict[st]['naturalResources'] = star_natural_resources('pulsars')
        ind += 1
    # wormholes
    for wh0, wh1 in zip(wormholes[::2], wormholes[1::2]):
        a_dict[wh0]['id'] = ind
        a_dict[wh0]['wormHoleToStarId'] = ind + 1
        a_dict[wh0]['location'] = {'x': wh0[0], 'y': wh0[1]}
        a_dict[wh0]['naturalResources'] = star_natural_resources('wormholes')
        ind += 1
        a_dict[wh1]['id'] = ind
        a_dict[wh1]['wormHoleToStarId'] = ind - 1
        a_dict[wh1]['location'] = {'x': wh1[0], 'y': wh1[1]}
        a_dict[wh1]['naturalResources'] = star_natural_resources('wormholes')
        ind += 1
    # ordinary stars
    for st in stars:
        a_dict[st]['id'] = ind
        a_dict[st]['location'] = {'x': st[0], 'y': st[1]}
        a_dict[st]['naturalResources'] = star_natural_resources('stars')
        ind += 1
    # warpgates
    for st in warpgates:
        a_dict[st]['warpGate'] = True
    # players stars
    for player_id, play_strs in enumerate(players_stars):
        for st in play_strs:
            a_dict[st]['playerId'] = player_id
    return a_dict
