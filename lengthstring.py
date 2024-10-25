fruit="mango"
p=len(fruit)
print(p)
print(fruit[:2])
print(fruit[3])
pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index
alphabets = "ABCDE"
for i in alphabets:
    print(i)
str1 = "AbcDEfghIJ"
print(str1.upper())
str2 = "AbcDEfghIJ"
print(str2.lower())
str2 = " Silver Spoon "
print(str2.strip)     #The strip() method removes any white spaces before and after the string.
str3 = "Hello !!!"
print(str3.rstrip("!"))     #the rstrip() removes any trailing characters
str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))
str2 = "Silver Spoon"
print(str2.split(" "))      #Splits the string at the whitespace " ".
str1 = "hello"
capStr1 = str1.capitalize()      #The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase.
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()      # The string has no effect if the first character is already uppercase.
print(capStr2)
str1 = "Welcome to the Console!!!"
print(str1.center(50))          #The center() method aligns the string to the center as per the parameters given by the user.
str2 = "Abracadabra"
countStr = str2.count("a")      #The count() method returns the number of times the given value has occurred within the given string.
print(countStr)
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))            #The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))           #The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))         #The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
str1 = "WelcomeToTheConsole"
print(str1.isalnum())           #The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
str1 = "Welcome"
print(str1.isalpha())         #The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
str1 = "hello world"
print(str1.islower())         #The islower() method returns True if all the characters in the string are lower case, else it returns False.
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())          #The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())                        #The isspace() method returns True only and only if the string contains white spaces, else returns False.
str1 = "World Health Organization" 
print(str1.istitle())                 #The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())            #The isupper() method returns True if all the characters in the string are upper case, else it returns False.
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))           #The endswith() method checks if the string starts with a given value. If yes then return True, else return False.
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())             #The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())               #The title() method capitalizes each letter of the word within the string.
