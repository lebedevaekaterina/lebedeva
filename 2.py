a=input("Введите номер: \n")
a=int(a)
if a % 2 ==0 and a < 37:
    print("Верхнее")
elif a % 2 != 0 and a < 37:
    print("Нижнее")
elif a % 2 == 0 and a >= 37:
    print("Верхнее боковое")
else:
    print("Нижнее боковое")