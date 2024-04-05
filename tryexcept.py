a = 5
b = 2
try:
    print(a/b)
except ZeroDivisionError as e:
    print("You cannot divide a number by zero")
except Exception as e:
    print("Something went wrong!", e)