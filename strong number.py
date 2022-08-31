input = int(input("sayı giriniz: "))
for i in range(1, input+1):
    num = i
    sum = 0
    while num > 0:
        digit = num % 10
        num = num//10
        factorial = 1
        for j in range(1, digit+1):
            factorial *= j
        sum += factorial

    if sum == i:
        print(i)
