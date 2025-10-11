#1
kvadro = [x**2 for x in range(1,11)]
print(kvadro)

#2
chet = [x for x in range(1,20) if x%2==0]
print(chet)

#3
words = ['python', 'Java', 'c++', 'Rust', 'go']
spisok = [x.upper() for x in words if len(x)>3]
print(spisok)

#4
class Countdown:
    def __init__(self, n):
        self.n = n + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.n -= 1
        if self.n < 1:
            raise StopIteration
        return self.n


for x in Countdown(5):
    print(x)

#5
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Пример использования
for num in fibonacci(5):
    print(num)

#6
from decimal import Decimal, getcontext

getcontext().prec = 28 #макс точность

# Ввод данных
P = Decimal(input("Начальная сумма вклада (в рублях, c копейками)").strip())
r = Decimal(input("Процентная ставка годовых").strip())
t = Decimal(input("Срок вклада(в годах)").strip())

# Расчет месячной ставки
monthly_rate = r / Decimal('100') / Decimal('12')

# Расчет экспоненты
month = Decimal('12') * t

# Расчет итоговой суммы
S = P * (Decimal('1') + monthly_rate) ** month

# Расчет прибыли
profit = S - P

# Вывод с точностью до копеек
print(S.quantize(Decimal('0.01')))
print(profit.quantize(Decimal('0.01')))

#7
from fractions import Fraction

# Создание дробей
f1 = Fraction(3, 4)
f2 = Fraction(5, 6)

# Операции
addition = f1 + f2
subtraction = f1 - f2
multiplication = f1 * f2
division = f1 / f2

# Вывод результатов
print(addition)
print(subtraction)
print(multiplication)
print(division)

#8
from datetime import datetime

now = datetime.now()

print("Текущая дата и время", now)
print("Текущая дата:", now.date())
print("Текущее время:", now.time())

#9
from datetime import date

# День рождения
birthday = date(2005, 11, 13)

# Текущая дата
today = date.today()

# Сколько дней прошло с момента рождения
days_passed = (today - birthday).days

# Определение следующего дня рождения
next_birthday_year = today.year
if (today.month, today.day) > (birthday.month, birthday.day):
    next_birthday_year += 1
next_birthday = date(next_birthday_year, birthday.month, birthday.day)

# Сколько дней до следующего дня рождения
days_to_next = (next_birthday - today).days

# Вывод результатов
print(days_passed)
print(days_to_next)