def collatz(number) :
    if number % 2 == 0 :
        return number, '//2'
    else :
        return 3 * number + 1

print(collatz(11))
print(collatz(22))
print(collatz(33))
print(collatz(44))