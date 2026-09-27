
def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    grid = [["." for _ in range(dim)] for _ in range(dim)]
    for r, c in stars:
        if 0 <= r < dim and 0 <= c < dim:
            grid[r][c] = "*"
    return ["".join(row) for row in grid]

