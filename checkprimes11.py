
number = int(input('Type a number to check if prime: '))
a = [x for x in range(2, number) if number % x == 0]


def isPrime(n):
    
    if n == 1:
        return False
    
    if len(a) == 0:
        return True
    else:
        return False


print(isPrime(number))