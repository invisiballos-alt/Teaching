print("w x y z | F")
# Перебираем все возможные комбинации значений переменных
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                # Записываем логическое выражение
                # Импликация (A -> B) в Python заменяется на (not A or B)

                F = not (not (z == x) or (w and z)) or (not (not y and z) or y)

                # Нас интересуют только строки, где функция равна 0
                # if F == 0:
                #     print(f"{w} {x} {y} {z} | {int(F)}")
