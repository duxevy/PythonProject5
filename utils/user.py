def user_interaction() -> tuple[int, int]:
    a, b = input().split()
    return int(a), int(b)

def parse_dict(data: dict[str, int]) -> tuple[list[str], list[int]]:
    keys = list(data.keys())
    values = list(data.values())
    return keys, values
