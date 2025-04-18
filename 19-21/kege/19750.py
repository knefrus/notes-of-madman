#19
def N(k, pos, end):
    if k <= 19 and pos == end:
        return True
    if k <= 19 and pos != end:
        return False
    if k > 19 and pos == end:
        return False
    else:
        if pos % 2 == 1:

            if k % 2 == 0:
                return (k - 5, pos + 1, end) or (k / 2, pos + 1, end)
            if k % 3 == 0:
                return (k - 5, pos + 1, end) or (k / 3, pos + 1, end)
            if k % 2 != 0 or k % 3 != 0:
                return (k - 5, pos + 1, end) or (k + 1, pos + 1, end)

        else:

            if k % 2 == 0:
                return (k - 5, pos + 1, end) and (k / 2, pos + 1, end)
            if k % 3 == 0:
                return (k - 5, pos + 1, end) and (k / 3, pos + 1, end)
            if k % 2 != 0 and k % 3 != 0:
                return (k - 5, pos + 1, end) and (k + 1, pos + 1, end)


def ZOV(k):
    a = [k-5]
    if k % 2 == 0:
        a.append(k / 2)
    if k % 3 == 0:
        a.append(k / 3)
    if k % 2 != 0 and k % 3 != 0:
        a.append(k + 1)

for i in range(19, 29):
    if N(i, 1, 4):
        print(i)













"""
№ 19750 (Уровень: Средний)
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может выполнить любое из следующих действий:
1) убрать из кучи пять камней;
2) если количество камней в куче чётно, уменьшить его в два раза;
3) если количество камней в куче кратно трём, уменьшить его в три раза;
4) если количество камней в куче нечётно и не кратно трём, добавить один камень.
Например, если в куче 12 камней, то за один ход можно получить 7, 6 или 4 камня, а если в куче 11 камней, то за один ход можно получить 6 или 12 камней. Игра завершается, когда количество камней в куче становится не более 19. Победителем считается игрок, сделавший последний ход, то есть первым получивший кучу, в которой будет 19 или меньше камней. В начале игры в куче было S камней, S > 19
Укажите минимальное значение S, при котором Петя не может выиграть первым ходом, но при любом первом ходе Пети Ваня может выиграть своим первым ходом.

Задание 20.
Для игры, описанной в задании 19, найдите два наименьших значения     S, при которых Петя не может выиграть первым ходом, но у Пети есть выигрышная стратегия, позволяющая ему выиграть вторым ходом при любой игре Вани.
В ответе запишите найденные значения в порядке возрастания.

Задание 21.
Для игры, описанной в задании 19, найдите минимальное значение S, при котором у Вани есть стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети, но у Вани нет стратегии, которая позволила бы ему гарантированно выиграть первым ходом.
"""
