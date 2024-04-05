a = [1, 2, 5, 4, 12, 16, 21]
for i in a:
    if i%5 == 0:
        print(i)
        break
else:
    print("Not found")