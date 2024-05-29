import json
from typing import Union, List, Tuple, Dict, Callable

from quick_plot import quick_plot
from json_populate import make_dictionary
from galaxy_maker import equitable_roundtable


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
    # TODO DEFINE OTHER TYPES OF GALAXIES
    galaxy_func = {
        'equitative_round_table': equitable_roundtable,
    }
    # TODO ADD SPECIALIST?
    (capitals, binaries, nebulas, asteroidfields, blackholes, pulsars, wormholes, warpgates,
     stars, players_stars) = galaxy_func[galaxy_type](player_amount, map_size, total_stars, binaries_ratio,
                                                      nebulas_ratio, asteroidfields_ratio, blackholes_ratio,
                                                      pulsars_ratio, wormholes_ratio, warpgates_ratio, stars_per_player)
    quick_plot(capitals, binaries, nebulas, asteroidfields, blackholes, pulsars, wormholes, warpgates, stars)
    # save to json
    json_d = make_dictionary(capitals, binaries, nebulas, asteroidfields, blackholes, pulsars,
                             wormholes, stars, warpgates, players_stars)
    json_l = {
        'stars': [dd for dd in json_d.values()],
        'carriers': [],
    }
    # dump to file
    with open(out_path, 'w', encoding='utf-8') as out_f:
        json.dump(json_l, out_f)
    return


if __name__ == '__main__':
    main(7, 250, 200,
         binaries_ratio=0.07,
         nebulas_ratio=0.07,
         asteroidfields_ratio=0.07,
         blackholes_ratio=0.07,
         pulsars_ratio=0.07,
         wormholes_ratio=0.07,
         warpgates_ratio=0.07,
         stars_per_player= 20,
         galaxy_type='equitative_round_table',
         out_path='./equitative_round_map.json',
         )
