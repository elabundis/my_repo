def check_factors(n):
    if n%15==0:
        return (3, 5)
    elif n%3==0:
        return 3
    elif n%5==0:
        return 5
    else:
        return None

n = int(input("Entero: "))
factors = check_factors(n)
print(f"factors: {factors}") if factors else  print('No factors')
