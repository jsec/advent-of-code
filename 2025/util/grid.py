neighbor_map = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (0, -1), (0, 1), (1, 0)]


class Grid:
    height: int
    width: int
    data: list[list[str]]

    def __init__(self, data: list[list[str]]) -> None:
        self.data = data
        self.height = len(data)
        self.width = len(data[0])

    def in_bounds(self, x: int, y: int):
        if x < 0 or x >= self.height:
            return False

        if y < 0 or y >= self.width:
            return False

        return True

    def neighbors(self, x: int, y: int):
        neighbors: list[tuple[int, int]] = []

        candidates = map(lambda t: (t[0] + x, t[1] + y), neighbor_map)
        for cx, cy in candidates:
            if self.in_bounds(cx, cy):
                neighbors.append((cx, cy))

        return neighbors

    def at(self, x: int, y: int):
        return self.data[x][y]

    def set(self, x: int, y: int, value: str):
        self.data[x][y] = value
