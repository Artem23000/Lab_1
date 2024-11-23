money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month = 0  # Кол-во месяцев
all_money = 0  # Все доступные деньги (бюджет)

while all_money >= 0:
    all_money = (money_capital + salary) - spend

    if all_money > 0:
        money_capital = (money_capital - spend) + salary
        spend *= 1 + increase
        month += 1
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", month)
