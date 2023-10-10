x = int(input())
kol = 0

if x <= 2000000000:
    for i in range(1, x+1, 1):
        if x % i == 0:
            kol += 1
    print(kol)
else:
    print('Это долго считать, давай другое число)')