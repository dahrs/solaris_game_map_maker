import json
import math
import random
from random import randint, sample
from collections import defaultdict
from typing import Union, List, Tuple, Dict, Callable


import numpy as np
import matplotlib.pyplot as plt


def make_circular_direction_coord(point_num: int, radius: int) -> List[Tuple[int, int]]:
    theta_zero = 2 * math.pi / point_num
    coord = []
    for n in range(0, point_num):
        coord.append((int(radius * math.cos(n * theta_zero)), int(radius * math.sin(n * theta_zero))))
    return coord


def make_star_coord(original: Tuple[int, int], max_radius: Union[int, float] = 10,
                    min_dist: Union[int, float] = 4) -> Tuple[int, int]:
    new_coord = (randint(original[0] - int(max_radius), original[0] + int(max_radius)),
                 randint(original[1] - int(max_radius), original[1] + int(max_radius)))
    while math.dist(original, new_coord) < min_dist:
        new_coord = (randint(original[0] - int(max_radius), original[0] + int(max_radius)),
                     randint(original[1] - int(max_radius), original[1] + int(max_radius)))
    return new_coord


def set_stars_near_capital(capitals: List[Tuple[int, int]],
                           number_of_stars: int = 100,
                           max_radius: Union[int, float] = 10,
                           min_dist: Union[int, float] = 4
                           ) -> List[Tuple[int, int]]:
    stars_coord = []
    ii_capital = 0
    while number_of_stars > 0:
        stars_coord.append(make_star_coord(capitals[ii_capital], max_radius, min_dist))
        number_of_stars -= 1
        ii_capital += 1
        ii_capital %= len(capitals)
    return stars_coord


def set_stars_random(other_stars: Union[None, List[Tuple[int, int]]] = None,
                     number_of_stars: int = 100,
                     max_radius: int = 100,
                     min_dist: Union[int, float] = 4,
                     ) -> List[Tuple[int, int]]:
    stars_coord = []
    other_stars = [] if other_stars is None else other_stars
    while number_of_stars > 0:
        new_coord = (randint(-max_radius, max_radius), randint(-max_radius, max_radius))
        for coord in other_stars + stars_coord:
            if math.dist(coord, new_coord) < min_dist:
                new_coord = None
                break
        if new_coord is not None:
            stars_coord.append(new_coord)
            number_of_stars -= 1
    return stars_coord


def set_stars_norm_random(other_stars: Union[None, List[Tuple[int, int]]] = None,
                          number_of_stars: int = 100,
                          min_dist: Union[int, float] = 4,
                          sigma: Union[float, int] = 35.0,
                          ) -> List[Tuple[int, int]]:
    stars_coord = []
    other_stars = [(0, 0)] if other_stars is None else other_stars
    while number_of_stars > 0:
        for coord in other_stars + stars_coord:
            new_coord = (int(np.random.normal(coord[0], sigma)), int(np.random.normal(coord[1], sigma)))
            if math.dist(coord, new_coord) > min_dist:
                stars_coord.append(new_coord)
                number_of_stars -= 1
    return stars_coord


def select_from_list(coord_list: List, amount: int) -> List:
    return sample(coord_list, amount)


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
                    stars_per_player
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
    # TODO: cluster a players closest stars and assign them
    return


