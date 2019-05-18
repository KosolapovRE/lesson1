def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    a = f"{one}{delimiter}{two}".upper()
    return a
b = get_summ('learn', 'python')
print(b)



def sum(a, b):
    return a+b

c = sum(2, 3)
print(c)
