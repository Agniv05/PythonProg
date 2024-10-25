import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime

def greeting(hour):
    if hour >= 22 or hour < 4:
        print("Good night")
    elif 4 <= hour < 12:
        print("Good Morning")
    elif 12 <= hour < 17:
        print("Good Afternoon")
    elif 17 <= hour < 22:
        print("Good Evening")

y=int(time.strftime('%H'))
greeting(y)
mim = int(input("Enter choice: ")) 