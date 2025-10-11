#1
kvadro = [x**2 for x in range(1,11)]
print("Квадраты чисел: ", kvadro)

#2
chet = [x for x in range(1,20) if x%2==0]
print("Четные числа: ", chet)

#3
words = ['python', 'Java', 'c++', 'Rust', 'go']
spisok = [x.upper() for x in words if len(x)>3]
print("Слова в верхнем регистре, которые длиннее 3 символов: ", spisok)

#4
print("Итератор: \n")
class Countdown:
    #инициализируем, не вызывая вручную
    def __init__(self, n):
        self.n = n + 1
    #сам итератор
    def __iter__(self):
        return self
    #действие
    def __next__(self):
        self.n -= 1
        if self.n < 1:
            raise StopIteration
        return self.n


for x in Countdown(5):
    print(x)

#5
print("Фибоначчи: \n")
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

for num in fibonacci(5):
    print(num)

#6
from decimal import Decimal, getcontext

getcontext().prec = 28 #макс точность

#ввод данных
P = Decimal(input("Начальная сумма вклада (в рублях, c копейками): ").strip())
r = Decimal(input("Процентная ставка годовых: ").strip())
t = Decimal(input("Срок вклада(в годах): ").strip())

#расчет месячной ставки
monthly_rate = r / Decimal('100') / Decimal('12')
#расчет кол-ва месяцев
month = Decimal('12') * t

#расчет итоговой суммы
S = P * (Decimal('1') + monthly_rate) ** month
#расчет прибыли
profit = S - P

#вывод с точностью до копеек
print("Итоговая сумма: ", S.quantize(Decimal('0.01')))
print("Прибыль: ", profit.quantize(Decimal('0.01')))

#7
from fractions import Fraction

#создание дробей
f1 = Fraction(3, 4)
f2 = Fraction(5, 6)

#операции
summ = f1 + f2
vich = f1 - f2
ymnozenie = f1 * f2
delen = f1 / f2

#вывод результатов
print("Сумма: ", summ)
print("Вычитание: ", vich)
print("Умноженипе: ", ymnozenie)
print("Деление: ", delen)

#8
from datetime import datetime

now = datetime.now()

print("Текущая дата и время: ", now)
print("Текущая дата: ", now.date())
print("Текущее время: ", now.time())

#9
from datetime import date

#мой др
birthday = date(2005, 11, 13)

#сегодня
today = date.today()

#ск дней с рождения
days_passed = (today - birthday).days

#когда след др
next_birthday_year = today.year
if (today.month, today.day) > (birthday.month, birthday.day):
    next_birthday_year += 1
next_birthday = date(next_birthday_year, birthday.month, birthday.day)

#ск дней до след др
days_to_next = (next_birthday - today).days

print("С момента рождения прошло: ", days_passed)
print("Сколько дней осталось до следующего дня рождения: ", days_to_next)

#10
from datetime import datetime

def format_datetime(dt: datetime) -> str:
    months = [
        '', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
        'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'
    ]
    day = dt.day
    month = months[dt.month] #берет его как число
    year = dt.year
    hour = dt.hour
    minute = dt.minute
    return f'Сегодня {day} {month} {year} года, время: {hour:02d}:{minute:02d}'
time = datetime.now()
print(format_datetime(time))