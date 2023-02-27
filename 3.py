a=input("Введите год: \n")
a=int(a)
if a % 4 ==0 and (a % 100 != 0 or a % 400 ==0):
    print("Год "+ str(a) + " - високосный")
else:
    print("Год "+ str(a) + " - не високосный")