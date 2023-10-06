def table(x):
    print("------[" + str(x) + "단]------")
    for y in range(1, 20):
        print(x, "X", y, "=", x*y)

a = int(input("몇 단까지 출력할까요?"))

for y in range(2, a+1):
    table(y)
