import math
import heapq
from random import randint, sample
from typing import Union, List, Tuple, Dict, Callable, Any

import numpy as np


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


def select_from_list(coord_list: List, amount: int) -> List[Tuple[int, int]]:
    return sample(coord_list, amount)


def take_from_list(coord_list: List, amount: int) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    amount_list = sample(coord_list, amount)
    remaining_list = [coord for coord in coord_list if coord not in amount_list]
    return amount_list, remaining_list


def naive_euclidian_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    return sum([(point1[x] - point2[x]) ** 2 for x in range(len(point1))]) ** 0.5


def get_closest_coord_to_coord(coord: Tuple[int, int], coord_stars: List[Tuple[int, int]],
                               num_stars: int) -> List[Tuple[int, int]]:
    cluster = []
    for star in coord_stars:
        heapq.heappush(cluster, (naive_euclidian_distance(coord, star), star))
    while len(cluster) < num_stars:
        dist, star_coord = heapq.heappop(cluster)
        cluster.append(star_coord)
    return cluster
