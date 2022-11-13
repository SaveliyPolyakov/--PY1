import random


def get_random_password() -> str:
    bank = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm123456789'  # TODO написать функцию генерации
    # случайных паролей
    password = ''
    i = random.sample(bank, 8)
    password += str(i)
    return password


print("".join(get_random_password()))
