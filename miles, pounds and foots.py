d = {
        'сто':             100,
        'двести':          200,
        'триста':          300,
        'четыреста':       400,
        'пятьсот':         500,
        'шестьсот':        600,
        'семьсот':         700,
        'восемьсот':       800,
        'девятьсот':       900,
        'десять':          10,
        'одиннадцать':     11,
        'двенадцать':      12,
        'тринадцать':      13,
        'четырнадцать':    14,
        'пятнадцать':      15,
        'шестнадцать':     16,
        'семнадцать':      17,
        'восемнадцать':    18,
        'девятнадцать':    19,
        'двадцать':        20,
        'тридцать':        30,
        'сорок':           40,
        'пятьдесят':       50,
        'шестьдесят':      60,
        'семьдесят':       70,
        'восемьдесят':     80,
        'девяносто':       90,
        'одна':            1,
        'две':             2,
        'три':             3,
        'четыре':          4,
        'пять':            5,
        'шесть':           6,
        'семь':            7,
        'восемь':          8,
        'девять':          9
    }

miles = ['миля', 'мили', 'миль']
#kilometers = ['километр',]
s = '- Нет, Джон, у вас нет даже лошади для этого путешествия в двести пятьдесят миль.'

ss = s.split(' ')
print(ss)

#  s1 = [[ss.index(m), m] if m in ss else [-1, m] for m in miles]
#  ТАК НЕ ПОЛУЧИТСЯ, ПОТОМУ ЧТО К СЛОВУ МИЛЯ МОЖЕТ БЫТЬ ПРИЛЕПЛЕНА '.'

s1 = [[s.find(m), m] for m in miles]
s1.sort(key=lambda x: x[0], reverse=True)
p = s1[0][0]

s_ = s[:p]



print()