def equitable_roundtable(player_amount: int,
                         map_size: int = 100,
                         total_stars: int = 100,
                         binaries_ratio: float = 0.1,
                         nebulas_ratio: float = 0.1,
                         asteroidfields_ratio: float = 0.1,
                         blackholes_ratio: float = 0.1,
                         pulsars_ratio: float = 0.1,
                         wormholes_ratio: float = 0.1,
                         warpgates_ratio: float = 0.1,
                         stars_per_player: Union[None, int] = None) -> Dict:
    stars_per_player = total_stars//player_amount if stars_per_player is None else stars_per_player
    radius = int(map_size / 2.0)
    # make capitals
    capitals = make_circular_direction_coord(player_amount, radius)
    near_capital_min = int(radius * 0.1) + 1
    near_capital_max = int(radius * 0.2) + near_capital_min + 1
    # binaries
    number_of_binaries = int(total_stars * binaries_ratio)
    # binaries = set_stars_near_capital(capitals, number_of_binaries, near_capital_max, near_capital_min)
    binaries = set_stars_norm_random(capitals, number_of_binaries, near_capital_min, sigma=30)
    # nebulas
    number_of_nebulas = int(total_stars * nebulas_ratio)
    # nebulas = set_stars_near_capital(capitals, number_of_nebulas, near_capital_max, near_capital_min)
    nebulas = set_stars_norm_random(capitals, number_of_nebulas, near_capital_min, sigma=45)
    # asteroid fields
    number_of_asteroidfields = int(total_stars * asteroidfields_ratio)
    # asteroidfields = set_stars_near_capital(capitals, number_of_asteroidfields, near_capital_max, near_capital_min)
    asteroidfields = set_stars_norm_random(capitals, number_of_asteroidfields, near_capital_min, sigma=45)
    # black holes
    number_of_blackholes = int(total_stars * blackholes_ratio)
    # blackholes = set_stars_near_capital(capitals, number_of_blackholes, near_capital_max, near_capital_min)
    blackholes = set_stars_norm_random(capitals, number_of_blackholes, near_capital_min, sigma=35)
    # pulsars
    number_of_pulsars = int(total_stars * pulsars_ratio)
    # pulsars = set_stars_near_capital(capitals, number_of_pulsars, near_capital_max, near_capital_min)
    pulsars = set_stars_norm_random(capitals, number_of_pulsars, near_capital_min, sigma=35)
    # wormholes
    number_of_wormholes = int(total_stars * wormholes_ratio)
    number_of_wormholes = number_of_wormholes if number_of_wormholes % 2 == 0 else number_of_wormholes + 1
    # wormholes = set_stars_near_capital(capitals, number_of_wormholes, near_capital_max, near_capital_min)
    wormholes = set_stars_norm_random(capitals, number_of_wormholes, near_capital_min, sigma=25)
    # normal stars
    total_stars -= player_amount + number_of_binaries + number_of_asteroidfields
    # stars = set_stars_random(binaries + nebulas + asteroidfields + blackholes + pulsars + wormholes,
    #                          total_stars, radius)
    stars = set_stars_norm_random(capitals, total_stars, near_capital_min, sigma=45)
    # warpgates # TODO need to separate?
    number_of_warpgates = int(total_stars * warpgates_ratio)
    warpgates = select_from_list(stars, number_of_warpgates)
    # plot
    quick_plot(capitals, binaries, nebulas, asteroidfields, blackholes, pulsars, wormholes, stars)
    # make dict
    solaris_dict = make_dictionary(capitals,
                                   binaries, nebulas, asteroidfields, blackholes, pulsars, wormholes,
                                   stars, warpgates, stars_per_player)
    return solaris_dict


def quick_plot(*args) -> None:
    markers = [",", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x",
               "X", "D", "d", "|", "_"]
    random.shuffle(markers)
    markers = [f'c{mm}' for mm in markers]
    for ii, coord_l in enumerate(args):
        marker = 'ro' if ii == 0 else None
        marker = 'b.' if ii == len(args) - 1 else marker
        marker = markers[ii] if marker is None else marker
        x, y = zip(*coord_l)
        plt.plot(x, y, marker)
    plt.show()
    return


def main(player_amount: int, map_size: int = 100, total_stars: int = 100,
         binaries_ratio: float = 0.1,
         nebulas_ratio: float = 0.1,
         asteroidfields_ratio: float = 0.1,
         blackholes_ratio: float = 0.1,
         pulsars_ratio: float = 0.1,
         wormholes_ratio: float = 0.1,
         warpgates_ratio: float = 0.1,
         capital_specialists: int = 1,
         galaxy_type: str = 'equitative_round_table',
         stars_per_player: Union[None, int] = None,
         out_path: str = './map.json') -> None:
    # TODO DEFINE TYPE OF GALAXY
    # TODO ADD SPECIALIST?
    equitable_roundtable(player_amount, map_size, total_stars, binaries_ratio, nebulas_ratio, asteroidfields_ratio,
    blackholes_ratio, pulsars_ratio, wormholes_ratio, warpgates_ratio, stars_per_player)
    # TODO save to json
    return


if __name__ == '__main__':
    main(7, 200, 100)

