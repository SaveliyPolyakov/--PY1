def get_unique_list_numbers(min, max, count) -> list[int]:
    from random import randint  # TODO написать функцию для получения списка уникальных целых чисел
    list_numbers = []
    while len(list_numbers) < count:
        i = randint(min, max)
        if i not in list_numbers:
            list_numbers.append(i)
    return list(list_numbers)


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
