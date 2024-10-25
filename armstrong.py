def countdig(x):
    s = 0
    while x > 0:
        s += 1
        x //= 10  # Integer division to remove last digit
    return s

def newno(x, y):
    m = 0
    while x > 0:
        a = x % 10  # Extract last digit
        b = pow(a, y)
        m += b
        x //= 10  # Move to next digit
    return m

def check():
    choice = int(input("Enter choice: "))  # Convert input to integer
    t = countdig(choice)
    f = newno(choice, t)
    if f == choice:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

check()
choice = int(input("Enter choice: "))  # Convert input to integer
