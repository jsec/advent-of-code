def transpose(arr: list[list[str]]):
    return list(zip(*arr))[::-1]
