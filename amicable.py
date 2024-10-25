def sumofdivisors(x):
    s=0
    for i in range (1,x-1):
        if (x%i==0):
            s=s+i
    return s

def check():
    dim = int(input("Enter choice: ")) 
    for i in range (1,dim+1):
        t=sumofdivisors(i)
        m=sumofdivisors(t)
        if (i==m) and (i!=t):
            print (i," ",t)
            print(" ")

check()
mim = int(input("Enter choice: ")) 
