def prime(number):
    if number >1:
        for i in range(2, number):
            if (number%i)==0:
                return False
        else:
            return True
    return False

def primeDivisor(a,b):
    osztok=[]
    for i in range(1, min(a,b)+1):
        if a%i==0 and b%i==0:
            osztok.append(i)
        else:
            continue
    for num in osztok[::-1]:
        if prime(num)==True:
            return num

a=int(input("a: "))
b=int(input("b: "))
print(a,b)
print(primeDivisor(a,b))