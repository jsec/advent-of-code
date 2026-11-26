def transpose(arr: list[list[str]]):
    return list(zip(*arr, strict=False))[::-1]
