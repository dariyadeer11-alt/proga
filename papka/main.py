kvadro = [x**2 for x in range(1,11)]
print(kvadro)

chet = [x for x in range(1,20) if x%2==0]
print(chet)

words = ['python', 'Java', 'c++', 'Rust', 'go']
spisok = [x.upper() for x in words if len(x)>3]
print(spisok)