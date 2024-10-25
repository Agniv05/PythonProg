def sumofdigits(x):
    s=0
    while x>0:
        a=x%10
        s=s+a
        x=x//10
    return s

def check():
     choice = int(input("Enter choice: "))  # Convert input to integer
     j=sumofdigits(choice)
     if (choice%j==0):
         print ("Harshad no")
     else:
         print("Not harshad no")

check()
dim = int(input("Enter choice: ")) 
