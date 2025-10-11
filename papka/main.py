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

getcontext().prec = 28

# Ввод данных
P = Decimal(input().strip())
r = Decimal(input().strip())
t = Decimal(input().strip())

# Расчет месячной ставки
monthly_rate = r / Decimal('100') / Decimal('12')

# Расчет экспоненты
exponent = Decimal('12') * t

# Расчет итоговой суммы
S = P * (Decimal('1') + monthly_rate) ** exponent

# Расчет прибыли
profit = S - P

# Вывод с точностью до копеек
print(S.quantize(Decimal('0.01')))
print(profit.quantize(Decimal('0.01')))