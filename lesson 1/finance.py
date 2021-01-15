
reciept = int(input("Введите выручку фирмы: ")) # в этом примере будем оперировать целыми числами без копеек
costs = int(input("Введите издержки фирмы: "))
profit = reciept - costs
if profit > 0:
    print(f"Фирма получила прибыль: {profit} рублей")
    print(f"Рентабельность фирмы составила: {(profit/reciept*100):.2f}%")
    quantityEmployee = int(input("Введите число сотрудников: "))
    print(f"Прибыль на одного сотрудника составила: {(profit/quantityEmployee):.2f} рублей")
elif profit < 0:
    print(f"Фирма получила убыток: {-profit} рублей") # "-" для более корректной записи, убыток это уже минус
else:
    print("Фирма сработала в 0")
