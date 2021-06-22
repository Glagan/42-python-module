import math


class TinyStatistician:
    def __init__(self):
        pass

    def mean(self, x: list) -> float:
        if not x:
            return None
        return sum(x) / len(x)

    def median(self, x: list) -> float:
        if not x:
            return None
        return self.quartile(x, 50)

    def quartile(self, lst: list, percentile: int) -> float:
        """
        Closest ranks with linear interpolation (C = 1)
        https://en.wikipedia.org/wiki/Percentile
        """
        if not lst:
            return None
        lst = sorted(lst)
        count = len(lst)
        x = (percentile / 100) * (count - 1)
        x_floor = math.floor(x)
        value = x_floor if x_floor >= 0 else 0
        value_next = x_floor + \
            1 if (x_floor + 1) < count - 1 else count - 1
        in_serie = lst[value]
        next_in_serie = lst[value_next]
        frac = x - x_floor
        return in_serie + frac * (next_in_serie - in_serie)

    def var(self, x: list) -> float:
        if not x:
            return None
        mean = self.mean(x)
        return sum((row - mean) ** 2 for row in x) / len(x)

    def std(self, x: list) -> float:
        if not x:
            return None
        return math.sqrt(self.var(x))
