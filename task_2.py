# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

n = int(input ('Введите количество журавликов :', ))

x = n//6

print(n, "->", x, x*4, x)


# Введите количество журавликов :6
# 6 -> 1 4 1
# Введите количество журавликов :24
# 24 -> 4 16 4
# Введите количество журавликов :60
# 60 -> 10 40 10