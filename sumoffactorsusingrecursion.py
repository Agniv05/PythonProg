def sumoffactors(x,i=1):   #sum of factors using recursion
    if (x==i):
        return 0
    if x % i == 0:
        return i + sumoffactors(x, i + 1)
    else:
        return sumoffactors(x, i + 1)

mim = int(input("Enter choice: ")) 
sumoffactors(mim)
nim = int(input("Enter choice: ")) 