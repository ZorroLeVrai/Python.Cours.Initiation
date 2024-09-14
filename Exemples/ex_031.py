def next_syracuse_term(nb):
    if nb % 2 == 0:
        # nb est pair
        return nb / 2
    else:
        # nb est impair
        return nb * 3 + 1
