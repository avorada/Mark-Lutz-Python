formatter = "{} {} {} {} "# переменная

print(formatter.format(1, 2, 3, 4))# с помощью метода(функции) format передали в переменную следующие значения
print(formatter.format("one", "two", "three", "four", "five"))# если вставить больше переменных, чем есть изначально ихх просто проигнорируют(вроде как), ошибки нет
print(formatter.format(True, False, False, True))#
print(formatter.format(formatter, formatter, formatter, formatter))#передали в каждую ячейку до ячейки)0)
print(formatter.format( "Спят в конюшне пони,",
                        "начал пес дремать,",
                        "только мальчик Джонни",
                        "не ложиться спать"
))
