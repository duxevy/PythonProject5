def sort_by_digit(data: list[int]) -> list[int]:
    """
    Сортирует числа
    :param data: список чисел
    :return: отсортированный список чисел
    """
    return sorted(data)

def filter_by_state(operations: list[dict], state: str = "EXECUTED"):
    return [oper_ for oper_ in operations if oper_["state"] == state]

print()
