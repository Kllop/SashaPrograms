sumbol = input("Ведите операцию: ")
n = input("Введите первое число ")
s = input("Введите второе число ")
if (sumbol == '+'):
    t = int(n)+int(s)
    print("сумма равна ", t)
elif (sumbol == '-'):
    t = int(n)-int(s)
    print("разность равна ", t)
elif (sumbol == '*'):
    t = int(n)*int(s)
    print("произведение равно ", t)
elif (sumbol == "/"):
    t = int(n)/int(s)
    print("часное равно", t)
else:
    print("неправильная операция")