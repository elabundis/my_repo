def check_factors(n):
    if n%15==0:
        print("divisible entre 3 y 5")
    elif n%3==0:
        print("divisible entre 3")
    elif n%5==0:
        print("divisible entre 5")
    else:
        print(n)
    return

n = int(input("Entero: "))
check_factors(n)
print("Goodbye")
