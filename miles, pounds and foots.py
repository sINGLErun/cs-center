from num2words import num2words

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
kilometers = ['километр', 'километра', 'километров']
s = '''- Нет, Джон, у вас нет даже лошади для этого путешествия
 в девятьсот миль. Это будет очень опасно!'''
# s = input()
# входная строка, дальше её стоит заменить на input()

s_ = [[s.find(m), m] for m in miles]
s_.sort(key=lambda x: x[0], reverse=True)
p = s_[0][0]

s1 = s[:p-1]
s2 = s1.split(' ')

k = -1
word = s2[k]
miles_number = 0
while word in list(d.keys()):
    miles_number += d[word]
    k -= 1
    word = s2[k]

kilometers_number = int(round(miles_number*1.61, 0))

# чтобы не писать странное "одна" для тысяч
if kilometers_number // 1000 == 1:
    numerical = ' '.join(num2words(kilometers_number, lang='ru').split(' ')[1:]) + ' '
else:
    numerical = num2words(kilometers_number, lang='ru') + ' '

s1 = ' '.join(s2[:k+1]) + ' ' + numerical

if kilometers_number % 10 == 1:
    kilometers_word = kilometers[0]
elif 2 <= kilometers_number % 10 < 5:
    kilometers_word = kilometers[1]
elif 5 <= kilometers_number % 10 or kilometers_number % 10 == 0:
    kilometers_word = kilometers[2]

s1 = s1 + kilometers_word + s[p + len(s_[0][1]):]
print(s1)
# ЕБАТЬ, ДА!
