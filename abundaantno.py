def sumofdivisors(x):
    s=0
    for i in range (1,x-1):
        if (x%i==0):
            s=s+i
    return s

def check():
    dim = int(input("Enter choice: ")) 
    y=sumofdivisors(dim)
    if (y>dim):
        print ("Abundant no")
        p=y-dim
        print ("Abundance = ", p)
    else:
        print ("Not abundant no")

check()
tim = int(input("Enter choice: ")) 
