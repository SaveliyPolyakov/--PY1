def get_unique_list_numbers() -> list[int]:
    from random import randint  # TODO написать функцию для получения списка уникальных целых чисел
    start = -10
    stop = 10
    count = 15
    list_numbers = set([randint(start, stop) for _ in range(count)])
    return list(list_numbers)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
