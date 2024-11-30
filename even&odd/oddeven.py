end = int(input("podaj wartość końcową: "))
for i in range(1, end + 1):
    print(i, end=" ")
    if i % 2 == 0:
        print("- parzysta")
    else:
        print("- nieparzysta")
