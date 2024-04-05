a = int(input("Enter a number: "))
i = 2
while i<a:
    if a%i == 0:
        print(i)
        break
    i+=1
else:
    print("Not found!")