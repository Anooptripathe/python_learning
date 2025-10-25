a=10
b=5

print("Open file")
try:
    c=a/b
    print(c)

    print("Enter a number:")
    x=int(input())

except ZeroDivisionError:
    print("You cannot divide number by zero")

except ValueError:
    print("Please enter valid number")

except Exception:
    print("Something went wrong:")

finally:
    print("Close the file")