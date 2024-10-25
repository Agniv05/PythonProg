def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def rotate_number(num):
    rotations = []
    str_num = str(num)
    for i in range(len(str_num)):
        rotated = str_num[i:] + str_num[:i]
        rotations.append(int(rotated))
    return rotations

def is_circular_prime(n):
    rotations = rotate_number(n)
    for rotation in rotations:
        if not is_prime(rotation):
            return False
    return True

number = int(input("Enter a number to check if it's a circular prime: "))
if is_circular_prime(number):
    print(f"{number} is a circular prime.")
else:
    print(f"{number} is not a circular prime.")