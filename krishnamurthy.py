def factorial(x):
    b=1
    for i in range(1,x+1):
        b=b*i
    return b

def check():
    dim = int(input("Enter choice: ")) 
    k=dim
    s=0
    while (dim>0):
        d=dim%10
        t=factorial(d)
        s=s+t
        dim=dim//10
    if (k==s):
        print ("Krishna murthy no.")
    else:
        print ("not krishna murthy no")

check()
bim = int(input("Enter choice: ")) 