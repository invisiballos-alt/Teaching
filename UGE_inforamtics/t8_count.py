from itertools import product

count = 0
# Перебираем все комбинации длиной 5 из восьмеричных цифр
for p in product('01234567', repeat=5):
    num = ''.join(p)
    # Первая цифра не 0, ровно две двойки, и две двойки не стоят подряд
    if num[0] != '0' and num.count('2') == 2 and '22' not in num:
        count += 1

print(count)
