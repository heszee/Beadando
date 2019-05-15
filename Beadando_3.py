def primeDivisor(a,b):
    osztok=[]
    n=1
    for i in range(1, min(a, b) + 1):
        if a%i==0 and b%i==0:
            osztok.append(i)
        else:
            continue
    for num in osztok[::-1]:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            return num


a=int(input("a: "))
b=int(input("b: "))
print(a,b)
print(primeDivisor(a,b))