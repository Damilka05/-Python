money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
all_money = salary+money_capital
total = 0
while all_money >= spend:
    all_money -= spend
    spend += spend*increase
    all_money += salary
    total += 1

print("Количество месяцев, которое можно протянуть без долгов:", total)
