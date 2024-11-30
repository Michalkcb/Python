i = 1
end = int(input("podaj wartość końcową: "))
while i <= end:
    print(i, end=" ")
    if i % 2 == 0:
        print("- even")
    else:
        print("- odd")
                
    i += 1
