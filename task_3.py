salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев
i = 0
while i <= months - 1:    # первый месяц не учитывается
    money_capital += spend - salary
    spend *= 1 + increase   # увеличиваем расходы на 3%
    i += 1

print(round(money_capital))
# GitHub