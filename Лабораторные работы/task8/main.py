money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0  # количество месяцев, которое можно прожить
overall = money_capital - spend  # Первый вычет трат без зарплаты
# TODO Оформить решение
while overall > 0:
    spend = spend * (1 + increase)
    overall = overall - spend + salary
    month = month + 1

print(month)
