kvadro = [x**2 for x in range(1,11)]
print(kvadro)

chet = [x for x in range(1,20) if x%2==0]
print(chet)

words = ['python', 'Java', 'c++', 'Rust', 'go']
spisok = [x.upper() for x in words if len(x)>3]
print(spisok)


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

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Пример использования
for num in fibonacci(5):
    print(num)