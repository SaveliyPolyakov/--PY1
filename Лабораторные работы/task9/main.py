salary = 5000  # зарплата
spend = 6000  # траты
months = 0  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
# TODO Оформить решение
for months in range(0, 10):
    delta = spend - salary
    spend = spend * (1+increase)
    need_money = need_money + delta
    months += 1
print(round(need_money))
