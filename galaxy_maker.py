from typing import Union, List, Tuple, Dict, Callable

from quick_plot import quick_plot
from coordinates import make_circular_direction_coord
from coordinates import make_star_coord, get_closest_coord_to_coord
from coordinates import set_stars_random, set_stars_norm_random, select_from_list, take_from_list


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
                         stars_per_player: Union[None, int] = None) -> Tuple[List, List, List, List, List, List, List, List, List, List]:
    stars_per_player = total_stars//player_amount if stars_per_player is None else stars_per_player
    radius = map_size // 2
    # make capitals
    capitals = make_circular_direction_coord(player_amount, radius)
    near_capital_min = int(radius * 0.1) + 1
    near_capital_max = int(radius * 0.2) + near_capital_min + 1
    # make some stars orbit around
    total_stars -= player_amount
    stars = set_stars_norm_random(capitals, total_stars, near_capital_min, sigma=45)
    # assign the given amount of stars to each player
    players_stars = []
    for capital_coord in capitals:
        players_stars.append([capital_coord] + get_closest_coord_to_coord(capital_coord, stars, stars_per_player))
    # set amount special stars
    number_of_binaries = int(total_stars * binaries_ratio)
    number_of_nebulas = int(total_stars * nebulas_ratio)
    number_of_asteroidfields = int(total_stars * asteroidfields_ratio)
    number_of_blackholes = int(total_stars * blackholes_ratio)
    number_of_pulsars = int(total_stars * pulsars_ratio)
    number_of_wormholes = int(total_stars * wormholes_ratio)
    number_of_wormholes = number_of_wormholes if number_of_wormholes % 2 == 0 else number_of_wormholes + 1
    number_of_warpgates = int(total_stars * warpgates_ratio)
    # set special stars
    binaries, stars = take_from_list(stars, number_of_binaries)
    nebulas, stars = take_from_list(stars, number_of_nebulas)
    asteroidfields, stars = take_from_list(stars, number_of_asteroidfields)
    blackholes, stars = take_from_list(stars, number_of_blackholes)
    pulsars, stars = take_from_list(stars, number_of_pulsars)
    wormholes, stars = take_from_list(stars, number_of_wormholes)
    warpgates = select_from_list(stars, number_of_warpgates)
    return capitals, binaries, nebulas, asteroidfields, blackholes, pulsars, wormholes, warpgates, stars, players_stars
