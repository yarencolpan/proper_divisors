def functioon(b):
    proper_divisors = []
    for i in range(2, b):
        if a % i == 0:
            proper_divisors.append(i)
    return proper_divisors


while True:
    print("Press 'p' to exit")
    a = input("Enter the number for which you want to determinant of proper divisors:")
    if a == "p":
        break
    else:
        a = int(a)
        print("proper_divisors:", functioon(a))
