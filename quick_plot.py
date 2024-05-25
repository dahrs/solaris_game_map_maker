import random

import matplotlib.pyplot as plt


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
